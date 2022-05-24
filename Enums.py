from enum import Enum

#OT Object-Type
Pi=3.1415926
class OT(Enum):
    Body=0
    Spring=1
    Planet=2
    Rope=3
    Wall=4

#CT Camera-Type
class CT(Enum):
    Stationary=0
    ConstentSpeed=1
    Attached=2
    MovesWith=3
    FreeFalling=4

#Pr precision
class Pr(Enum):
    Low=0
    Med=1
    High=2
    SuperHigh=3