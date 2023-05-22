
from typing import List

from pydantic import BaseModel

from cvpartner.types.cv import CVResponse
from cvpartner.types.employee import Employee


class Department(BaseModel):
    '''Department is a list of employees & CVs'''
    __root__: List[tuple[Employee, CVResponse]] = []
