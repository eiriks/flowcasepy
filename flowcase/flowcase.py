#!/usr/bin/env python
# -*- coding: utf-8 -*-

# std lib
import logging
from functools import lru_cache
from typing import List, Literal, Optional

# 3rd party
import pydantic
import requests
from pydantic import ValidationError

# types
from flowcase.reportmanager import ReportManager
from flowcase.types.country import Countries, Office
from flowcase.types.customer import Customers
from flowcase.types.cv import CVResponse
from flowcase.types.department import Department
from flowcase.types.employee import Employee, EmployeeSearchResult
from flowcase.types.search_result import SearchResults
from flowcase.types.search_result_v4 import SearchResponseV4

# URLs
USERS_API_V2_SEARCH_URL = (
    "https://{org}.flowcase.com/api/v2/users/search?deactivated=false&name={name}"
)
USERS_API_V4_SEARCH_URL = "https://{org}.flowcase.com/api/v4/search"
CV_API_V3_URL_BASE = "https://{org}.flowcase.com/api/v3/cvs/{user_id}/{cv_id}"
# COUNTRIES_API_V1_URL = "https://{org}.cvpartner.com/api/v1/countries"
COUNTRIES_API_V1_URL = (
    "https://{org}.flowcase.com/api/v1/countries?use_legacy_codes=false"
)
CUSTOMER_API_V2_SEARCH_URL = "https://{org}.flowcase.com/api/v2/company/cv/customers?customer_name={customer_name}&size={size}&offset={offset}"
CUSTOMER_API_V2_URL = "https://{org}.flowcase.com/api/v2/company/cv/customers/{customer_id}/projects/{project_id}"

REFERENCE_REPORTS_API_V4_URL = "https://{org}.flowcase.com/api/v4/references/reports"

# logger
log = logging.getLogger(__name__)


class Flowcase:
    """Class for interacting with flowcase API. Docs for API at https://docs.flowcase.com/"""

    ERROR_MESSAGE_DECODE = "Couldn't decode response from Flowcase:\n"
    ERROR_MESSAGE_PARSE = "Couldn't parse response from Flowcase:\n"

    SEARCH_TYPES = Literal["free_text", "name", "technology_skill"]

    def __init__(self, org: str, api_key: str, verbose: bool = False):
        """Set up the Flowcase API client."""
        self._auth_header = {"Authorization": f'Token token="{api_key}"'}
        self.org = org
        """Name of the organization in Flowcase. It's the subdomain in the URL."""
        self.verbose = verbose
        """If True, print debug messages to stdout."""
        self.report_manager = ReportManager(
            REFERENCE_REPORTS_API_V4_URL.format(org=self.org), self._auth_header
        )

    def search(
        self,
        query_string: str,
        query_type: SEARCH_TYPES = "free_text",
        country_code: str = "no",
        office_ids: Optional[list[str]] = [],
        offset: int = 0,
        size: int = 10,
    ) -> SearchResponseV4:
        """Search for users in Flowcase.

        Args:
            office_ids: List of office IDs to search in.
            offset: Offset for the search results.
            size: Number of results to return.
            query_type: str, one of: free_text, name, technology_skill.
            query_value: Value to search for.
            field: Field to search in.
            tag: Tag to search for."""
        log.debug(
            f"Retrieving users with query type: {query_type} and value: {query_string}"
        )

        # if office_ids is empty, get all offices in the country
        if not office_ids:
            # make sure country is in [n.code for n in self.list_countries()]
            if country_code not in [n.code for n in self.list_countries()]:
                raise ValueError(
                    f"Country code {country_code} not found in organization."
                )
            # grab the office ids for the country
            office_ids = [o.id for o in self.list_offices_from_country(country_code)]

        # print the office_ids and country_code
        log.debug(
            f"Searching with Country code: '{country_code}' Office IDs: {office_ids}"
        )

        # Construct the query based on the type
        must_clause = []
        if query_type == "free_text":
            must_clause.append({"query": {"value": query_string}})
        elif query_type == "name":
            must_clause.append(
                {
                    "bool": {
                        "should": [{"query": {"field": "name", "value": query_string}}]
                    }
                }
            )
        elif query_type == "technology_skill":
            must_clause.append({"technology_skill": {"tag": query_string}})
        else:
            raise ValueError(f"query_type must be one of {self.SEARCH_TYPES}")

        # Construct the full request body
        data = {
            "office_ids": office_ids,
            "offset": offset,
            "size": size,
            "must": must_clause,
        }

        search_url = USERS_API_V4_SEARCH_URL.format(org=self.org)
        r = requests.post(search_url, headers=self._auth_header, json=data)

        try:
            user_data = r.json()
        except requests.exceptions.JSONDecodeError:
            print(self.ERROR_MESSAGE_DECODE + r.text)
            raise

        try:
            search_result: SearchResponseV4 = SearchResponseV4.model_validate(user_data)
        except pydantic.ValidationError:
            print(self.ERROR_MESSAGE_PARSE + r.text)
            raise

        return search_result

    def search_users(self, query: str, only_norway=True) -> SearchResults:
        log.debug(f"Retreiving user {query} from API...")
        search_url = USERS_API_V2_SEARCH_URL.format(org=self.org, name=query)

        if only_norway:
            offices_url = ""
            for office in self.list_offices_from_country(country_code="no"):
                offices_url += f"&office_ids[]={office.id}"
            search_url += offices_url

        r = requests.get(search_url, headers=self._auth_header)
        try:
            user_data = r.json()
        except requests.exceptions.JSONDecodeError:
            print(self.ERROR_MESSAGE_DECODE + r.text)
            raise

        try:
            search_result: SearchResults = SearchResults.model_validate(user_data)
        except pydantic.ValidationError:
            print(self.ERROR_MESSAGE_PARSE + r.text)
            raise

        return search_result

    def generate_reference_report(self):
        """Generate a reference report from Flowcase."""

        return self.report_manager.generate_report()

    @lru_cache(maxsize=1)
    def get_emploees_by_department(
        self, office_name: str = "Data Engineering", size=100
    ) -> List[Employee]:
        # find office ID from name
        offices = self.list_offices_from_country()
        # filter down to only the match, if any

        office_id = [o.id for o in offices if o.name == office_name][0]

        if not office_id:
            log.warning(f"No office found with name {office_name}!")
            return []
        # do a "search" for users in that office
        url = USERS_API_V4_SEARCH_URL.format(org=self.org)

        params = {
            "office_ids": [office_id],
            "offset": 0,
            "size": size,
            "deactivated": False,
        }

        r = requests.post(url, json=params, headers=self._auth_header)

        try:
            user_data = r.json()
        except requests.exceptions.JSONDecodeError:
            print(self.ERROR_MESSAGE_DECODE + r.text)
            raise

        try:
            search_result: EmployeeSearchResult = EmployeeSearchResult.model_validate(
                user_data
            )
            # return list of Employee objects
            return [emp_meta.cv for emp_meta in search_result.cvs]

        except pydantic.ValidationError:
            print(self.ERROR_MESSAGE_PARSE + r.text)
            raise

    @lru_cache(maxsize=1)
    def get_emploees_and_cvs_from_department(
        self, office_name: str = "Data Engineering", size=100
    ) -> Department:
        """Get employees and their CVs from a department.

        The results are cached since this data rarely changes.
        Use Flowcase.get_emploees_and_cvs_from_department.cache_clear() to force a refresh.
        """
        # this fails by returning 100, it should be limited to size of department...
        # TODO: fix this

        users: list[Employee] = self.get_emploees_by_department(office_name, size)

        cvs: list[CVResponse] = [
            self.get_user_cv(user.user_id, user.id) for user in users
        ]
        # the_dep = []
        the_dep = list(zip(users, cvs))
        try:
            department: Department = Department.model_validate({"root": the_dep})
            return department
        except pydantic.ValidationError:
            print(self.ERROR_MESSAGE_PARSE + office_name)
            raise

    def get_user_cv(self, user_id: str, cv_id: str) -> CVResponse:
        log.debug(f"Retreiving user {user_id} CV {cv_id} from API...")
        cv_url = CV_API_V3_URL_BASE.format(org=self.org, user_id=user_id, cv_id=cv_id)
        r = requests.get(cv_url, headers=self._auth_header)
        try:
            cv_data = r.json()
        except requests.exceptions.JSONDecodeError:
            print(self.ERROR_MESSAGE_DECODE + r.text)
            raise

        try:
            cv = CVResponse(**cv_data)

        except pydantic.ValidationError as e:
            print(self.ERROR_MESSAGE_PARSE + str(e))
            raise

        return cv

    @lru_cache(maxsize=1)  # cache the result, Countries class should be one result.
    def list_countries(self) -> Countries:
        """Lists the countries in the organization.

        The results are cached since this data rarely changes.
        Use Flowcase.list_countries.cache_clear() to force a refresh.
        """
        url = COUNTRIES_API_V1_URL.format(org=self.org)
        r = requests.get(url, headers=self._auth_header)
        try:
            data = r.json()
        except requests.exceptions.JSONDecodeError as e:
            print(self.ERROR_MESSAGE_DECODE + r.text)
            raise ValueError(f"{self.ERROR_MESSAGE_DECODE}{r.text}") from e

        try:
            return Countries.model_validate(data)
        except pydantic.ValidationError as e:
            print(self.ERROR_MESSAGE_PARSE + r.text)
            raise ValidationError(f"{self.ERROR_MESSAGE_PARSE}{r.text}") from e

    @lru_cache(maxsize=1)  # cache the result, Countries class should be one result.
    def list_offices_from_country(self, country_code: str = "no") -> list[Office]:
        """return name and Id of offices, aka departments

        The results are cached since this data rarely changes.
        Use Flowcase.list_offices_from_country.cache_clear() to force a refresh.
        """
        countries: Countries = self.list_countries()
        offices = [c.offices for c in countries.root if c.code == country_code][0]
        return offices

    @lru_cache(maxsize=1)
    def get_department_names(self, country_code: str = "no") -> List[str]:
        """return name of offices, aka departments"""
        offices = self.list_offices_from_country(country_code)
        return [o.name for o in offices]

    @lru_cache(maxsize=1)
    def get_country_codes(self) -> List[str]:
        """return country codes"""
        countries = self.list_countries()
        return [c.code for c in countries.root]

    # this method is not used by anything? remove?
    def get_customers_by_name(self, customer_name: str, size=10, offset=0) -> Customers:
        url = CUSTOMER_API_V2_SEARCH_URL.format(
            org=self.org, customer_name=customer_name, size=size, offset=offset
        )
        r = requests.get(url, headers=self._auth_header)

        try:
            data = r.json()
        except requests.exceptions.JSONDecodeError:
            print(self.ERROR_MESSAGE_DECODE + r.text)
            raise

        try:
            return Customers.model_validate(data)
        except pydantic.ValidationError:
            print(self.ERROR_MESSAGE_PARSE + r.text)
            raise
