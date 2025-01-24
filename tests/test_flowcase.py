import os
import re
from unittest.mock import patch

import pytest
import requests_mock
from dotenv import load_dotenv

from flowcase import Flowcase
from flowcase.types.country import Countries

load_dotenv()


@pytest.fixture
def cv_partner():
    return Flowcase(org="noaignite", api_key=os.environ["FLOWCASE_API_KEY"])


@pytest.fixture
def mock_countries_response():
    return [
        {
            "_id": "country1_id",
            "id": "country1",
            "code": "no",
            "native_language_code": "nb",
            "override_ui_language_code": "en",
            "selected": True,
            "default_ppt_template_id": False,
            "default_word_template_id": False,
            "offices": [
                {
                    "_id": "office1_id",
                    "id": "office1",
                    "name": "Content Design",
                    "selected": True,
                    "default_word_template_id": False,
                    "default_ppt_template_id": False,
                    "country_id": "country1",
                    "country_code": "NO",
                    "override_language_code": False,
                    "num_users": 50,
                    "num_users_activated": 45,
                    "num_users_deactivated": 5,
                },
                {
                    "_id": "office2_id",
                    "id": "office2",
                    "name": "Backend",
                    "selected": False,
                    "default_word_template_id": False,
                    "default_ppt_template_id": False,
                    "country_id": "country1",
                    "country_code": "no",
                    "override_language_code": False,
                    "num_users": 30,
                    "num_users_activated": 28,
                    "num_users_deactivated": 2,
                },
            ],
            "setting": {"_id": "setting1_id"},
        },
        {
            "_id": "country2_id",
            "id": "country2",
            "code": "SE",
            "native_language_code": "sv",
            "override_ui_language_code": "no",
            "selected": False,
            "default_ppt_template_id": False,
            "default_word_template_id": False,
            "offices": [
                {
                    "_id": "office3_id",
                    "id": "office3",
                    "name": "Stockholm Office",
                    "selected": True,
                    "default_word_template_id": False,
                    "default_ppt_template_id": False,
                    "country_id": "country2",
                    "country_code": "SE",
                    "override_language_code": False,
                    "num_users": 40,
                    "num_users_activated": 38,
                    "num_users_deactivated": 2,
                }
            ],
            "setting": {"_id": "setting2_id"},
        },
    ]


def test_initiate_report_success(cv_partner):
    # Mock the requests library to return a successful response
    with requests_mock.Mocker() as m:
        m.post(
            re.compile(r"https://.*\.flowcase\.com/api/v4/references/reports"),
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
            re.compile(r"https://.*\.flowcase\.com/api/v4/references/reports"),
            json={"error": "Invalid request"},
            status_code=400,
        )

        # Call the method under test and assert that it raises an exception
        with pytest.raises(Exception, match="Failed to initiate report: 400"):
            cv_partner.initiate_report()


def test_list_countries_success(cv_partner, mock_countries_response):
    with patch("requests.get") as mock_get:
        mock_get.return_value.json.return_value = mock_countries_response
        mock_get.return_value.status_code = 200

        countries = cv_partner.list_countries()

        # print(
        #     isinstance(countries, Countries),
        #     len(countries.root),
        #     countries.root[0].code,
        #     len(countries.root[0].offices),
        #     countries.root[0].offices[0].name,
        # )
        assert isinstance(countries, Countries)
        assert len(countries.root) == 2
        assert countries.root[0].code == "no"
        assert len(countries.root[0].offices) == 2
        assert countries.root[0].offices[0].name == "Content Design"


# def test_list_countries_api_error(cv_partner):
#     with patch("requests.get") as mock_get:
#         mock_get.return_value.status_code = 500
#         mock_get.return_value.text = "Internal Server Error"

#         with pytest.raises(Exception):
#             cv_partner.list_countries()
