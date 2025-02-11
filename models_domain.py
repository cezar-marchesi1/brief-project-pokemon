from typing import List, Dict
from models_dto import PokemonDTO


class PokemonDomain:
    def __init__(self,
                 name: str,
                 base_experience: int,
                 height: int,
                 weight: int,
                 abilities: List[str] = None,
                 types: List[str] = None):
        self.name = name.strip() if name else ""
        self.base_experience = base_experience
        self.height = height
        self.weight = weight
        self.abilities = abilities if abilities is not None else []
        self.types = types if types is not None else []

    def add_ability(self, ability: str) -> None:
        if ability not in self.abilities:
            self.abilities.append(ability)

    def add_type(self, t: str) -> None:
        if t not in self.types:
            self.types.append(t)

    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "base_experience": self.base_experience,
            "height": self.height,
            "weight": self.weight,
            "abilities": self.abilities,
            "types": self.types,
        }

    @classmethod
    def from_dto(cls, dto: PokemonDTO) -> "PokemonDomain":
        abilities = [entry.ability.name for entry in dto.abilities]
        types = [entry.type.name for entry in dto.types]

        instance = cls(
            name=dto.name,
            base_experience=dto.base_experience if dto.base_experience is not None else 0,
            height=dto.height,
            weight=dto.weight,
            abilities=abilities,
            types=types,
        )
        return instance
