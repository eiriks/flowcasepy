from typing import List, Optional, Tuple

from pydantic import BaseModel

from flowcase.types.cv import CVResponse
from flowcase.types.employee import Employee


# class Department(RootModel):
class Department(BaseModel):
    """Department is a list of tuples of employees & CVResponses"""

    name: Optional[str] = None
    root: List[Tuple[Employee, CVResponse]] = []

    def __len__(self):
        return self.root.__len__()

    def __getitem__(self, item):
        return self.root[item]

    def __iter__(self):
        return iter(self.root)
