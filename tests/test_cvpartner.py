import os
import re

import pytest
import requests_mock

from cvpartner import CVPartner


@pytest.fixture
def cv_partner():
    return CVPartner(org="noaignite", api_key=os.environ["CVPARTNER_API_KEY"])


def test_initiate_report_success(cv_partner):
    # Mock the requests library to return a successful response
    with requests_mock.Mocker() as m:
        m.post(
            re.compile(r"https://.*\.cvpartner\.com/api/v4/references/reports"),
            json={"id": "report123"},
            status_code=200,
        )

        # Call the method under test
        report_id = cv_partner.initiate_report()

        # Assert the expected result
        assert report_id == "report123"


def test_initiate_report_failure(cv_partner):
    # Mock the requests library to return an error response
    with requests_mock.Mocker() as m:
        m.post(
            re.compile(r"https://.*\.cvpartner\.com/api/v4/references/reports"),
            json={"error": "Invalid request"},
            status_code=400,
        )

        # Call the method under test and assert that it raises an exception
        with pytest.raises(Exception, match="Failed to initiate report: 400"):
            cv_partner.initiate_report()
