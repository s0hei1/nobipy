from __future__ import annotations
from dataclasses import dataclass
from apps.nobipy.data.abstracts import DataclassMappings

@dataclass
class AddBankCardRequest(DataclassMappings):
    number : str
    bank: str

    def __post_init__(self):
        if not (16 <= len(self.number) <= 20):
            raise ValueError(f'{self.number} is not a valid bank number')
