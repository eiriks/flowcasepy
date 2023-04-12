
import os
import json
from cvpartner import CVPartner

DATA_BASE_PATH = 'tests/data'

cvp = CVPartner(org='noaignite', api_key=os.environ['CVPARTNER_API_KEY'])
department = cvp.get_department_by_name(office_name='Data Engineering')

# save department dict to file
with open(f'{DATA_BASE_PATH}/department.json', 'w') as f:
    json.dump(department, f, indent=4)


department_with_cvs = cvp.get_users_and_cvs_from_department(
    office_name='Data Engineering')

# save department and CVs dict to file
with open(f'{DATA_BASE_PATH}/department_with_cvs.json', 'w') as f:
    json.dump(department_with_cvs, f, indent=4)
