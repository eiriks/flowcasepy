from cvpartner.types.department import Department
import os
import json
from cvpartner import CVPartner

DATA_BASE_PATH = "tests/data"

cvp = CVPartner(org="noaignite", api_key=os.environ["CVPARTNER_API_KEY"])
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
            (p.dict(by_alias=True), cv.dict(by_alias=True))
            for p, cv in department_with_cvs.__root__
        ],
        f,
        indent=4,
    )

# Save a single CV as an example
cv = department_with_cvs.__root__[0][1]
with open(f"{DATA_BASE_PATH}/example_cv.json", "w") as f:
    json.dump(cv.dict(by_alias=True), f, indent=4)
