from datetime import datetime
from typing import Any, Dict, List, Optional

from pydantic import BaseModel, Field, HttpUrl


class ImageUrl(BaseModel):
    url: Optional[HttpUrl] = None


class Image(BaseModel):
    url: Optional[HttpUrl] = None
    thumb: Optional[ImageUrl] = None
    fit_thumb: Optional[ImageUrl] = None
    large: Optional[ImageUrl] = None
    small_thumb: Optional[ImageUrl] = None


class Titles(BaseModel):
    int: Optional[str] = None
    no: Optional[str] = None
    se: Optional[str] = None
    pl: Optional[str] = None


class CVSearchResult(BaseModel):
    field_id: Optional[str] = Field(None, alias="_id")
    id: Optional[str] = None
    image: Optional[Image] = None
    title: Optional[str] = None
    titles: Optional[Titles] = None
    telephone: Optional[str] = None
    custom_tag_ids: List[Any] = []
    office_id: Optional[str] = None
    country_id: Optional[str] = None
    email: Optional[str] = None
    navn: Optional[str] = None
    name: Optional[str] = None
    name_multilang: Dict[str, Any] = {}
    is_external: bool = False
    is_deactivated: bool = False
    bruker_id: Optional[str] = None
    user_id: Optional[str] = None
    company_id: Optional[str] = None
    updated_at: Optional[datetime] = None
    updated_ago: Optional[str] = None
    owner_updated_at: Optional[datetime] = None
    default_word_template_id: Optional[str] = None
    default_word_json_template_id: Optional[str] = None
    default_ppt_template_id: Optional[str] = None
    default_indesign_template_id: Optional[str] = None
    country_code: Optional[str] = None
    language_code: Optional[str] = None
    language_codes: List[str] = []
    template_document_type: Optional[str] = None
    status: Optional[str] = None


class CVSearchResultWrapper(BaseModel):
    cv: CVSearchResult
    preview_url: Optional[str] = None
    highlights: Dict[str, Any] = {}

    def __len__(self) -> int:
        return len(self.cv)

    def __str__(self) -> str:
        return f"CVSearchResultWrapper({[n.name for n in self.cv]})"


class SearchResponseV4(BaseModel):
    cvs: List[CVSearchResultWrapper]
    total: int

    def __len__(self) -> int:
        """Return the number of users in the response."""
        return len(self.cvs)

    # def __iter__(self):
    #     return iter([n.cv for n in self.cvs])

    # @property
    # def names(self) -> List[str]:
    #     return [cv.cv.name for cv in self.cvs]  # Access nested name

    def __str__(self) -> str:
        """Return a string representation of the response."""
        return (
            f"SearchResponseV4(total={self.total}, "
            f"cvs_returned={len(self.cvs)} stk, {[n.cv.name for n in self.cvs]})"
        )

    # def __repr__(self) -> str:
    #     """Return an official string representation of the object."""
    #     return (f"SearchResponseV4(current_page={self.current_page}, "
    #             f"total_pages={self.total_pages}, total={self.total}, "
    #             f"user_data=[...])")
