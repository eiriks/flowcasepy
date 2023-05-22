

from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field


class Thumb(BaseModel):
    url: Optional[str] = None


class FitThumb(BaseModel):
    url: Optional[str] = None


class Large(BaseModel):
    url: Optional[str] = None


class SmallThumb(BaseModel):
    url: Optional[str] = None


class Image(BaseModel):
    url: Optional[str]
    thumb: Thumb
    fit_thumb: FitThumb
    large: Large
    small_thumb: SmallThumb


class Titles(BaseModel):
    no: Optional[str] = None
    int: Optional[str] = None
    se: Optional[str] = None


class Employee(BaseModel):
    '''The v4 version of the API'''
    image: Image
    title: Optional[str] = None
    titles: Titles
    telephone: Optional[str] = None
    email: Optional[str] = None
    navn: Optional[str] = None
    name: Optional[str] = None
    name_multilang: Dict[str, Any]
    is_external: bool
    is_deactivated: bool
    bruker_id: str
    user_id: str
    company_id: str
    field_id: str = Field(..., alias="_id")
    id: str
    updated_at: str
    updated_ago: str
    owner_updated_at: Optional[str] = None
    default_word_template_id: str
    default_ppt_template_id: Any
    country_code: str
    language_code: str
    language_codes: List[str]
    template_document_type: str


class EmployeeMeta(BaseModel):
    cv: Employee
    preview_url: str
    highlight: str
    index: int
    id: int


class SearchResult(BaseModel):
    cvs: List[EmployeeMeta]
    facets: Dict[str, Any]
    total: int
