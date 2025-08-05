from dataclasses import dataclass

@dataclass
class Task:
    id : int
    name : str
    status : str = "Pending"


