import json
import os

from dotenv import load_dotenv

from flowcase import Flowcase
from flowcase.types.department import Department

load_dotenv()

DATA_BASE_PATH = "tests/data"

cvp = Flowcase(org="noaignite", api_key=os.environ["FLOWCASE_API_KEY"])
department = cvp.get_emploees_by_department(office_name="Data Engineering")

# save department dict to file
with open(f"{DATA_BASE_PATH}/department.json", "w") as f:
    json.dump([p.dict(by_alias=True) for p in department], f, indent=4)


department_with_cvs: Department = cvp.get_emploees_and_cvs_from_department(
    office_name="Data Engineering"
)

# save department and CVs dict to file
with open(f"{DATA_BASE_PATH}/department_with_cvs.json", "w") as f:
    json.dump(
        [
            (p.model_dump(by_alias=True), cv.model_dump(by_alias=True))
            for p, cv in department_with_cvs
        ],
        f,
        indent=4,
    )

# Save a single CV as an example
cv = department_with_cvs[0][1]
with open(f"{DATA_BASE_PATH}/example_cv.json", "w") as f:
    json.dump(cv.dict(by_alias=True), f, indent=4)
