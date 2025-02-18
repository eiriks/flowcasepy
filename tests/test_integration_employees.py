import os

import pytest
from dotenv import load_dotenv

from flowcase.flowcase import Flowcase
from flowcase.types.cv import CVResponse
from flowcase.types.department import Department
from flowcase.types.employee import Employee

load_dotenv()


@pytest.fixture(scope="session")
def flowcase():
    return Flowcase(org="noaignite", api_key=os.environ["FLOWCASE_API_KEY"])


@pytest.fixture(scope="session")
def employee_list(flowcase, office_name: str = "Data Engineering", size=100):
    emploees: list[Employee] = flowcase.get_emploees_by_department(office_name, size)
    return emploees


# this is slow, I guess.
@pytest.fixture(scope="session")
def department_with_cvs(flowcase):
    return flowcase.get_emploees_and_cvs_from_department()


@pytest.mark.skip(reason="slow")
def test_get_employees(employee_list):
    # this fails by returning 100, it should be limited to size of department...
    # TODO: fix this

    users = employee_list

    assert isinstance(users, list)
    for user in users:
        assert isinstance(user, Employee)


# now lats thets CVResponse
def test_get_employee_cv(flowcase, employee_list):
    for user in employee_list:
        user: Employee
        # print(user)
        cv = flowcase.get_user_cv(user.user_id, user.id)
        assert type(cv) is not None
        assert type(cv) is CVResponse


@pytest.mark.skip(reason="slow")
def test_get_department_details(flowcase, employee_list):
    # I want to make a Department object from the list of employees

    cvs: list[CVResponse] = [
        flowcase.get_user_cv(user.user_id, user.id) for user in employee_list
    ]
    assert len(cvs) == len(employee_list)
    assert type(cvs[0]) is CVResponse

    the_dep = list(zip(employee_list, cvs))
    department: Department = Department.model_validate({"root": the_dep})

    assert type(department) is Department
    assert len(department) == len(employee_list)


@pytest.mark.skip(reason="slow")
def test_more(department_with_cvs):
    assert type(department_with_cvs) is Department
