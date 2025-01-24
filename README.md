## Flowcase scraper

This is a package for scraping the flowcase api

### Getting started

Install this fork of flowcasepy from this repo:
`pip install git+https://github.com/eiriks/flowcasepy.git`

#### Usage

The package has support for getting user metadata and CVs attached to users.
This can be used to scrape out all user CVs from the api:

```python
import os
from flowcase import Flowcase

# load_dotenv() <- grab key

cvp = Flowcase(org="myorg", api_key=os.environ["FLOWCASE_API_KEY"])

```

Search for single CV
```python

from IPython.display import HTML, display
from flowcase.types.search_result import SearchItem

# Find a CV to work on:
results = cvp.search_users(query="Rufus Scrimgeour")

print(f"{len(results)} users found")
table=[["name", "user_id", "cv_id"]]
for user in results:
    user: SearchItem
    #print(user.name, "\t\t\t\t|", user.user_id, "\t|", user.default_cv_id)
    table.append([user.name, user.user_id, user.default_cv_id])

display(HTML(
    "<table><tr>{}</tr></table>".format(
        "</tr><tr>".join(
            "<td>{}</td>".format("</td><td>".join(str(_) for _ in row)) for row in table)
    )
))
```

Retrieve a spesific CV.
```python
user_cv = cvp.get_user_cv(user_id="5a16db...b862",
                          cv_id="5a1...eb863")
```

Retrieve a full department:
```python
DEPARTMENT_NAME = "Department of Magical Accidents and Catastrophes"

department = cvp.get_emploees_and_cvs_from_department(DEPARTMENT_NAME)
```

## Documentation
pdoc was tested..

I find the github workflow (.github/workflows/docs.yaml)

```
 pdoc flowcase -o ./docs --logo "http..."
```
But where does the generated html gets deployed?

Oh.. here: https://eiriks.github.io/flowcasepy/...? cvpartner.html
