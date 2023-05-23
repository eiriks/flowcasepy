# file with functions to generate reports
from cvpartner.types.cv import CVResponse
from cvpartner.types.department import Department
from cvpartner.helpers import sort_projects, get_new_certification
import logging

from cvpartner.types.employee import Employee
logger = logging.getLogger(__name__)


def print_users_with_older_unclosed_projects(
    department: Department
) -> list[tuple[Employee, dict]]:
    """Get all users with older unclosed projects

    Args:
        department (list[tuple(dict, dict)]): list of tuples with (cv, user)

    Returns:
        list[tuple[Employee, dict]]: list of tuples with (Employee, cv)
    """

    users_with_older_unclosed_projects = []
    for user, cv in department.__root__:
        user: Employee
        cv: CVResponse

        sorted_projects = sort_projects(cv)
        if sorted_projects:
            unclosed_projects: list = []
            # skip first project
            for project in sorted_projects[1:]:
                date_from, date_to, delta, project_details = project
                # skip projects that are closed
                if date_to:
                    continue

                unclosed_projects.append(
                    (date_from, date_to, delta, project_details)
                )
        if len(unclosed_projects) > 0:
            users_with_older_unclosed_projects.append(
                (user, unclosed_projects))

    # return users_with_older_unclosed_projects
    # dont return, print
    for user, projects in users_with_older_unclosed_projects:
        print(user.name)
        for date_from, date_to, delta, project_details in projects:
            print(
                f"from: {date_from.date()}, to: {date_to}, lasted {delta}mnd @ {project_details.customer.no} ")

        # print(len(projects))
        print()


#
def print_people_with_new_certifications(department: Department,
                                         days_to_look_back=365) -> None:

    print("Looking for new certifications...")
    new_certifications = []

    for person, cv in department.__root__[:]:
        new_certs = get_new_certification(cv,
                                          days_to_look_back=days_to_look_back)
        if new_certs:
            new_certifications.append(
                (cv.navn, new_certs)
            )
    print(len(new_certifications), "pople new certifications found")

    for name, certs in new_certifications:
        print(f'{name}, ({len(certs)}stk)')
        for cert in certs:
            print(f"\t- {cert.name.no}")


def print_people_who_might_have_forgotten_to_put_current_work_on_cv(
    department: Department,
    months_to_look_back: int = 3
) -> None:
    from cvpartner.helpers import newest_project_is_older_than_n_months
    print("Looking for people who might have forgotten to put current work on CV...")
    for persone, cv in department.__root__[:]:
        if newest_project_is_older_than_n_months(cv, months_to_look_back):
            print(cv.navn)
