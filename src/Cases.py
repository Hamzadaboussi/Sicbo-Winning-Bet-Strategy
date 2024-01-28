from enum import Enum


class Cases(Enum):
    ODD_AND_BIG = "Odd and Big"
    EVEN_AND_SMALL = "Even and Small"
    ODD_AND_SMALL = "Odd and Small"
    EVEN_AND_BIG = "Even and Big"
    TIE = "Tie"


class Types(Enum):
    SMALL = "S"
    BIG = "B"
    TIE = "T"
class Result(Enum):
    WIN = "win"
    LOST = "lost"

