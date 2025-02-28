from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class TranslatedString(BaseModel):
    no: Optional[str] = None
    int: Optional[str] = None
    se: Optional[str] = None
    dk: Optional[str] = None
    fi: Optional[str] = None

    def __str__(self):
        # this surely is a problem if not using Norwegian
        # but heck, it's probably just me using this
        return self.no or self.int or self.se or self.dk or self.fi or "Unknown"

    def __repr__(self):
        return (
            f"TranslatedString(no={self.no!r}, int={self.int!r}, se={self.se!r}, "
            f"dk={self.dk!r}, fi={self.fi!r})"
        )


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
    field_id: Optional[str] = Field(None, alias="_id")
    diverged_from_master: bool = None
    external_unique_id: Any = None
    long_description: Optional[TranslatedString] = None
    month: Optional[str | int] = None
    month_expire: Optional[str | int] = None
    name: Optional[TranslatedString] = None
    organiser: Optional[TranslatedString] = None
    origin_id: Any = None
    year: Optional[str | int] = None
    year_expire: Any = None
    attachments: Optional[List] = None

    def __str__(self):
        name = self.name if self.name else "Unknown"
        organiser = self.organiser if self.organiser else "Unknown"
        year = self.year if self.year else "Unknown"
        month = self.month if self.month else "Unknown"
        return f"🏆 Certification: {name} by {organiser}, Date: {month}/{year}"


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
    diverged_from_master: Optional[bool] = None
    name: TranslatedString
    origin_id: Optional[Any] = None
    years_of_experience: Optional[int] = None
    years_of_experience_offset: Optional[int] = None
    project_experiences: Optional[List[ProjectExperience]] = []


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
    month: Optional[str] = None
    name: TranslatedString
    origin_id: Any
    year: Optional[str] = None


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
    field_id: Optional[str] = Field(..., alias="_id")
    id: Optional[str] = None
    blogs: List[Blog] = []
    born_day: Optional[int] = None
    born_month: Optional[int] = None
    born_year: Optional[int] = None  # ??
    bruker_id: str = None
    certifications: Optional[List[Certification]] = None
    courses: Optional[List[Course]] = None
    custom_tag_ids: Optional[List] = None
    cv_roles: Optional[List[CvRole]] = None
    default: Optional[bool] = None
    educations: Optional[List[Education]] = None
    honors_awards: Optional[List[HonorsAward]] = []
    imported_date: Optional[Any] = None
    key_qualifications: Optional[List[KeyQualification]] = None
    landline: Optional[Any] = None
    languages: Optional[List[Language]] = None
    level: Optional[Any] = None
    locked_at: Optional[Any] = None
    locked_until: Optional[Any] = None
    name_multilang: Optional[Dict[str, Any]] = None
    nationality: Optional[TranslatedString] = None
    navn: Optional[str] = None
    owner_updated_at_significant: Optional[str] = None
    place_of_residence: Optional[TranslatedString] = None
    positions: List[Position] = []
    presentations: List[Presentation] = []
    project_experiences: Optional[List[ProjectExperienceExpanded]] = None
    technologies: Optional[list[Technology]] = None
    telefon: Optional[str] = None
    tilbud_id: Optional[Any] = None
    title: Optional[TranslatedString] = None
    twitter: Optional[str] = None
    work_experiences: Optional[list[WorkExperience]] = None
    name: Optional[str] = None
    user_id: Optional[str] = None
    company_id: Optional[str] = None
    external_unique_id: Optional[Any] = None
    email: Optional[str] = None
    country_code: Optional[str] = None
    language_code: Optional[str] = None
    language_codes: Optional[List[str]] = None
    proposal: Optional[Any] = None
    custom_tags: Optional[List] = None
    updated_ago: Optional[str] = None
    template_document_type: Optional[str] = None
    default_word_template_id: Optional[str] = None
    default_ppt_template_id: Any = None
    highlighted_roles: Optional[List] = None
    image: Optional[Image] = None
    can_write: Optional[bool] = None
