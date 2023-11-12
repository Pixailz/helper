from modules import *

class	Run():
	def	__init__(self):

		if parsing.args["setup_name"] not in setup.config:
			log.print(f"[{parsing.args['setup_name']}] "
					   "not implemented yet", p.FAILURE)
			return

		log.print("Executing helper profile "
				 f"({a.YEL}{parsing.args['setup_name']}{a.RST})", p.INFO, 1)

		timer = Timer()
		self.do_setup()
		timer.end()

		log.print("Successfully executed helper profile"
				 f", {a.GRE}{parsing.args['setup_name']}{a.RST}, in "
				 f"{a.GRE}{timer.elapsed()}{a.RST} ms", p.SUCCESS)

	def	do_setup(self) -> None:

		for part in setup.config[parsing.args["setup_name"]]["_profile_"]:
			log.print(f"{a.YEL}{parsing.args['setup_name']}{a.RST} Part "
					  f"{a.PUR}{part}{a.RST}")

			data = setup.config[parsing.args["setup_name"]]["_profile_"][part]
			self.current_config = data["_config_"]

			for module in data:
				if not Is.private(module):
					log.print(f"{a.YEL}{parsing.args['setup_name']}{a.RST} "
							  f"  Module {a.ITA}{a.GRE}{module}{a.RST}")

					match module:
						case "makefile": module_func = self.do_setup_makefile
						case "prototype": module_func = self.do_setup_prototype
						case "header": module_func = self.do_setup_header
					timer = Timer()
					module_func(data[module])
					timer.end()
					self.print_elapsed(module, timer)


	def	do_setup_makefile(self, data: any) -> None:
		makefile = Makefile(
			makefile	= self.current_config["makefile"],
			src_dir		= self.current_config["src_dir"],
		)

		for item in data:
			makefile.add_var(*item)

		makefile.update_makefile()

	def	do_setup_prototype(self, data: any) -> None:
		prototype = Prototype(
			inc_dir	= self.current_config["inc_dir"][0],
			src_dir	= self.current_config["src_dir"],
		)

		for item in data:
			prototype.add_header(*item)

		prototype.update_include()

	def	do_setup_header(self, data: any) -> None:
		header = Header(
			inc_dir	= self.current_config["inc_dir"],
			src_dir	= self.current_config["src_dir"],
		)

		header.get_unused_header()

	def	print_elapsed(self, title, timer):
		elapsed = timer.elapsed()
		warning = False
		if elapsed > .75 * 1_000_000:
			elapsed_str = a.RED
			warning = True
		elif elapsed > .25 * 1_000_000:
			elapsed_str = a.YEL
			warning = True
		else:
			elapsed_str = a.GRE

		elapsed_str += str(elapsed) + a.RST

		if warning:
			log.print(f"Module {a.ITA}{a.GRE}{title}{a.RST} "
				f"took {elapsed_str} ms", p.WARN)
		else:
			log.print(f"Module {a.ITA}{a.GRE}{title}{a.RST} "
				f"took {elapsed_str} ms", p.INFO)
