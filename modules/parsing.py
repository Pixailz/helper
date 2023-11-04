from modules import *

class	Parsing():
	def	__init__(self):
		self.add_args_main()
		self.get_args()

	def	add_args_main(self):
		self.parser = argparse.ArgumentParser(
			prog="helper",
			description="help you with C project",
			epilog="Developed by Pixailz",
		)

		self.parser.add_argument(
			"--src-dir", "-s",
			help="C src dir to search in",
			default="src",
			metavar="FOLDER",
		)

		self.parser.add_argument(
			"--inc-dir", "-I",
			help="Header dir to work on",
			default="inc",
			metavar="FOLDER",
		)

		self.parser.add_argument(
			"--makefile", "-M",
			help="Makefile to work on",
			default="Makefile",
			metavar="FILE",
		)

		for module in MODULES:
			getattr(self, "add_args_" + module)()

	def	add_args_prototype(self):
		self.g_prototype = self.parser.add_argument_group(
			"Prototype", "Format prototype in header"
		)

	def	add_args_makefile(self):
		self.g_makefile = self.parser.add_argument_group(
			"Makefile", "Update src in Makefile"
		)

	def	add_args_header(self):
		self.g_header = self.parser.add_argument_group(
			"Header", "Check for unused header in C file"
		)

		self.g_header.add_argument(
			"--header-max-rec",
			help="Limit the recursion of the Header module",
			metavar="FOLDER",
		)

	def	get_args(self):
		self.args = vars(self.parser.parse_args())
