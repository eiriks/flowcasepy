from __future__ import annotations

from typing import Any, List, Optional

from pydantic import BaseModel, RootModel


class Office(BaseModel):
    _id: str
    id: str
    name: str
    selected: bool
    default_word_template_id: Any
    default_ppt_template_id: Any
    country_id: str
    country_code: str
    override_language_code: Any
    num_users: int
    num_users_activated: int
    num_users_deactivated: int


class Setting(BaseModel):
    _id: str


class Country(BaseModel):
    _id: str
    id: str
    code: str
    native_language_code: str
    override_ui_language_code: Optional[str]
    selected: bool
    default_ppt_template_id: Any
    default_word_template_id: Any
    offices: List[Office]
    setting: Setting


# class Model(BaseModel):
#     __root__: List[ModelItem]


class Countries(RootModel):
    '''Root model for countries'''
    root: List[Country]

    def __iter__(self):
        return iter(self.root)

    def __getitem__(self, item):
        return self.root[item]
