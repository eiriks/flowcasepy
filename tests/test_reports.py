import os
import pytest
from cvpartner import CVPartner


# from cvpartner.reports import get_value_additions_last_period


@pytest.fixture
def cv_partner():
    return CVPartner(org='noaignite', api_key=os.environ['CVPARTNER_API_KEY'])


def test_get_value_additions_last_period(cv_partner):
    cv = cv_partner.get_user_cv("5a16db4c40566607dc9eb862",
                                "5a16db4c40566607dc9eb863")

    # get_value_additions_last_period(cv, days_to_look_back=1365)
