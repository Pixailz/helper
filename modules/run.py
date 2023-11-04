from modules import *

class	Run():
	def	__init__(self):
		if not self.setup_name:
			log.print("HELPER_SETUP_NAME variable not found", p.FAILURE)
			return

		if self.setup_name not in self.config:
			log.print(f"[{self.setup_name}] not implemented yet", p.FAILURE)
			return

		log.print(f"Executing setup ({a.YEL}{self.setup_name}{a.RST})", p.INFO, 1)

		self.do_setup()

		log.print(f"Successfully executed setup ({a.GRE}{self.setup_name}{a.RST})", p.SUCCESS)

	def	do_setup(self) -> None:
		for part in self.config[self.setup_name]:
			log.print(f"{self.setup_name} Part {part}")

			data = self.config[self.setup_name][part]
			self.current_config = data["part_config"]
			del data["part_config"]

			for module in data:
				log.print(f"{self.setup_name}   Module {module}")

				match module:
					case "makefile": module_func = self.do_setup_makefile
					case "prototype": module_func = self.do_setup_prototype
					case "header": module_func = self.do_setup_header
				timer = Timer()
				module_func(data[module])
				timer.end()
				self.print_elapsed(module)

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
			inc_dir	= self.current_config["inc_dir"],
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

	def	print_elapsed(self, title):
		elapsed = timer.elapsed()
		elapsed /= 1000
		warning = False
		if elapsed > .75 * 1_000_000:
			elapsed_str = a.RED
			warning = True
		elif elapsed > .25 * 1_000_000:
			elapsed_str = a.YEL
			warning = True
		else:
			elapsed_str = a.GRE

		elapsed_str += str(round(elapsed, 3)) + a.RST

		if warning:
			log.print(f"Module {a.YEL}{title}{a.RST} "
				f"took {elapsed_str} ms", p.WARN)
		else:
			log.print(f"Module {a.YEL}{title}{a.RST} "
				f"took {elapsed_str} ms", p.INFO)
