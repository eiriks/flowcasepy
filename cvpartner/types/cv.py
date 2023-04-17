from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class TranslatedString(BaseModel):
    no: Optional[str] = None
    int: Optional[str] = None
    se: Optional[str] = None
    dk: Optional[str] = None
    fi: Optional[str] = None


class CVField(BaseModel):
    field_id: str = Field(..., alias="_id")
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    owner_updated_at: Optional[str] = None
    order: Optional[int] = None
    recently_added: Optional[bool] = None
    starred: Optional[bool] = None
    starred_order: Optional[int] = None
    version: Optional[int] = None
    modifier_id: Optional[Any] = None
    disabled: Optional[bool] = None


class Blog(CVField):
    diverged_from_master: bool
    external_unique_id: Any
    long_description: TranslatedString
    month: str
    name: TranslatedString
    origin_id: Any
    url: Optional[str]
    year: str


class Certification(CVField):
    diverged_from_master: bool
    external_unique_id: Any
    long_description: TranslatedString
    month: Optional[str] = None
    month_expire: Any
    name: TranslatedString
    organiser: TranslatedString
    origin_id: Any
    year: str
    year_expire: Any
    attachments: List


class Course(CVField):
    diverged_from_master: bool
    external_unique_id: Any
    long_description: TranslatedString
    month: Optional[str] = None
    name: TranslatedString
    origin_id: Any
    program: TranslatedString
    year: Optional[str] = None
    attachments: List


class ProjectExperience(CVField):
    field_id: str = Field(..., alias="_id")
    roles: List[CVField]
    diverged_from_master: bool


class CvRole(CVField):
    diverged_from_master: bool
    name: TranslatedString
    origin_id: Any
    years_of_experience: int
    years_of_experience_offset: int
    project_experiences: List[ProjectExperience]


class Education(CVField):
    degree: TranslatedString
    description: TranslatedString
    diverged_from_master: bool
    external_unique_id: Any
    month_from: Optional[str] = None
    month_to: Optional[str] = None
    origin_id: Any
    school: TranslatedString
    year_from: Optional[str] = None
    year_to: Optional[str] = None
    attachments: List


class HonorsAward(CVField):
    diverged_from_master: bool
    external_unique_id: Any
    for_work: TranslatedString
    issuer: TranslatedString
    long_description: TranslatedString
    month: str
    name: TranslatedString
    origin_id: Any
    year: str


class KeyQualification(CVField):
    diverged_from_master: bool
    external_unique_id: Any
    label: Dict[str, Any]
    long_description: TranslatedString
    origin_id: Any
    tag_line: Dict[str, Any]


class Language(CVField):
    diverged_from_master: bool
    external_unique_id: Any
    level: TranslatedString
    name: TranslatedString
    origin_id: Any


class Position(CVField):
    description: TranslatedString
    diverged_from_master: bool
    external_unique_id: Any
    name: TranslatedString
    origin_id: Any
    roles: list[CVField] = []
    year_from: str
    year_to: str
    years_of_experience: Optional[int] = None


class Presentation(CVField):
    description: TranslatedString
    diverged_from_master: bool
    external_unique_id: Any
    long_description: TranslatedString
    month: str
    origin_id: Any
    year: str


class ProjectExperienceSkill(CVField):
    base_duration_in_years: int
    offset_duration_in_years: int
    proficiency: int
    tags: TranslatedString
    total_duration_in_years: int


class Role(CVField):
    cv_role_id: Optional[str] = None
    diverged_from_master: bool
    long_description: TranslatedString
    name: Optional[TranslatedString] = None
    origin_id: Any
    summary: Dict[str, Any] = {}


class ProjectExperienceExpanded(ProjectExperience):
    area_amt: Any
    area_unit: Any
    customer: TranslatedString
    customer_anonymized: Dict[str, Any]
    customer_description: Dict[str, Any]
    customer_selected: str
    customer_value_proposition: Dict[str, Any]
    description: TranslatedString
    exclude_tags: Optional[List[Any]]
    expected_roll_off_date: Any
    extent_hours: Optional[str]
    external_unique_id: Any
    industry: TranslatedString
    location_country_code: Any
    long_description: TranslatedString
    month_from: Optional[str] = None
    month_to: Optional[str] = None
    origin_id: Any
    percent_allocated: Optional[str]
    project_experience_skills: List[ProjectExperienceSkill] = []
    project_extent_amt: Optional[str]
    project_extent_currency: Optional[str]
    project_extent_hours: Optional[str]
    project_type: TranslatedString
    related_work_experience_id: Any
    roles: List[Role]
    total_extent_amt: Optional[str]
    total_extent_currency: Optional[str]
    total_extent_hours: Optional[str]
    year_from: Optional[str] = None
    year_to: Optional[str] = None
    images: List


class TechnologySkill(CVField):
    base_duration_in_years: int
    offset_duration_in_years: int
    proficiency: int
    tags: TranslatedString
    total_duration_in_years: int


class Technology(CVField):
    category: TranslatedString
    diverged_from_master: bool
    exclude_tags: Optional[List[Any]]
    external_unique_id: Any
    origin_id: Any
    technology_skills: List[TechnologySkill] = None
    uncategorized: bool


class WorkExperience(CVField):
    description: TranslatedString
    diverged_from_master: bool
    employer: TranslatedString
    external_unique_id: Any
    long_description: TranslatedString
    month_from: Optional[str] = None
    month_to: Optional[str] = None
    origin_id: Any
    year_from: Optional[str] = None
    year_to: Optional[str] = None


class URL(BaseModel):
    url: Optional[str] = None


class Image(BaseModel):
    url: Optional[str] = None
    thumb: URL
    fit_thumb: URL
    large: URL
    small_thumb: URL


class CVResponse(CVField):
    blogs: List[Blog] = []
    born_day: int
    born_month: int
    born_year: int
    bruker_id: str
    certifications: List[Certification] = None
    courses: List[Course]
    custom_tag_ids: List
    cv_roles: List[CvRole]
    default: bool
    educations: List[Education] = None
    honors_awards: List[HonorsAward] = []
    imported_date: Any
    key_qualifications: List[KeyQualification] = None
    landline: Any
    languages: List[Language] = None
    level: Any
    locked_at: Any
    locked_until: Any
    name_multilang: Dict[str, Any]
    nationality: TranslatedString
    navn: str
    owner_updated_at_significant: Optional[str] = None
    place_of_residence: TranslatedString
    positions: List[Position] = []
    presentations: List[Presentation] = []
    project_experiences: List[ProjectExperienceExpanded] = None
    technologies: List[Technology] = None
    telefon: Optional[str] = None
    tilbud_id: Any
    title: TranslatedString
    twitter: Optional[str] = None
    work_experiences: List[WorkExperience] = None
    name: str
    user_id: str
    company_id: str
    external_unique_id: Any
    email: str
    country_code: str
    language_code: str
    language_codes: List[str]
    proposal: Any
    custom_tags: List
    updated_ago: str
    template_document_type: str
    default_word_template_id: str
    default_ppt_template_id: Any
    highlighted_roles: List
    image: Image
    can_write: bool


# class UserListResponse(BaseModel):
#     __root__: List[CVResponse]


# from dataclasses import dataclass, field
# from typing import Optional


# @dataclass
# class Cv:
#     _id: str
#     born_month: int
#     born_year: int
#     bruker_id: str
#     certifications: list
#     courses: list
#     created_at: str
#     custom_tag_ids: list
#     cv_roles: list
#     default: bool
#     educations: list
#     imported_date: str
#     key_qualifications: list
#     landline: str
#     languages: list
#     level: str
#     locked_at: str
#     locked_until: str
#     modifier_id: str
#     name_multilang: dict
#     nationality: dict
#     navn: str
#     order: str
#     owner_updated_at: str
#     owner_updated_at_significant: str
#     place_of_residence: dict
#     positions: list
#     project_experiences: list
#     technologies: list
#     updated_at: str
#     version: int
#     work_experiences: list
#     name: str
#     user_id: str
#     company_id: str
#     external_unique_id: str
#     email: str
#     country_code: str
#     language_code: str
#     language_codes: list
#     proposal: str
#     custom_tags: list
#     updated_ago: str
#     template_document_type: str
#     default_word_template_id: str
#     default_ppt_template_id: str
#     highlighted_roles: list
#     image: dict
#     can_write: bool
#     positions: list = field(default_factory=list)
#     blogs: list = field(default_factory=list)
#     honors_awards: list = field(default_factory=list)
#     presentations: list = field(default_factory=list)
#     project_experiences: list = field(default_factory=list)
#     technologies: list = field(default_factory=list)
#     twitter: Optional[str]
#     title: Optional[dict]
#     tilbud_id: Optional[str]
#     born_day: Optional[int]
#     telefon: Optional[str]
#     locked_at: Optional[bool]
#     locked_until: Optional[str]
