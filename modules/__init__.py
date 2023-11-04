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

from pprint import pprint

CWD = os.getcwd()

"""
-1  all
0   disable
1.. debug level
"""
DEBUG = 0

MODULES = [
	"prototype",
	"makefile",
	"header",
]

# UTILS
	# LOG
from modules.utils.log import log, a, p
	# REGEX
from modules.utils.regex import reg
	# CHECK
from modules.utils.check import Is
	# GLOB
from modules.utils.glob import get_file
	# EXEC TIME
from modules.utils.exec_time import timer, TimerMode

# MAIN MODULES

	# PARSING
from modules.parsing import Parsing
	# SETUP
from modules.setup import Setup

from modules.prototype import Prototype
from modules.makefile import Makefile
from modules.header import Header

