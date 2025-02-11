from pydantic import BaseModel, HttpUrl
from typing import List, Optional


class NamedAPIResource(BaseModel):
    name: str
    url: HttpUrl


class AbilityEntry(BaseModel):
    ability: NamedAPIResource
    is_hidden: bool
    slot: int


class FormEntry(BaseModel):
    name: str
    url: HttpUrl


class Sprites(BaseModel):
    front_default: Optional[HttpUrl]
    back_default: Optional[HttpUrl]
    front_shiny: Optional[HttpUrl]
    back_shiny: Optional[HttpUrl]


class StatEntry(BaseModel):
    base_stat: int
    effort: int
    stat: NamedAPIResource


class TypeEntry(BaseModel):
    slot: int
    type: NamedAPIResource


class PokemonDTO(BaseModel):
    id: int
    name: str
    base_experience: Optional[int]
    height: int
    weight: int
    abilities: List[AbilityEntry]
    forms: List[FormEntry]
    sprites: Sprites
    stats: List[StatEntry]
    types: List[TypeEntry]
