import datetime
import json
import os

import pytest
from dotenv import load_dotenv

from flowcase import Flowcase
from flowcase.helpers import get_days_since_last_finished_project
from flowcase.types.country import Countries
from flowcase.types.cv import CVResponse
from flowcase.types.department import Department

load_dotenv()

# get department with cvs
department_with_cv = json.loads(open("tests/data/department_with_cvs.json").read())


@pytest.mark.skip(
    reason="go back and encure that the json file is correct. Ither it is old and in wrong format, or this model_validate is no longer used in pydantic V2"
)
def test_mapping_department():
    department_with_cv_object = Department.model_validate(department_with_cv)
    assert type(department_with_cv_object) is Department


def test_single_cv():
    _cv = department_with_cv[0][1]
    cv = CVResponse(**_cv)

    assert isinstance(cv.name, str)
    assert len(cv.name) > 0


def test_cv():
    # print(department_with_cv[0][1])
    cv = CVResponse(**department_with_cv[0][1])
    # print(cv)

    assert isinstance(cv.name, str)
    assert len(cv.name) > 0


# @pytest.mark.skip(reason="not implemented")
def test_cvs():
    cvs = [CVResponse(**cv[1]) for cv in department_with_cv]

    assert isinstance(cvs[len(cvs) - 1].name, str)
    assert len(cvs[len(cvs) - 1].name) > 0
    assert isinstance(cvs[0], CVResponse)


@pytest.mark.parametrize(
    "project, expected_days",
    [
        (
            (
                "Project1",
                datetime.datetime.now() - datetime.timedelta(days=365),
                "Company1",
                "Description1",
            ),
            365,
        ),
        (("Project2", None, "Company2", "Description2"), 0),
    ],
)
def test_get_days_since_last_finished_project(project, expected_days):
    assert get_days_since_last_finished_project(project) == expected_days


# q: how to run a spesific test iun pytest?


@pytest.fixture
def cv_partner():
    return Flowcase(org="noaignite", api_key=os.environ["FLOWCASE_API_KEY"])


def test_get_employees_by_department(cv_partner):
    employees = cv_partner.get_emploees_by_department()
    assert isinstance(employees, list)


@pytest.mark.skip(reason="takes 20s")
def test_get_employees_and_cvs_from_department(cv_partner):
    department = cv_partner.get_emploees_and_cvs_from_department()
    assert isinstance(department, Department)


def test_get_user_cv(cv_partner):
    user_id = "5a16db4c40566607dc9eb862"
    cv_id = "5a16db4c40566607dc9eb863"
    cv = cv_partner.get_user_cv(user_id, cv_id)
    assert isinstance(cv, CVResponse)


def test_list_countries(cv_partner):
    countries: Countries = cv_partner.list_countries()
    assert isinstance(countries, Countries)


def test_list_offices(cv_partner):
    offices = cv_partner.list_offices_from_country()
    assert isinstance(offices, list)
