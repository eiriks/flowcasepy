# file with functions to generate reports
from cvpartner.types.cv import CVResponse, Course, HonorsAward
from cvpartner.types.department import Department
from cvpartner.helpers import get_new_courses, get_new_honors_and_awards, get_new_presentations, sort_projects, get_new_certification
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
    print("new!")

    new_certifications = get_people_with_new_certifications(
        department=department, days_to_look_back=days_to_look_back)

    for name, certs in new_certifications.items():
        print(f'{name}, ({len(certs)}stk)')
        for cert in certs:
            print(f"\t- {cert.name.no}")


def get_people_with_new_courses(department: Department, days_to_look_back=365) -> dict[str, list[Course]]:
    print("Looking for new courses...")
    new_courses = {}
    for _, cv in department.__root__[:]:
        cv: CVResponse
        new_certs = get_new_courses(cv,
                                    days_to_look_back=days_to_look_back,
                                    language='no')
        if new_certs:
            new_courses[cv.navn] = new_certs

    print(f'{len(new_courses)} people with new courses found')
    return new_courses


def print_people_with_new_courses(department: Department,
                                  days_to_look_back=365) -> None:
    new_courses = get_people_with_new_courses(
        department=department, days_to_look_back=days_to_look_back)

    for name, courses in new_courses.items():
        print(f'{name}, ({len(courses)}stk)')
        for course in courses:
            print(f"\t- {course.name.no}")


def get_people_with_new_certifications(department: Department,
                                       days_to_look_back=365):
    # print("Looking for new certifications...")

    new_certifications = {}
    for _, cv in department.__root__[:]:
        cv: CVResponse
        new_certs = get_new_certification(cv,
                                          days_to_look_back=days_to_look_back)
        if new_certs:
            new_certifications[cv.navn] = new_certs

    print(f'{len(new_certifications)} people with new certifications found')
    return new_certifications


def print_people_who_might_have_forgotten_to_put_current_work_on_cv(
    department: Department,
    months_to_look_back: int = 3
) -> None:
    from cvpartner.helpers import newest_project_is_older_than_n_months
    print("Looking for people who might have forgotten to put current work on CV...")
    for persone, cv in department.__root__[:]:
        if newest_project_is_older_than_n_months(cv, months_to_look_back):
            print(cv.navn)


# get_people_with_new_presentation, print_people_with_new_presentations


def get_people_with_new_presentations(department: Department,
                                      days_to_look_back=365):
    print("Looking for new presentations...")
    new_presentations = {}
    for _, cv in department.__root__[:]:
        cv: CVResponse
        presentations = get_new_presentations(cv,
                                              days_to_look_back)
        if presentations:
            new_presentations[cv.navn] = get_new_presentations(cv,
                                                               days_to_look_back)

    print(f'{len(new_presentations)} people with new presentations found')
    return new_presentations


def print_people_with_new_presentations(department: Department,
                                        days_to_look_back=365) -> None:
    new_presentations = get_people_with_new_presentations(
        department=department, days_to_look_back=days_to_look_back)

    for name, presentations in new_presentations.items():
        if len(presentations) > 0:
            print(f'{name}, ({len(presentations)}stk)')
            for presentation in presentations:
                print(f"\t- {presentation.description.no}")


# get_people_with_new_honors_and_awards, print_people_with_new_honors_and_awards

def get_people_with_new_honors_and_awards(department: Department,
                                          days_to_look_back=365) -> dict[str, list[HonorsAward]]:
    print("Looking for new honors and awards...")
    new_honors_and_awards = {}
    for _, cv in department.__root__[:]:
        cv: CVResponse
        honors_awareds = get_new_honors_and_awards(cv,
                                                   days_to_look_back)
        if honors_awareds:
            new_honors_and_awards[cv.navn] = honors_awareds

    print(f'{len(new_honors_and_awards)} people with new honors and awards found')
    return new_honors_and_awards


def print_people_with_new_honors_and_awards(department: Department,
                                            days_to_look_back=365) -> None:
    new_honors_and_awards = get_people_with_new_honors_and_awards(
        department=department, days_to_look_back=days_to_look_back)

    for name, honors_and_awards in new_honors_and_awards.items():
        if len(honors_and_awards) > 0:
            print(f'{name}, ({len(honors_and_awards)}stk)')
            for honor in honors_and_awards:
                print(f"\t- {honor.name.no}")
