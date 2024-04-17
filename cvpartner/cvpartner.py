#!/usr/bin/env python
# -*- coding: utf-8 -*-

# std lib
import logging
from typing import List
from cvpartner.types.customer import Customer, Customers


from cvpartner.types.cv import CVResponse
from cvpartner.types.country import Countries, Country, Office
from cvpartner.types.department import Department
from cvpartner.types.employee import SearchResult, Employee


# 3rd party
import requests
import pydantic



# URLs
USERS_URL_BASE = "https://{org}.cvpartner.com/api/v1/users?offset={offset}"
USERS_URL_BASE_SEARCH = "https://{org}.cvpartner.com/api/v2/users/search?deactivated=false&size={size}&office_ids[]={office_id}"
USERS_URL_BASE_SEARCH_V4 = "https://{org}.cvpartner.com/api/v4/search"
CV_URL_BASE = "https://{org}.cvpartner.com/api/v3/cvs/{user_id}/{cv_id}"

COUNTRIES = "https://{org}.cvpartner.com/api/v1/countries"

# Not sure I even need these..
URL_CUSTOMER_SEARCH = "https://{org}.cvpartner.com/api/v2/company/cv/customers?customer_name={customer_name}&size={size}&offset={offset}"
URL_CUSTOMER = "https://{org}.cvpartner.com/api/v2/company/cv/customers/{customer_id}/projects/{project_id}"


# logger
log = logging.getLogger(__name__)


class CVPartner():
    ERROR_MESSAGE_DECODE = "Couldn't decode response from CVPartner:\n"
    ERROR_MESSAGE_PARSE = "Couldn't parse response from CVPartner:\n"

    def __init__(self, org, api_key: str, verbose: bool = False):
        self.auth_header = {"Authorization": f'Token token="{api_key}"'}
        self.org = org
        self.verbose = verbose

    def get_customers_by_name(self, customer_name: str, size=10, offset=0):
        url = URL_CUSTOMER_SEARCH.format(
            org=self.org, customer_name=customer_name, size=size, offset=offset)
        r = requests.get(url, headers=self.auth_header)

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

    def get_emploees_by_department(self, office_name: str = 'Data Engineering', size=100) -> None | List[Employee]:
        # find office ID from name
        offices = self.get_offices_from_country()
        # filter down to only the match, if any


        office_id = [o.id for o in offices if o.name == office_name][0]

        if not office_id:
            log.warning(f'No office found with name {office_name}!')
            return []
        # do a "search" for users in that office
        url = USERS_URL_BASE_SEARCH_V4.format(org=self.org)

        params = {
            "office_ids": [office_id],
            "offset": 0,
            "size": size,
            "deactivated": False,
        }

        r = requests.post(url, json=params, headers=self.auth_header)

        try:
            user_data = r.json()
        except requests.exceptions.JSONDecodeError:
            print(self.ERROR_MESSAGE_DECODE + r.text)
            raise

        try:
            search_result: SearchResult = SearchResult.model_validate(user_data)
            # return list of Employee objects
            return [emp_meta.cv for emp_meta in search_result.cvs]

        except pydantic.ValidationError:
            print(self.ERROR_MESSAGE_PARSE + r.text)
            raise

    def get_emploees_and_cvs_from_department(self, office_name: str = 'Data Engineering', size=100) -> Department | None:
        # this fails by returning 100, it should be limited to size of department...
        # TODO: fix this

        users: list[Employee] = self.get_emploees_by_department(
            office_name, size)

        the_dep = []

        for user in users:
            cv = self.get_user_cv(user.user_id, user.id)
            the_dep.append((user, cv))


        try:
            return Department(root=the_dep)

        except pydantic.ValidationError:
            print(self.ERROR_MESSAGE_PARSE + office_name)
            raise

    def get_user_cv(self, user_id: str, cv_id: str) -> CVResponse:
        log.debug(f'Retreiving user {user_id} CV {cv_id} from API...')
        cv_url = CV_URL_BASE.format(
            org=self.org, user_id=user_id, cv_id=cv_id)
        r = requests.get(cv_url, headers=self.auth_header)
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

    def list_countries(self) -> Countries:
        url = COUNTRIES.format(org=self.org)
        r = requests.get(url, headers=self.auth_header)
        try:
            data = r.json()
        except requests.exceptions.JSONDecodeError:
            print(self.ERROR_MESSAGE_DECODE + r.text)
            raise

        try:
            return Countries.model_validate(data)
        except pydantic.ValidationError:
            print(self.ERROR_MESSAGE_PARSE + r.text)
            raise

    # should return list[Office] ?``
    def get_offices_from_country(self, country_code: str = 'no') -> list[Office]:
        """return name and Id of offices, aka departments"""
        countries: Countries = self.list_countries()
        offices = [c.offices for c in countries.root if c.code == country_code][0]
        return offices
