from modules import *

class Setup():
	@staticmethod
	def ft_libft():
		src_dir = "src"
		inc_dir = "inc"

		# Makefile
		config = {
			"makefile":		"mk/srcs.mk",
			"src_dir":		src_dir,
		}
		makefile = Makefile(**config)
		makefile.add_var("SRC_INT", "integer")
		makefile.add_var("SRC_STR", "string")
		makefile.add_var("SRC_MEM", "memory")
		makefile.add_var("SRC_PAR", "parsing")
		makefile.add_var("SRC_ERR", "error")
		makefile.add_var("SRC_CHK", "check")
		makefile.add_var("SRC_LST", "list")
		makefile.add_var("SRC_PRT", "print")
		makefile.add_var("SRC_INP", "input")
		makefile.add_var("SRC_RDM", "random")
		makefile.add_var("SRC_LNX", "linux")
		makefile.add_var("SRC_NET_IPV4", "network/ipv4")
		makefile.add_var("SRC_UNI_TEST", "unit_test")
		makefile.update_makefile()

		# Prototype
		config = {
			"inc_dir":	inc_dir,
			"src_dir":	src_dir,
		}
		prototype = Prototype(**config)
		prototype.add_header("libft_integer.h", "integer")
		prototype.add_header("libft_string.h", "string")
		prototype.add_header("libft_memory.h", "memory")
		prototype.add_header("libft_parsing.h", "parsing")
		prototype.add_header("libft_error.h", "error")
		prototype.add_header("libft_check.h", "check")
		prototype.add_header("libft_list.h", "list")
		prototype.add_header("libft_print.h", "print")
		prototype.add_header("libft_input.h", "input")
		prototype.add_header("libft_random.h", "random")
		prototype.add_header("libft_linux.h", "linux")
		prototype.add_header("libft_network/ipv4.h", "network/ipv4")
		prototype.add_header("libft_unit_test.h", "unit_test")
		prototype.update_include()

		# Header
		header = Header(**config)

	@staticmethod
	def	ft_ping():
		# Mandatory
		inc_dir = "inc"
		src_dir = "src/mandatory"
		#  Makefile
		config = {
			"makefile":		"mk/srcs.mk",
			"src_dir":		src_dir
		}
		makefile = Makefile(**config)
		makefile.add_var("SRC_C_MANDATORY")
		makefile.update_makefile()

		#  Prototype
		config = {
			"inc_dir":	inc_dir,
			"src_dir":	src_dir
		}
		prototype = Prototype(**config)
		prototype.add_header("ft_ping.h")
		prototype.update_include()

		#  Header
		header = Header(**config)

	@staticmethod
	def	SupaBlank():
		# Mandatory
		inc_dir = "inc"
		src_dir = "src/mandatory"
		#  Makefile
		config = {
			"makefile":		"mk/srcs.mk",
			"src_dir":		src_dir
		}
		makefile = Makefile(**config)
		makefile.add_var("SRC_C_MANDATORY")
		makefile.update_makefile()

		#  Prototype
		config = {
			"inc_dir":	inc_dir,
			"src_dir":	src_dir
		}

		prototype = Prototype(**config)
		prototype.add_header("template.h")
		prototype.update_include()

		#  Header
		header = Header(**config)

		# Bonus
		src_dir = "src/bonus"
		#  Makefile
		config = {
			"makefile":		"mk/srcs.mk",
			"src_dir":		src_dir
		}
		makefile = Makefile(**config)
		makefile.add_var("SRC_C_BONUS")
		makefile.update_makefile()

		#  Prototype
		config = {
			"inc_dir":	inc_dir,
			"src_dir":	src_dir
		}
		prototype = Prototype(**config)
		prototype.add_header("template_bonus.h")
		prototype.update_include()

		#  Header
		header = Header(**config)

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
