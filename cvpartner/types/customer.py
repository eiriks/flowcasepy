from __future__ import annotations

from typing import Any, Dict, List, Optional

from pydantic import BaseModel


class CustomerName(BaseModel):
    int: str
    fi: Optional[str] = None
    no: str
    se: str
    dk: Optional[str] = None


class CustomerDescription(BaseModel):
    no: Optional[str] = None
    int: Optional[str] = None


class CustomerDescriptionToCvs(BaseModel):
    no: Optional[str] = None
    int: Optional[str] = None


class Thumb(BaseModel):
    url: Optional[str]


class FitThumb(BaseModel):
    url: Optional[str]


class Large(BaseModel):
    url: Optional[str]


class SmallThumb(BaseModel):
    url: Optional[str]


class Image(BaseModel):
    url: Optional[str]
    thumb: Thumb
    fit_thumb: FitThumb
    large: Large
    small_thumb: SmallThumb


class Values(BaseModel):
    int: str
    no: str
    se: str


class IndustryItem(BaseModel):
    id: str
    values: Values
    external_unique_id: Any
    help_text: Dict[str, Any]
    company_id: str
    created_at: str
    updated_at: str
    _id: str


class Customer(BaseModel):
    id: str
    customer_name: CustomerName
    customer_description: CustomerDescription
    customer_description_to_cvs: CustomerDescriptionToCvs
    customer_url: Optional[str]
    external_unique_id: Any
    image_width: Optional[int]
    image_height: Optional[int]
    image: Image
    version: int
    company_id: str
    masterdata_industry_id: Optional[str]
    created_at: str
    updated_at: str
    _id: str
    custom_tags: List
    project_count: int
    industry: Optional[IndustryItem]


class Customers(BaseModel):
    def __len__(self):
        return len(self.customers)

    customers: List[Customer]
    total: int
