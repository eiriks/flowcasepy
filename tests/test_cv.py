
import os
from cvpartner.types.country import Country
from cvpartner import CVPartner
from typing import List
import datetime
import json
from pydantic import parse_obj_as
import pytest
from cvpartner.helpers import get_days_since_last_finished_project


from cvpartner.types.cv import CVResponse
from cvpartner.types.department import Department


# get department with cvs
department_with_cv = json.loads(
    open('tests/data/department_with_cvs.json').read())


def test_mapping_department():
    # department_with_cv = Department(**department_with_cv)
    department_with_cv_object = parse_obj_as(Department, department_with_cv)
    assert type(department_with_cv_object) == Department


def test_single_cv():
    _cv = department_with_cv[0][1]
    # print()
    cv = CVResponse(**_cv)
    # print(cv)

    assert type(cv.name) == str
    assert len(cv.name) > 0


def test_cv():
    # print(department_with_cv[0][1])
    cv = CVResponse(**department_with_cv[0][1])
    # print(cv)

    assert type(cv.name) == str
    assert len(cv.name) > 0


# @pytest.mark.skip(reason="not implemented")
def test_cvs():
    cvs = [CVResponse(**cv[1]) for cv in department_with_cv]

    assert type(cvs[len(cvs)-1].name) == str
    assert len(cvs[len(cvs)-1].name) > 0
    assert type(cvs[0]) == CVResponse


@pytest.mark.parametrize("project, expected_days", [
    (('Project1', datetime.datetime.now() -
     datetime.timedelta(days=365), 'Company1', 'Description1'), 365),
    (('Project2', None, 'Company2', 'Description2'), 0)
])
def test_get_days_since_last_finished_project(project, expected_days):
    assert get_days_since_last_finished_project(project) == expected_days


# q: how to run a spesific test iun pytest?


@pytest.fixture
def cv_partner():
    return CVPartner(org='noaignite', api_key=os.environ['CVPARTNER_API_KEY'])


def test_get_employees_by_department(cv_partner):
    employees = cv_partner.get_emploees_by_department()
    assert isinstance(employees, list)
    # assert len(employees) == 100


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
    countries = cv_partner.list_countries()
    assert isinstance(countries, List)


def test_list_offices(cv_partner):
    offices = cv_partner.list_offices()
    assert isinstance(offices, list)
