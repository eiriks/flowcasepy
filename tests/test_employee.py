import json

import pytest

from cvpartner.types.employee import Employee

department = json.loads(open("tests/data/department.json").read())


def test_employee():
    employee = Employee(**department[0])
    print(employee)
    assert type(employee.name) is str
    assert len(employee.name) > 0


def test_employees():
    employees = [Employee(**emp) for emp in department]

    assert type(employees[len(employees) - 1].name) is str
    assert len(employees[0].name) > 0
    assert type(employees[0]) is Employee


@pytest.mark.skip(reason="Lots of params are required")
def test_new_employee():
    employee = Employee(name="John Doe", company_name="NoAignite")
    # print(employee)
    assert employee.name == "John Doe"
