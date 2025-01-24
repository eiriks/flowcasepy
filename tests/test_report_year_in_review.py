import os

import pytest
from dotenv import load_dotenv

from flowcase import Flowcase
from flowcase.make_slides import make_ppt_from_year_in_review
from flowcase.reports import get_year_in_review

load_dotenv()


@pytest.fixture
def cv_partner():
    return Flowcase(org="noaignite", api_key=os.environ["FLOWCASE_API_KEY"])


@pytest.mark.skip(reason="TDD")
def test_report_year_in_review(cv_partner):
    department = cv_partner.get_emploees_and_cvs_from_department()

    result = get_year_in_review(department=department)

    assert len(result) > 0


@pytest.mark.skip(reason="This makes a new ppt every time. Not necessary")
def test_make_ppt_from_year_in_review(cv_partner):
    department = cv_partner.get_emploees_and_cvs_from_department()

    (
        projects_worked_on,
        new_courses,
        new_certifications,
        new_presentations,
        new_honors_and_awards,
    ) = get_year_in_review(department=department)

    worked = make_ppt_from_year_in_review(
        projects_worked_on,
        new_courses,
        new_certifications,
        new_presentations,
        new_honors_and_awards,
        department_name="Data engineering",
    )

    assert worked is True
