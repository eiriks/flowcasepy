# generated by datamodel-codegen:
#   filename:  search_result.json
#   timestamp: 2024-05-21T15:39:52+00:00

from __future__ import annotations

from typing import List, Optional

from pydantic import BaseModel, Field
from pydantic import RootModel


class Title(BaseModel):
    no: Optional[str] = None
    int: Optional[str] = None
    se: Optional[str] = None
    dk: Optional[str] = None
    fi: Optional[str] = None


class Thumb(BaseModel):
    url: str


class FitThumb(BaseModel):
    url: str


class Large(BaseModel):
    url: str


class SmallThumb(BaseModel):
    url: str


class Image(BaseModel):
    url: str
    thumb: Thumb
    fit_thumb: FitThumb
    large: Large
    small_thumb: SmallThumb


class SearchItem(BaseModel):
    user_id: str
    field_id: str = Field(..., alias='_id')
    id: str
    company_id: str
    company_name: str
    company_subdomains: List[str]
    company_group_ids: List[str]
    email: str
    external_unique_id: Optional[str] = None
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
    title: Title
    international_toggle: Optional[str] = None
    preferred_download_format: Optional[str] = None
    masterdata_languages: List[str]
    expand_proposals_toggle: bool
    selected_office_ids: List[str]
    include_officeless_reference_projects: bool
    selected_tag_ids: List
    override_language_code:  Optional[str] = None
    default_cv_template_id: Optional[str] = None
    image: Image
    name: str
    telephone: Optional[str] = None
    default_cv_id: str


class SearchResults(RootModel):
    root: List[SearchItem]
    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]

    def __len__(self):
        return len(self.root)