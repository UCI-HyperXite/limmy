'''
This module is the main entry point for the limmy library. It provides the
following functions:

    * VESC: A class that represents a VESC motor controller. This class
        provides methods for controlling the motor, as well as reading
        data from the motor controller.

    For examples on how to use, see examples in the examples directory.

Written by Adrian Ornelas, with help from Lea Pang and Saketh Karumuri
'''

import sys
if sys.version_info < (3, 3):
    raise SystemExit("Invalid Python version. limmy requires Python 3.3 or greater.")

from limmy.protocol import *
from limmy.VESC import *
