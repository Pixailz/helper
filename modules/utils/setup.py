from modules import *

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
		makefile.add_var("SRC_UNI_TEST", "unit_test")
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
		header.add_header("libft_unit_test.h", "unit_test")
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

	@staticmethod
	def	SupaBlank():
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
		header.add_header("template.h")
		header.update_include()

		src_dir = "src/bonus"
		config = {
			"makefile":		"mk/srcs.mk",
			"src_dir":		src_dir
		}
		makefile = Makefile(**config)
		makefile.add_var("SRC_C_BONUS")
		makefile.update_makefile()

		config = {
			"inc_dir":	"inc",
			"src_dir":	src_dir
		}
		header = Prototype(**config)
		header.add_header("template_bonus.h")
		header.update_include()

	def	__init__(self):
		self.setup_name = os.getenv("HELPER_SETUP_NAME")

	def	launch(self):
		log.print("Executing helper (setup)", p.INFO, 1)
		if not self.setup_name:
			log.print(f"HELPER_SETUP_NAME variable not found", p.FAILURE)
			return
		for item in dir(Setup):
			if item == self.setup_name:
				func = item
		if not func:
			log.print(f"[{self.setup_name}] not implemented yet", p.FAILURE)
			return
		getattr(Setup, func)()
		log.print(f"Successfully executed [{a.GREEN}{func}{a.RST}]", p.SUCCESS)

setup = Setup()
