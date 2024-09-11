import os

import pytest

# import requests_mock
from cvpartner import CVPartner
from cvpartner.types.customer import Customers


@pytest.fixture
def cv_partner():
    return CVPartner(org="noaignite", api_key=os.environ["CVPARTNER_API_KEY"])


def test_get_customers_by_name(cv_partner):
    customers = cv_partner.get_customers_by_name("nor", size=10, offset=0)
    assert type(customers) is Customers
    assert len(customers) == 10


# def test_get_customer_success(cv_partner, requests_mock):
#     # Mock the requests library to return a successful response
#     requests_mock.get(
#         'https://api.cvpartner.com/v1/orgs/noaignite/customers?customer_name=example&size=10&offset=0',
#         json=[
#             {"id": 1, "name": "Example Customer 1"},
#             {"id": 2, "name": "Example Customer 2"}
#         ],
#         status_code=200
#     )

#     # Call the method under test
#     customers = cv_partner.get_customer("example")

#     # Assert the expected result
#     assert len(customers) == 2
#     assert customers[0].id == 1
#     assert customers[0].name == "Example Customer 1"
#     assert customers[1].id == 2
#     assert customers[1].name == "Example Customer 2"


# def test_get_customer_error(cv_partner, requests_mock):
#     # Mock the requests library to return an error response
#     requests_mock.get(
#         'https://api.cvpartner.com/v1/orgs/noaignite/customers?customer_name=example&size=10&offset=0',
#         json={"error": "Invalid API key"},
#         status_code=401
#     )

#     # Call the method under test and assert that it raises an exception
#     with pytest.raises(requests.exceptions.HTTPError):
#         cv_partner.get_customer("example")
