from dataclasses import dataclass
from apps.nobipy.data.abstracts import DataclassMappings

@dataclass(frozen=True)
class GetStatsRequest(DataclassMappings):
    srcCurrency : list[str]
    dstCurrency : list[str]


    def to_dict(self):
        srcCurrency_str = ','.join(self.srcCurrency)
        dstCurrency_str = ','.join(self.dstCurrency)

        return {
            'srcCurrency' : srcCurrency_str,
            'dstCurrency' : dstCurrency_str,
        }

