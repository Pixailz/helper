from modules import *

from modules import __AUTHOR__
from modules import __NAME__
from modules import __VERSION__
from modules import __MODULES__

_IMP = a.RED
_MOD = a.PUR

_SUB = a.GRE
_VER = a.YEL
_ADJ = a.BLU

_WIP = a.BOL + a.BLI + _IMP + "*" + a.RST

_F_META_DIR = f"{_ADJ}FOLDER{a.RST}"
_F_META_FILE = f"{_ADJ}FILE{a.RST}"
_F_META_LOG_FILE = f"{_ADJ}LOG_FILE{a.RST}"
_F_META_N = f"{_ADJ}N{a.RST}"
_F_META_STRING = f"{_ADJ}STRING{a.RST}"

class	Parsing():
	def	__init__(self):
		self.add_args_main()

	def	add_args_main(self):
		self.parser = argparse.ArgumentParser(
			prog=f"{_IMP}{__NAME__}{a.RST}",
			description=f"{_MOD}Modules{a.RST} to {_VER}help{a.RST} "
						f"you with {_SUB}C{a.RST} "
						f"{_ADJ}project{a.RST}",
			epilog=f"""
				marked line with {_WIP} is a Work In Progress, meaning is
				parsed but do nothing
				{_VER}Developed{a.RST} by {_IMP}Pixailz{a.RST}
				""",
		)

		self.parser.add_argument(
			"--version", "-V",
			action="version",
			version=f"%(prog)s, version {_SUB}{__VERSION__}{a.RST}"
		)

		self.parser.add_argument(
			"--src-dir", "-s",
			help=f"{_F_META_DIR} is the dir where helper will search for "
				 "C code file",
			metavar=_F_META_DIR,
			default="src",
			type=str,
		)

		self.parser.add_argument(
			"--inc-dir", "-I",
			help=f"{_F_META_DIR} is the dir where helper will search for include header",
			metavar=_F_META_DIR,
			default="inc",
			type=str,
		)

		self.parser.add_argument(
			"--makefile", "-M",
			help=f"{_F_META_FILE} to update src path",
			metavar=_F_META_FILE,
			default="Makefile",
			type=str,
		)

		self.parser.add_argument(
			"--setup-name", "-S",
			help=f"{_F_META_STRING} profile to search in setup.json",
			metavar=_F_META_STRING,
			default="_default_",
			type=str,
		)

		self.parser.add_argument(
			f"--log-file", "-L",
			help=f"{_F_META_LOG_FILE} to output log",
			metavar=_F_META_LOG_FILE,
			default=None,
			type=str,
		)

		self.parser.add_argument(
			f"--no-color",
			help=f"{_WIP}disable color",
			action="store_true"
		)

		for module in __MODULES__:
			getattr(self, "add_args_" + module)()

	def	add_args_prototype(self):
		self.g_prototype = self.parser.add_argument_group(
			f"{_MOD}Prototype{a.RST}",
			f"{_VER}Format{a.RST} {_SUB}prototype{a.RST} in {_ADJ}header{a.RST}"
		)

	def	add_args_makefile(self):
		self.g_makefile = self.parser.add_argument_group(
			f"{_MOD}Makefile{a.RST}",
			f"{_VER}Update{a.RST} {_SUB}src path{a.RST} in {_ADJ}Makefile{a.RST}"
		)

	def	add_args_header(self):
		self.g_header = self.parser.add_argument_group(
			f"{_MOD}Header{a.RST}",
			f"{_VER}Check{a.RST} for {_SUB}unused{a.RST} "
			f"{_ADJ}header{a.RST} in C file"
		)

		self.g_header.add_argument(
			f"--header-max-rec",
			help=f"{_WIP}Limit the recursion of the "
				 f"{_MOD}Header{a.RST} module by {_F_META_N}",
			metavar=_F_META_N,
			default=10,
			type=int,
		)

	def	parse_args(self):
		self.args = vars(self.parser.parse_args())
		log.set_log_file(self.args["log_file"])
		log.print(f"Successfully parsed sys.argv", p.SUCCESS)

parsing = Parsing()
