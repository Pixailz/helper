from modules import *

from pprint import pprint

class Setup():
	@staticmethod
	def ft_libft():
		src_dir = "src"
		config = {
			"makefile":		"mk/srcs.mk",
			"src_dir":		src_dir
		}
		makefile = Makefile(**config)
		makefile.add_var("SRC_INT", "integer")
		makefile.add_var("SRC_STR", "string")
		makefile.add_var("SRC_MEM", "memory")
		makefile.add_var("SRC_CHK", "check")
		makefile.add_var("SRC_LST", "list")
		makefile.add_var("SRC_PRT", "print")
		makefile.add_var("SRC_INP", "input")
		makefile.add_var("SRC_RDM", "random")
		makefile.add_var("SRC_LNX", "linux")
		makefile.add_var("SRC_NET_IPV4", "network/ipv4")
		makefile.add_var("SRC_ERR", "error")
		makefile.add_var("SRC_C_MANDATORY")
		makefile.update_makefile()

		config = {
			"inc_dir":	"inc",
			"src_dir":	src_dir
		}
		header = Prototype(**config)
		header.add_header("libft_integer.h", "integer")
		header.add_header("libft_string.h", "string")
		header.add_header("libft_memory.h", "memory")
		header.add_header("libft_check.h", "check")
		header.add_header("libft_list.h", "list")
		header.add_header("libft_print.h", "print")
		header.add_header("libft_input.h", "input")
		header.add_header("libft_random.h", "random")
		header.add_header("libft_linux.h", "linux")
		header.add_header("libft_network/ipv4.h", "network/ipv4")
		header.add_header("libft_error.h", "error")
		header.add_header("ft_ping.h")
		header.update_include()

	@staticmethod
	def	ft_ping():
		src_dir = "src/mandatory"
		config = {
			"makefile":		"mk/srcs.mk",
			"src_dir":		src_dir
		}
		makefile = Makefile(**config)
		makefile.add_var("SRC_C_MANDATORY")
		makefile.update_makefile()

		config = {
			"inc_dir":	"inc",
			"src_dir":	src_dir
		}
		header = Prototype(**config)
		header.add_header("ft_ping.h")
		header.update_include()

	def	__init__(self):
		self.git_config = os.path.join(os.path.join(CWD, '.git'), "config")

	def	launch(self):
		if not os.path.isfile(self.git_config):
			log.print(f"{self.git_config} not found", p.FAILURE)
			return
		with open(self.git_config, 'r') as f:
			git_config_str = f.read()
		founded = reg.get_git_name.findall(git_config_str)
		if not len(founded):
			log.print(f"repo name not found in {self.git_config}", p.FAILURE)
			return
		func = None
		for item in dir(Setup):
			if item == founded[0]:
				func = item
		if not func:
			log.print(f"{founded[0]} not implemented yet", p.FAILURE)
			return
		getattr(Setup, func)()
		log.print(f"successfully executed {func}", p.SUCCESS)

setup = Setup()
