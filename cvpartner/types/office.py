from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, Field


class Office(BaseModel):
    """Office is what we call department.
    'UX', 'CX', 'Frontend' and 'Platforms & services' are all offices."""
    office_id: str = Field(..., alias="_id")
    # _id: str
    name: str
    selected: bool
    default_word_template_id: Any
    default_ppt_template_id: Any
    cv_template_id: Optional[str] = None
    cv_template_type: Optional[str] = None
    country_id: str
    country_code: str
    override_language_code: Any
    num_users: int
