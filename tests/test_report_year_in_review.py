import os
import pytest

from cvpartner import CVPartner
from cvpartner.reports import get_year_in_review

from cvpartner.make_slides import make_ppt_from_year_in_review


@pytest.fixture
def cv_partner():
    return CVPartner(org='noaignite', api_key=os.environ['CVPARTNER_API_KEY'])



@pytest.mark.skip(reason="TDD")
def test_report_year_in_review(cv_partner):

    department = cv_partner.get_emploees_and_cvs_from_department()

    result = get_year_in_review(department=department)

    assert len(result) > 0


@pytest.mark.skip(reason="This makes a new ppt every time. Not necessary")
def test_make_ppt_from_year_in_review(cv_partner):
    department = cv_partner.get_emploees_and_cvs_from_department()

    projects_worked_on, new_courses, new_certifications, new_presentations, new_honors_and_awards \
          = get_year_in_review(department=department)

    worked = make_ppt_from_year_in_review(
                                        projects_worked_on, new_courses,
                                        new_certifications, new_presentations,
                                        new_honors_and_awards,
                                        department_name='Data engineering')


    assert worked == True