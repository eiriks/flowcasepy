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
    month: Optional[str] = None
    name: TranslatedString
    origin_id: Any
    url: Optional[str]
    year: Optional[str] = None


class Certification(CVField):
    diverged_from_master: bool
    external_unique_id: Any
    long_description: TranslatedString
    month: Optional[str] = None
    month_expire: Any
    name: TranslatedString
    organiser: TranslatedString
    origin_id: Any
    year: Optional[str] = None
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
    year_from: Optional[str] = None
    year_to: Optional[str] = None
    years_of_experience: Optional[int] = None


class Presentation(CVField):
    description: TranslatedString
    diverged_from_master: bool
    external_unique_id: Any
    long_description: TranslatedString
    month: Optional[str] = None
    origin_id: Any
    year: Optional[str] = None


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
    project_experience_skills: Optional[List[ProjectExperienceSkill]] = []
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
    field_id: str = Field(..., alias="_id")
    base_duration_in_years: int
    offset_duration_in_years: int
    proficiency: int
    tags: TranslatedString
    total_duration_in_years: int


class Technology(CVField):
    field_id: str = Field(..., alias="_id")
    category: TranslatedString
    diverged_from_master: bool
    exclude_tags: Optional[List[Any]]
    external_unique_id: Any
    origin_id: Any
    technology_skills: Optional[List[TechnologySkill]] = None
    uncategorized: bool


class WorkExperience(CVField):
    field_id: str = Field(..., alias="_id")
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
    born_day: Optional[int]
    born_month: Optional[int]
    born_year: Optional[int] = None  # ??
    bruker_id: str
    certifications: Optional[List[Certification]] = None
    courses: Optional[List[Course]]
    custom_tag_ids: Optional[List]
    cv_roles: Optional[List[CvRole]]
    default: Optional[bool]
    educations: Optional[List[Education]] = None
    honors_awards: List[HonorsAward] = []
    imported_date: Any
    key_qualifications: Optional[List[KeyQualification]] = None
    landline: Any
    languages: Optional[List[Language]] = None
    level: Any
    locked_at: Any
    locked_until: Any
    name_multilang: Optional[Dict[str, Any]]
    nationality: Optional[TranslatedString]
    navn: str
    owner_updated_at_significant: Optional[str] = None
    place_of_residence: Optional[TranslatedString]
    positions: List[Position] = []
    presentations: List[Presentation] = []
    project_experiences: Optional[List[ProjectExperienceExpanded]] = None
    technologies: Optional[list[Technology]] = None
    telefon: Optional[str] = None
    tilbud_id: Any
    title: TranslatedString
    twitter: Optional[str] = None
    work_experiences: Optional[list[WorkExperience]] = None
    name: Optional[str]
    user_id: Optional[str]
    company_id: Optional[str]
    external_unique_id: Any
    email: Optional[str]
    country_code: Optional[str]
    language_code: Optional[str]
    language_codes: Optional[List[str]]
    proposal: Any
    custom_tags: Optional[List]
    updated_ago: Optional[str]
    template_document_type: Optional[str]
    default_word_template_id: Optional[str]
    default_ppt_template_id: Any
    highlighted_roles: Optional[List]
    image: Optional[Image]
    can_write: Optional[bool]
