import json

import pytest

department = json.loads(open("tests/data/department.json").read())


print(department[0])


# write a dataclass for employee


# List emploees that are about to be promoted js>ks>sr>principal


@pytest.mark.skip(reason="TDD")
def test_list_emploees_that_are_about_to_be_promoted():
    assert False


# List dept by time since highest edu was ended
@pytest.mark.skip(reason="TDD")
def test_list_dept_by_time_since_highest_edu_ended():
    assert False


# List dept by time since first project_expeirence was started
@pytest.mark.skip(reason="TDD")
def test_list_dept_by_time_since_first_project_expeirence_was_started():
    assert False


# List dept by times sinze last project_expeirence that was longer than 3 months
# (expected to filter out summer jobs, internships etc)


@pytest.mark.skip(reason="TDD")
def test_list_dept_by_time_sinze_last_project_expeirence_that_was_longer_than_3_months():
    assert False


# List department by time since last updated by user
@pytest.mark.skip(reason="TDD")
def test_list_department_by_time_since_last_updated_by_user():
    assert False


# group adpartment into 4 groups:
# 1. 0-1 years (junior)
# 2. >2 years (konsultant)
# 3. >5 years (senior)
# 4. >10 years (principal)
@pytest.mark.skip(reason="TDD")
def test_group_department_into_4_groups():
    assert False


# group department into 4 levels:
# • Level 1: 8 < years experience
# Selvstendige konsulenter med lang erfaring - over de siste 8 år som er relevant for det aktuelle området. Konsulenten har høyere utdanning, manglende utdanning kan kompenseres med lengre erfaring.
# • Level 2: 5-8 years experience
# Selvstendige konsulenter med lengre erfaring  over de siste 5-8 år som er relevant for det aktuelle området. Konsulenten har høyere utdanning, manglende utdanning kan kompenseres med lengre erfaring.
# • Level 3: 2 - <5 years experience
# Selvstendige konsulenter med minimum - over de siste 2 års erfaring som er relevant for det aktuelle området. Konsulenten har høyere utdannelse, anglende utdanning kan kompenseres med lengre erfaring
# • Level 4: < 2 years experience
# Konsulenter med under 2 års erfaring som er relevant for det aktuelle området. Konsulenten har høyere utdannelse, minimum mastergrad, manglende utdanning kan kompenseres med lengre erfaring. "


@pytest.mark.skip(reason="TDD")
def test_group_department_into_4_levels():
    assert False
