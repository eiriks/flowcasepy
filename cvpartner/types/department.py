from typing import List, Tuple

from pydantic import BaseModel

from cvpartner.types.cv import CVResponse
from cvpartner.types.employee import Employee


# class Department(RootModel):
class Department(BaseModel):
    """Department is a list of tuples of employees & CVResponses"""

    root: List[Tuple[Employee, CVResponse]] = []

    def __len__(self):
        return self.root.__len__()

    def __getitem__(self, item):
        return self.root[item]

    def __iter__(self):
        return iter(self.root)