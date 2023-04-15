# enum : creating a constant
# no one can change the value
#########################
from enum import Enum

class State(Enum):
    INACTIVE = 0
    ACTIVE = 1

print(State.ACTIVE.value)  # 1
print(State(1))  # State.ACTIVE
print(State["ACTIVE"]) # State.ACTIVE
print(State["ACTIVE"].value)  # 1
print(list(State)) # [<State.INACTIVE: 0>, <State.ACTIVE: 1>]
print(len(State)) # 2
