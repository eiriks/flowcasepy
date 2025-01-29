import pytest

from flowcase.helpers import get_proper_project_dates


def test_valid_year_month_day():
    result = get_proper_project_dates(2023, 10, 15)
    assert result.year == 2023
    assert result.month == 10
    assert result.day == 15


def test_valid_year_month_default_day():
    result = get_proper_project_dates(2023, 10)
    assert result.year == 2023
    assert result.month == 10
    assert result.day == 1


def test_valid_year_default_month_day():
    result = get_proper_project_dates(2023)
    assert result.year == 2023
    assert result.month == 1
    assert result.day == 1


def test_invalid_month():
    with pytest.raises(ValueError):
        get_proper_project_dates(2023, 13, 1)


def test_invalid_day():
    with pytest.raises(ValueError):
        get_proper_project_dates(2023, 10, 32)


def test_invalid_year():
    with pytest.raises(ValueError):
        get_proper_project_dates("invalid_year", 10, 1)


def test_none_month():
    result = get_proper_project_dates(2023, None, 15)
    assert result.year == 2023
    assert result.month == 1
    assert result.day == 15


def test_empty_string_month():
    result = get_proper_project_dates(2023, "", 15)
    assert result.year == 2023
    assert result.month == 1
    assert result.day == 15

    result = get_proper_project_dates(2023, None, 15)
    assert result.year == 2023
    assert result.month == 1
    assert result.day == 15

    result = get_proper_project_dates(2023, "0", 15)
    assert result.year == 2023
    assert result.month == 1
    assert result.day == 15


def test_none_day():
    result = get_proper_project_dates(2023, 10, None)
    assert result.year == 2023
    assert result.month == 10
    assert result.day == 1

    result = get_proper_project_dates(2023, 10, "")
    assert result.year == 2023
    assert result.month == 10
    assert result.day == 1

    result = get_proper_project_dates(2023, 10)
    assert result.year == 2023
    assert result.month == 10
    assert result.day == 1
