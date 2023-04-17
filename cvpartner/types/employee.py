
# Pydantic class of employee

from typing import Any, List, Dict, Optional
from datetime import datetime
from pydantic import BaseModel, Field


class URL(BaseModel):
    url: Optional[str]


class Image(BaseModel):
    url: Optional[str]
    thumb: URL
    fit_thumb: URL
    large: URL
    small_thumb: URL


class Employee(BaseModel):
    '''This class represents an employee in the CVPartner API. '''
    user_id: str
    field_id: str = Field(..., alias="_id")
    id: str
    company_id: str
    company_name: str
    company_subdomains: List[str]
    company_group_ids: List[str]
    email: str
    external_unique_id: Optional[str]
    upn: Optional[str]
    deactivated: bool
    deactivated_at: bool
    created_at: str
    updated_at: str
    role: str
    roles: List[str]
    role_allowed_office_ids: List
    role_allowed_tag_ids: List
    office_id: str
    office_name: str
    country_id: str
    country_code: str
    language_code: str
    language_codes: List[str]
    international_toggle: str
    preferred_download_format: str
    masterdata_languages: List[str]
    expand_proposals_toggle: bool
    selected_office_ids: List
    include_officeless_reference_projects: bool
    selected_tag_ids: List
    override_language_code: Any
    default_cv_template_id: str
    image: Image
    name: str
    telephone: str
    default_cv_id: str
