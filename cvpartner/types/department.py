
from typing import List

from pydantic import BaseModel, RootModel

from cvpartner.types.cv import CVResponse
from cvpartner.types.employee import Employee


# class Department(RootModel):
class Department(BaseModel):
    '''Department is a list of employees & CVs'''
    root: List[tuple[Employee, CVResponse]] = []
    def __len__(self):
        return self.root.__len__()
