from dataclasses import dataclass,asdict
from apps.nobipy.data.abstracts import DataclassMappings


@dataclass
class GetMarketHistoryRequest(DataclassMappings):
    symbol : str
    resolution : str
    to : int
    page  : int
    from_ : int | None = None
    countback : int | None = None

    def to_dict(self):
        d = asdict(self)
        d['from'] = d.pop('from_')
        return d
