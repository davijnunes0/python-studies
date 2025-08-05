from dataclasses import dataclass,field
from typing import Dict

@dataclass(frozen=True)
class Person:
    first_name : str
    last_name : str
    phone : Dict[str,str] = fiel[default_factory=dict]
    ddd: int = field[repr=False]
    fullname: str = field[init=False]

    def __post_init__(self):
        self.fullname = f"{self.first_name} {self.last_name}"
