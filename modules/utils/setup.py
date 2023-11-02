from modules import *

class Setup():
	def	__init__(self):
		self.setup_name = os.getenv("HELPER_SETUP_NAME")
		setup_json_path = os.path.join(HELPER_DIR, "modules/utils/setup.json")
		with open(setup_json_path, "r") as f:
			setup_json = f.read()
		self.config = json.loads(setup_json)

	def	launch(self):
		if not self.setup_name:
			log.print("HELPER_SETUP_NAME variable not found", p.FAILURE)
			return
		log.print(f"Executing setup ({a.YELLOW}{self.setup_name}{a.RST})", p.INFO, 1)
		if self.setup_name not in self.config:
			log.print(f"[{self.setup_name}] not implemented yet", p.FAILURE)
			return
		self.do_setup()
		log.print(f"Successfully executed setup ({a.GREEN}{self.setup_name}{a.RST})", p.SUCCESS)

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
				begin = time.time()
				module_func(data[module])
				end = time.time()
				print_elapsed(module, begin, end)

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

setup = Setup()
