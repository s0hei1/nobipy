from __future__ import annotations
from dataclasses import dataclass
from src.data.abstracts import DataclassMappings

@dataclass
class AddBankAccountRequest(DataclassMappings):
    number : str
    shaba: str
    bank: str
