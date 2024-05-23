import os
import pytest

from cvpartner import CVPartner

from cvpartner.helpers import get_highest_degree, get_graduation_year, get_email

from cvpartner.helpers import remove_extra_whitespace, remove_ending_period, convert_developer_to_utvikler, \
    convert_enginer_to_engineer, rename_common_variations_in_dev, get_role_from_cv_roles
from cvpartner.types.search_result import SearchResults


def test_remove_extra_whitespace():
    assert remove_extra_whitespace("   a  b  c  ") == "a b c"
    assert remove_extra_whitespace("a\tb\tc") == "a b c"


def test_remove_ending_period():
    assert remove_ending_period("abcd.") == "abcd"
    assert remove_ending_period("abcd") == "abcd"


def test_convert_developer_to_utvikler():
    assert convert_developer_to_utvikler("Developer") == "utvikler"
    assert convert_developer_to_utvikler("developer") == "utvikler"


def test_convert_enginer_to_engineer():
    assert convert_enginer_to_engineer("Enginer") == "engineer"
    assert convert_enginer_to_engineer("enginer") == "engineer"


def test_rename_common_variations_in_dev():
    assert rename_common_variations_in_dev(
        "Back End Developer") == "Backend Utvikler"


def test_get_role_from_cv_roles():
    cv_role = {'name': {'no': 'Back End Developer.'}}
    assert get_role_from_cv_roles(cv_role) == "Backend Utvikler"
    cv_role = {'name': {'no': 'Enginer'}}
    assert get_role_from_cv_roles(cv_role) == "Engineer"
    cv_role = {'name': {'no': None}}
    assert get_role_from_cv_roles(cv_role) is None


@pytest.fixture
def cv_partner():
    return CVPartner(org='noaignite', api_key=os.environ['CVPARTNER_API_KEY'])


def test_get_highest_degree(cv_partner):
    cv = cv_partner.get_user_cv("5702cc5f69702d53c10088e8",
                                "5702cc5f69702d53c10088e9")
    assert get_highest_degree(cv) == 'bachelor'


def test_get_graduation_year(cv_partner):
    cv = cv_partner.get_user_cv("5702cc5f69702d53c10088e8",
                                "5702cc5f69702d53c10088e9")
    assert get_graduation_year(cv) == 1998


def test_get_email(cv_partner):
    cv = cv_partner.get_user_cv("5a16db4c40566607dc9eb862",
                                "5a16db4c40566607dc9eb863")
    assert get_email(cv) == 'eirik.stavelin@noaignite.com'

#    exam_year[person.name] = {'degree': get_highest_degree(cv),
#                                       'graduation_year': get_graduation_year(cv),
#                                       'email': get_email(person)}


def test_serach(cv_partner):
    results = cv_partner.search_users("Eirik Stavelin")
    assert type(results) == SearchResults