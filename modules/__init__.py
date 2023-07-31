import os
import re
import enum
import inspect

CWD = os.getcwd()
"""
-1  all
0   disable
1.. debug level
"""
DEBUG = 0

from modules.utils.log import log
from modules.utils.log import a
from modules.utils.log import p
from modules.utils.regex import reg

from modules.prototype import Prototype
from modules.makefile import Makefile

from modules.utils.setup import setup
