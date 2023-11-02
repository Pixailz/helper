import os
import re
import sys
import enum
import glob
import inspect
import subprocess

import norminette

CWD = os.getcwd()
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
	# Norminette

# MAIN MODULES
from modules.prototype import Prototype
from modules.makefile import Makefile
from modules.header import Header

from modules.norminette import check_norminette

# SETUP
from modules.utils.setup import setup
