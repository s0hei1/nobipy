from dataclasses import dataclass
from src.data.abstracts import DataclassMappings


@dataclass
class GetDepositsRequest(DataclassMappings):
    wallet : str = 'all'