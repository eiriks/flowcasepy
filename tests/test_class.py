import os
from datetime import datetime

import pytest

from cvpartner import CVPartner
from cvpartner.helpers import get_age, get_role_from_cv_roles
from cvpartner.types.cv import CVResponse
from cvpartner.types.employee import Employee


@pytest.fixture
def cv_partner():
    return CVPartner(org="noaignite", api_key=os.environ["CVPARTNER_API_KEY"])


def test_class_instanciation_using_fixture(cv_partner):
    assert cv_partner


def test_get_emploees_by_department(cv_partner):
    t0 = datetime.now()
    department = cv_partner.get_emploees_by_department()
    # assert I get a list of Employees back
    assert isinstance(department, list)
    assert isinstance(department[0], Employee)

    t1 = datetime.now() - t0
    print(f"t1: {t1}")
    t2 = datetime.now() - t0
    print(f"t2: {t2}")
    print(len(department))
    assert len(department) > 0


@pytest.mark.skip(reason="This is so slow..")  # slow, 30+ seconds
def test_get_emploees_and_cvs_from_department(cv_partner):
    department = cv_partner.get_emploees_and_cvs_from_department()
    print(len(department))
    assert len(department) > 0


def test_age():
    cv = CVResponse(
        born_year=datetime.now().year - 40,
        born_day=1,
        born_month=1,
        _id="123",
        bruker_id="123",
        cv_roles=[],
        navn="Testing",
        title={"no": "Konge"},
    )

    assert get_age(cv) == 40


SOFTWARE_UTVIKLER = "Software Utvikler"


def test_get_role_from_cv_roles_no_lang():
    cv_role = {"name": {"no": "software developer."}}
    assert get_role_from_cv_roles(cv_role) == SOFTWARE_UTVIKLER


def test_get_role_from_cv_roles_en_lang():
    cv_role = {"name": {"en": "software developer"}}
    assert get_role_from_cv_roles(cv_role, lang="en") == SOFTWARE_UTVIKLER


def test_get_role_from_cv_roles_with_dot():
    cv_role = {"name": {"no": "software developer."}}
    assert get_role_from_cv_roles(cv_role) == SOFTWARE_UTVIKLER


def test_get_role_from_cv_roles_with_slash():
    cv_role = {"name": {"no": "Tech Lead/Utvikler"}}
    assert get_role_from_cv_roles(cv_role) == "Tech Lead / Utvikler"


def test_get_role_from_cv_roles_empty_string():
    cv_role = {"name": {"no": ""}}
    assert get_role_from_cv_roles(cv_role) == ""


def test_get_role_from_cv_roles_none():
    cv_role = {"name": {}}
    assert get_role_from_cv_roles(cv_role) is None
