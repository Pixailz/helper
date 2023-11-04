import os
import re
import sys
import enum
import glob
import json
import time
import inspect
import subprocess
import argparse

import norminette

from pprint import pprint

# METAVAR
__VERSION__ = "beta-0.0.0"
__NAME__ = "helper"
__AUTHOR__ = "Pixailz"

# DIR STUFF
__CWD__ = os.getcwd()
__PROJECT_DIR__ = __CWD__
__HELPER_DIR__ = os.path.join(__PROJECT_DIR__, "rsc/helper")

# CONFIG

## MAIN
"""
-1  all
0   disable
1.. debug level
"""
__DEBUG__ = 0
__MODULES__ = [
	"makefile",
	"prototype",
	"header",
]
## ANSI
__NO_ANSI__=False
## SETUP
__SETUP_DEFAULT_NAME__ = "_default_"

# UTILS
from modules.utils.ansi import a
from modules.utils.log import log, p
from modules.utils.regex import reg
from modules.utils.check import Is
from modules.utils.glob import get_file
from modules.utils.exec_time import Timer, TimerMode

# MAIN MODULES
from modules.parsing import Parsing
from modules.setup import Setup

from modules.prototype import Prototype
from modules.makefile import Makefile
from modules.header import Header
