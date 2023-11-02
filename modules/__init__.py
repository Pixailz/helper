import os
import re
import sys
import enum
import glob
import json
import time
import inspect
import subprocess

CWD = os.getcwd()
HELPER_DIR = os.path.join(CWD, "rsc/helper")
"""
-1  all
0   disable
1.. debug level
"""
DEBUG = 0

# UTILS
from pprint import pprint
	# LOG
from modules.utils.log import log
from modules.utils.log import a
from modules.utils.log import p
	# REGEX
from modules.utils.regex import reg
	# GLOB
from modules.utils.glob import get_file
	# EXEC TIME
from modules.utils.exec_time import print_elapsed

# MAIN MODULES
from modules.prototype import Prototype
from modules.makefile import Makefile
from modules.header import Header

# SETUP
from modules.utils.setup import setup
