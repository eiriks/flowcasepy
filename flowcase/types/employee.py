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
    """The v4 version of the API"""

    field_id: Optional[str] = Field(None, alias="_id")
    id: Optional[str] = None
    image: Optional[Image] = None
    title: Optional[str] = None
    titles: Optional[Titles] = None
    telephone: Optional[str] = None
    email: Optional[str] = None
    navn: Optional[str] = None
    name: Optional[str] = None
    name_multilang: Optional[Dict[str, Any]] = None
    is_external: Optional[bool] = None
    is_deactivated: Optional[bool] = None
    bruker_id: Optional[str] = None
    user_id: Optional[str] = None
    company_id: Optional[str] = None
    updated_at: Optional[str] = None
    updated_ago: Optional[str] = None
    owner_updated_at: Optional[str] = None
    default_word_template_id: Optional[str] = None
    default_ppt_template_id: Optional[Any] = None
    country_code: Optional[str] = None
    language_code: Optional[str] = None
    language_codes: Optional[List[str]] = None
    template_document_type: Optional[str] = None

    def __str__(self) -> str:
        """Return a human-readable string representation of the Employee."""
        return f"{self.name} ({self.id})"

    def __repr__(self) -> str:
        """Return a detailed string representation for debugging."""
        return f"Employee(id='{self.id}', " f"name='{self.name}'"


class EmployeeMeta(BaseModel):
    cv: Employee
    preview_url: str
    highlight: str
    index: int
    id: int


class EmployeeSearchResult(BaseModel):
    cvs: List[EmployeeMeta]
    facets: Dict[str, Any]
    total: int
