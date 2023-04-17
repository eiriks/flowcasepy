
import json
import pytest


from cvpartner.types.cv import CVResponse


# get department with cvs
department_with_cv = json.loads(
    open('tests/data/department_with_cvs.json').read())


def test_single_cv():
    _cv = department_with_cv[0][1]
    # print()
    cv = CVResponse(**_cv)
    # print(cv)

    assert type(cv.name) == str
    assert len(cv.name) > 0


def test_cv():
    # print(department_with_cv[0][1])
    cv = CVResponse(**department_with_cv[0][1])
    # print(cv)

    assert type(cv.name) == str
    assert len(cv.name) > 0


# @pytest.mark.skip(reason="not implemented")
def test_cvs():
    cvs = [CVResponse(**cv[1]) for cv in department_with_cv]

    assert type(cvs[len(cvs)-1].name) == str
    assert len(cvs[len(cvs)-1].name) > 0
    assert type(cvs[0]) == CVResponse
