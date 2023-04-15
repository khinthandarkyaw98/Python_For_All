import dog
dog.bark()

# instaed of calling the wholde file
# let's call only bark function from dog module
from dog import bark
bark()

from lib import dog2
dog2.bark()

from lib.dog2 import bark
bark()

import math
print(math.sqrt(4))

from math import sqrt
print(sqrt(4))

