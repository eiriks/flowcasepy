#!/usr/bin/env python
# -*- coding: utf-8 -*-

import datetime
import logging
import re
from datetime import date
from typing import Optional

from cvpartner.types.cv import (
    Certification,
    Course,
    CVResponse,
    Education,
    HonorsAward,
    Position,
    Presentation,
    ProjectExperienceExpanded,
    WorkExperience,
)
from cvpartner.types.department import Department
from cvpartner.types.employee import Employee

# set up logging to std out
logger = logging.getLogger(__name__)


# grab date parts from project
# put together a proper python date
def create_dates_from_project(
    project: ProjectExperienceExpanded,
) -> tuple[datetime.datetime, datetime.datetime | None, int]:
    """Function to make a best guess at the start and end dates of a project."""
    month_from = int(project.month_from) if project.month_from else 1
    month_to = int(project.month_to) if project.month_to else 1
    year_from = int(project.year_from) if project.year_from else 1
    year_to = int(project.year_to) if project.year_to else 1

    date_from = datetime.datetime(year=year_from, month=month_from, day=1)
    date_to = datetime.datetime(year=year_to, month=month_to, day=1)
    # compute time delta in months between from and to
    delta_months = (date_to.year - date_from.year) * 12 + (
        date_to.month - date_from.month
    )

    if date_to == datetime.datetime(year=1, month=1, day=1):
        # if no end date, assume it's still ongoing
        date_to = None
        delta_months = (datetime.datetime.now().year - date_from.year) * 12 + (
            datetime.datetime.now().month - date_from.month
        )

    return date_from, date_to, delta_months


def sort_projects(
    cv: CVResponse, return_newest_first: bool = True
) -> list[tuple[datetime.datetime, datetime.datetime | None, int, dict]]:
    """Sort projects by date, newest first or oldest first."""
    projects_to_sort = []

    # gard against empty cv
    if cv.project_experiences is None:
        return projects_to_sort

    for project in cv.project_experiences:
        date_from, date_to, delta_monts = create_dates_from_project(project)

        projects_to_sort.append((date_from, date_to, delta_monts, project))

    sorted_projects = sorted(
        projects_to_sort, key=lambda x: x[0], reverse=return_newest_first
    )
    return sorted_projects


def get_days_since_last_finished_project(project: tuple) -> int:
    _, date_to, _, _ = project
    if date_to is None:
        # current gig is not ended
        return 0
    else:
        return (datetime.datetime.now() - date_to).days


# Dersom feltet «fra-til» har et «til-dato» > 3mnd gammel
def newest_project_is_older_than_n_months(cv: CVResponse, n_months: int = 3):
    projects = sort_projects(cv)
    if not projects:
        # no project experiences found
        return False

    _, date_to, _, _ = projects[0]
    if date_to is None:
        # current gig is not ended
        return False
    else:
        days_in_n_months = n_months * 30
        return get_days_since_last_finished_project(projects[0]) > days_in_n_months


def get_new_projects(
    cv: CVResponse, days_to_look_back: int = 365, language: str = "no"
) -> list[ProjectExperienceExpanded]:
    # what I want here is to get any ProjectExperienceExpanded that has was
    # - ended last year
    # - started last year
    # - that is new-ish, but still not ended, assmuing an ongoing project

    new_projects: list[ProjectExperienceExpanded] = []

    # guard against empty cv
    if cv.project_experiences is None:
        return new_projects

    for project in cv.project_experiences:
        # started last year
        if not project.year_from:
            logger.warning(
                f"{cv.navn} har et prosjekt uten start-årstall: {getattr(project.customer, language)}"
            )
            continue  # skip project without a start year

        project_start_date = get_proper_project_dates(
            year=project.year_from, month=project.month_from
        )

        now = datetime.datetime.now().astimezone()
        delta_in_days_since_start = (now - project_start_date).days

        if delta_in_days_since_start < days_to_look_back:
            new_projects.append(project)

        # ended last year
        if project.year_to:
            project_end_date = get_proper_project_dates(
                year=project.year_to,
                month=int(project.month_to) if project.month_to else 12,
                day=1,
            )
            delta_in_days_since_end = (now - project_end_date).days
            if (
                delta_in_days_since_end < days_to_look_back
                and project not in new_projects
            ):
                new_projects.append(project)

        # is ongoing
        # start date should be less than 4 years from now AND have no end_year
        # Consultant A has been 7 years with customer Y..  Need to accept longer projects
        YEARS_BACK_TO_CHECK = 8
        if (
            delta_in_days_since_start < YEARS_BACK_TO_CHECK * 365
            and not project.year_to
            and project not in new_projects
        ):
            # print(f'{cv.name} Ongoing project: {project.customer.no}')
            new_projects.append(project)
    # sort new projects descending
    new_projects.sort(key=lambda x: x.year_from, reverse=True)

    return new_projects


def get_new_courses(
    cv: CVResponse, days_to_look_back: int = 365, language: str = "no"
) -> list[Course]:
    new_courses: list[Course] = []

    # gard against empty cv
    if cv.courses is None:
        return new_courses

    for course in cv.courses:
        if not course.year:
            logger.warning(
                f"{cv.navn} har et kurs uten årstall: {getattr(course.name, language)}"
            )
            continue  # skip course without a year

        course_date = get_proper_project_dates(year=course.year, month=course.month)

        now = datetime.datetime.now().astimezone()

        delta_in_days = (now - course_date).days

        if delta_in_days < days_to_look_back:
            new_courses.append(course)

    return new_courses


def get_number_of_new_courses_by_department(
    department: Department, days_to_look_back: int = 365
) -> int:
    new_courses = 0
    for _, cv in department.root:
        new_courses += len(get_new_courses(cv, days_to_look_back))
    return new_courses


def get_new_certification(
    cv: CVResponse, days_to_look_back: int = 365, language: str = "no"
) -> list[Certification]:
    new_certifications: list[Certification] = []

    # gaerd against empty cv
    if cv.certifications is None:
        return new_certifications

    for cert in cv.certifications:
        if not cert.year:
            logger.warning(
                f"{cv.navn} har en sertifisering uten årstall: {getattr(cert.name, language)}"
            )
            continue  # skip certification without a year

        cert_date = get_proper_project_dates(year=cert.year, month=cert.month)

        now = datetime.datetime.now().astimezone()
        delta_in_days = (now - cert_date).days

        if delta_in_days < days_to_look_back:
            # print(f'\t --> New last {days_to_look_back} days')
            new_certifications.append(cert)

    return new_certifications


def get_number_of_new_sertifications_from_department(
    department: Department, days_to_look_back: int = 365
) -> int:
    certifications = []
    for _, cv in department.root:
        new_certs = None
        new_certs = get_new_certification(cv, days_to_look_back=days_to_look_back)
        if new_certs:
            # print(cv.name)
            certifications.extend(new_certs)
    return len(certifications)


def get_new_positions(
    cv: CVResponse, days_to_look_back: int = 365, language: str = "no"
) -> list[Position]:
    new_positions: list[Position] = []
    for position in cv.positions:
        if not position.year_from:
            logger.warning(
                f"{cv.navn} har en stilling uten start-årstall: {getattr(position.name, language)}"
            )
            continue  # skip position without a start year

        position_date = get_proper_project_dates(year=position.year_from, month=1)

        now = datetime.datetime.now().astimezone()
        delta_in_days = (now - position_date).days

        if delta_in_days < days_to_look_back:
            new_positions.append(position)
        # possistion that are not ednded
        if position.year_to is None or position.year_to in [" ", "", "0"]:
            new_positions.append(position)

    return new_positions


def get_new_honors_and_awards(
    cv: CVResponse, days_to_look_back: int = 365, language: str = "no"
) -> list[HonorsAward]:
    new_honors_and_awards: list[HonorsAward] = []

    # gard against empty cv
    if cv.honors_awards is None:
        return new_honors_and_awards

    for honor in cv.honors_awards:
        if not honor.year:
            logger.warning(
                f"{cv.navn} har en award uten årstall: {getattr(honor.name, language)}"
            )
            continue  # skip honor without a year

        honor_date = get_proper_project_dates(year=honor.year, month=honor.month)

        now = datetime.datetime.now().astimezone()
        delta_in_days = (now - honor_date).days

        if delta_in_days < days_to_look_back:
            new_honors_and_awards.append(honor)

    return new_honors_and_awards


def get_new_presentations(
    cv: CVResponse, days_to_look_back: int = 365, language: str = "no"
) -> list[Presentation]:
    """
    Retrieves a list of new presentations from the given CV response.

    Args:
        cv (CVResponse): The CV response object containing the presentations.
        days_to_look_back (int, optional): The number of days to look back for new presentations. Defaults to 365.
        language (str, optional): The language to use for logging warnings. Defaults to 'no'.

    Returns:
        list[Presentation]: A list of new presentations.

    """
    new_presentations: list[Presentation] = []
    for presentation in cv.presentations:
        if not presentation.year:
            logger.warning(
                f"{cv.navn} har en pressentasjon uten årstall: {getattr(presentation.description, language)}"
            )
            continue  # skip presentation without a year

        presentation_date = get_proper_project_dates(
            year=presentation.year, month=presentation.month
        )

        now = datetime.datetime.now().astimezone()
        delta_in_days = (now - presentation_date).days

        if delta_in_days < days_to_look_back:
            new_presentations.append(presentation)

    return new_presentations


def get_new_work_experiences(
    cv: CVResponse, days_to_look_back: int = 365, language: str = "no"
) -> list[WorkExperience]:
    """Not very relevant as work experience is emplyers.
    We mostly care about work done in current posistion.
    """
    new_work_experiences: list[WorkExperience] = []

    # gard against empty cv
    if cv.work_experiences is None:
        return new_work_experiences

    for job in cv.work_experiences:
        if not job.year_from:
            logger.warning(
                f"{cv.navn} har en jobb uten start-årstall: {getattr(job.employer, language)}"
            )
            continue  # skip work without a start year

        work_date = get_proper_project_dates(year=job.year_from, month=job.month_from)
        now = datetime.datetime.now().astimezone()
        delta_in_days = (now - work_date).days

        if delta_in_days < days_to_look_back:
            new_work_experiences.append(job)

    return new_work_experiences


def get_proper_project_dates(year: str | int, month: Optional[str | int], day: int = 1):
    month = int(month) if month else 1
    year = int(year)
    return datetime.datetime(year=year, month=month, day=day).astimezone()


def get_new_project_experiences(
    cv: CVResponse, days_to_look_back: int = 365, language: str = "no"
) -> list[ProjectExperienceExpanded]:
    new_project_experiences: list[ProjectExperienceExpanded] = []

    # gard against empty cv
    if cv.project_experiences is None:
        return new_project_experiences

    for project in cv.project_experiences:
        if not project.year_from:
            logger.warning(
                f"{cv.navn} har et prosjekt uten start-årstall: {getattr(project.customer, language)}"
            )
            continue

        # find start date
        project_start_date = get_proper_project_dates(
            year=project.year_from, month=project.month_from
        )

        now = datetime.datetime.now().astimezone()
        delta_in_days_since_start = (now - project_start_date).days

        # find end date
        if project.year_to:
            project_end_date = get_proper_project_dates(
                year=project.year_to, month=project.month_to
            )
        else:
            # set end date to now, if no end date
            project_end_date = datetime.datetime.now().astimezone()

        delta_in_days_since_end = (now - project_end_date).days

        # project is started less than a year ago, or is closed less than a year ago
        if (delta_in_days_since_start < days_to_look_back) or (
            delta_in_days_since_end < days_to_look_back
        ):
            new_project_experiences.append(project)

    return new_project_experiences


def get_old_project_experiences(
    cv: CVResponse, older_than_days: int = 365, language: str = "no"
) -> list[ProjectExperienceExpanded]:
    old_project_experiences: list[ProjectExperienceExpanded] = []

    # gard against empty cv
    if cv.project_experiences is None:
        return old_project_experiences

    for project in cv.project_experiences:
        if not project.year_from:
            logger.warning(
                f"{cv.navn} har et prosjekt uten start-årstall: {getattr(project.customer, language)}"
            )
            continue

        # find start date
        # project_start_date = get_proper_project_dates(year=project.year_from, month=project.month_from)

        now = datetime.datetime.now().astimezone()
        # delta_in_days_since_start = (now - project_start_date).days

        # find end date
        if project.year_to:
            project_end_date = get_proper_project_dates(
                year=project.year_to, month=project.month_to
            )
        else:
            # set end date to now, if no end date
            project_end_date = datetime.datetime.now().astimezone()

        delta_in_days_since_end = (now - project_end_date).days
        # more than a year old since ended
        if delta_in_days_since_end > older_than_days:
            old_project_experiences.append(project)

        # # then look at start dates
        # if (delta_in_days_since_start > older_than_days) or \
        #     (delta_in_days_since_end > older_than_days):
        #     old_project_experiences.append(project)

    return old_project_experiences


def get_new_educations(cv, days_to_look_back=365):
    new_educations: list[Education] = []
    for education in cv.educations:
        if education.year_to is None:
            # un-finnished edu bussiness?
            continue  # skip

        if education.year_to > datetime.datetime.now() - datetime.timedelta(
            days=days_to_look_back
        ):
            new_educations.append(education)
    return new_educations


def get_degree_candidates(degree: Optional[str]) -> str:
    """Function to return a standard name for a degree, from a user input string."""

    phd_spellings = ["phd", "ph.d.", "doktor", "doctor"]
    master_spellings = [
        "master",
        "m.a.",
        "m.s.",
        "siviløkonom",
        "sivilingeniør",
        "cand scient",
        "cand.scient.",
        "cand.mag.",
        "cand-mag",
        "m. sc",
        "m.sc.",
    ]
    bachelor_spellings = [
        "b.a.",
        "bs",
        "ba",
        "bachelor",
        "b.sc.",
        "b.sc",
        "ingeniør",
        "3 year it education",
    ]

    if not degree:
        return "no degree"
    degree = degree.lower()
    if any(deg in degree for deg in phd_spellings):
        return "phd"
    if any(deg in degree for deg in master_spellings):
        return "master"
    if any(deg in degree for deg in bachelor_spellings):
        return "bachelor"
    return "unknown"


# 'Høyskolekandidat i programmering'
# that is two years. not a BA/BS
# fallback to unknown


def get_highest_degree(cv: CVResponse) -> str:
    # sample candidate degrees: phd, master, bachelor
    canditate_top_degrees = []
    if cv.educations:
        for edu in cv.educations:
            if not edu.year_to or not edu.year_to.strip().isnumeric():
                # skip unfinnished education
                continue

            canditate_top_degrees.append(get_degree_candidates(edu.degree.no))

    # resolve
    if "phd" in canditate_top_degrees:
        return "phd"
    if "master" in canditate_top_degrees:
        return "master"
    if "bachelor" in canditate_top_degrees:
        return "bachelor"
    # fallback for no hits
    return "unknown"


def get_email(person: Employee, convert_to_lowercase: bool = True) -> Optional[str]:
    if person.email is None:
        return None
    return person.email.lower() if convert_to_lowercase else person.email


def get_graduation_year(cv) -> Optional[int]:
    """Get the finnal year of the last compleated education

    Args:
        cv (dict): CVpartner cv object

    Returns:
        Optional[int]: the year as int (eg 2008) or None
    """
    if cv.educations:
        # print(cv.educations)
        graduation_years = [
            int(n.year_to)
            for n in cv.educations
            if n is not None and str(n.year_to).isnumeric()
        ]
        if len(graduation_years) > 0:
            return int(max(graduation_years))


def get_age(cv: CVResponse) -> Optional[int]:
    if cv.born_year:
        return date.today().year - cv.born_year


def add_space_around_slash(string: str) -> str:
    return string.replace("/", " / ")


def clean_name(name: str) -> str:
    # guard
    if not name:
        return name
    name = remove_ending_period(name)
    name = remove_extra_whitespace(name)
    return name


def remove_extra_whitespace(string: str) -> str:
    return " ".join(string.split())


def remove_ending_period(string: str) -> str:
    string = string.strip()
    if string.endswith("."):
        string = string.replace(".", "")
    return string


def convert_developer_to_utvikler(string: str) -> str:
    """substitute developer with utvikler, disregard case"""
    return re.sub("developer", "utvikler", string, flags=re.IGNORECASE)


def convert_enginer_to_engineer(string: str) -> str:
    return re.sub("enginer", "engineer", string, flags=re.IGNORECASE)


def rename_common_variations_in_dev(string) -> str:
    if string == "Back End Developer":
        return "Backend Utvikler"
    if string == "Back End Utvikler":
        return "Backend Utvikler"
    return string


def get_role_from_cv_roles(cv_role: dict, lang: str = "no") -> str | None:
    tmp_role_string = cv_role.get("name", {}).get(lang)
    if not tmp_role_string:
        return None

    if tmp_role_string:
        tmp_role_string = tmp_role_string.replace("-", " ")
        tmp_role_string = remove_ending_period(tmp_role_string)
        tmp_role_string = rename_common_variations_in_dev(tmp_role_string)
        tmp_role_string = convert_enginer_to_engineer(tmp_role_string)
        tmp_role_string = convert_developer_to_utvikler(tmp_role_string)
        tmp_role_string = add_space_around_slash(tmp_role_string)
        tmp_role_string = remove_extra_whitespace(tmp_role_string)
        tmp_role_string = tmp_role_string.title().strip()

    return tmp_role_string


def get_tags_from_cv(cv: dict, lang: str = "no") -> list[str]:
    tags = []
    for technology in cv.get("technologies"):
        # these come in groups
        if technology.get("technology_skills"):
            for group in technology.get("technology_skills"):
                if group.get("tags").get(lang):
                    tags.append(group.get("tags").get(lang))
            # print(json.dumps(group.get('tags').get(lang), indent=2))
    return tags


def get_keywords_from_projects(projects: list[ProjectExperienceExpanded]) -> list[str]:
    words = []
    for project in projects:
        project: ProjectExperienceExpanded
        for skills in project.project_experience_skills:
            if skills.tags.no:
                words.append(skills.tags.no)
    return words


def get_avg_new_keywords_pr_department(
    department: Department, days_to_look_back: int = 365
) -> float:
    new_skills_counter = 0
    for _, cv in department.root:
        new_projects: list[ProjectExperienceExpanded] = get_new_project_experiences(
            cv, days_to_look_back
        )
        new_skills = get_keywords_from_projects(new_projects)

        old_projects: list[ProjectExperienceExpanded] = get_old_project_experiences(
            cv, days_to_look_back
        )
        old_skills = get_keywords_from_projects(old_projects)

        # find all word in new list that is not in old list
        ture_new_skills = [skill for skill in new_skills if skill not in old_skills]
        new_skills_counter += len(ture_new_skills)
    return new_skills_counter / len(department.root)
