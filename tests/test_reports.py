import os

import pytest
from dotenv import load_dotenv

from flowcase import Flowcase

# from flowcase.reports import get_value_additions_last_period


load_dotenv()


@pytest.fixture
def cv_partner():
    return Flowcase(org="noaignite", api_key=os.environ["FLOWCASE_API_KEY"])


def test_get_value_additions_last_period(cv_partner):
    cv = cv_partner.get_user_cv("5a16db4c40566607dc9eb862", "5a16db4c40566607dc9eb863")
    assert cv is not None
    # get_value_additions_last_period(cv, days_to_look_back=1365)
