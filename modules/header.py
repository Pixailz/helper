from modules import *

from modules import __CWD__

BLACK_LISTED_WORD = [
	"include",
	"return",
	"while",
	"for",
	"of",
	"if",
	"else",
	"const",
	"unsigned",
	"char",
	"short",
	"int",
	"long",
	"float",
	"double",
	"void",
]

class	Header():
	def	__init__(self,
			inc_dir: list[str],
			src_dir: str,
			excluded_files: list[str]	= [],
			max_recursion: int			= 10,
			remove_unused: bool			= False,
		):
		self.inc_dir: list[str] = inc_dir
		self.src_dir: str = os.path.join(__CWD__, src_dir)
		self.c_files: dict[any] = {}
		self.h_files: dict[any] = {}

		self.lib_dir = []
		self.get_lib_dir()

		self.max_recursion = max_recursion
		self.recursion_lvl: list[str] = []

		self.reset_stats()
		self.populate_files(excluded_files)

		self.remove_unused = remove_unused

	def	get_lib_compiler(self, compiler: str) -> None:
		io = reg.c_compiler_inc.findall(
			subprocess.run(
				[f"echo | {compiler} -xc -E -v -"],
				shell=True,
				capture_output=True,
			).stderr.decode("utf-8")
		)

		if len(io):
			for item in io[0].split('\n'):
				if len(item):
					self.lib_dir.append(item.removeprefix(" "))

	def	get_lib_dir(self) -> None:
		self.get_lib_compiler("gcc")
		self.get_lib_compiler("clang")

		for inc_dir in self.inc_dir:
			self.lib_dir.append(os.path.join(__CWD__, inc_dir))

		self.lib_dir = sorted(set(self.lib_dir), reverse=True)

	def	reset_stats(self):
		self.stats_prefix = "nb_symbols_"
		self.nb_symbols_function = 0
		self.nb_symbols_define = 0
		self.nb_symbols_typedef = 0
		self.nb_symbols_enum = 0
		self.nb_symbols_c_files = 0
		self.nb_symbols_h_files = 0

	def	get_path(self, key) -> str:
		to_check = [
			self.src_dir,
			*self.lib_dir,
		]

		for lib_dir in to_check:
			path = os.path.join(lib_dir, key)
			if os.path.isfile(path):
				return (path)
		return (None)

	def	get_key(self, path) -> str:
		to_check = [
			self.src_dir,
			*self.lib_dir,
		]

		for lib_dir in to_check:
			id_lib_dir = lib_dir + '/'
			if path[:len(id_lib_dir)] == id_lib_dir:
				return path.removeprefix(id_lib_dir)
		return (path)

	def	update_data(
			self,
			src: str,
			value: any,
			primary_key: str,
			secondary_key: str = None,
		) -> None:
		value_type = type(value)

		if not value:
			value = []
			value_type = list
		if value_type == dict:
			pass
		elif value_type == list:
			value = sorted(set(value))

		src_attr = getattr(self, src)

		if secondary_key:
			try:
				tmp_type = type(src_attr[primary_key][secondary_key])
				if tmp_type != value_type:
					log.print(f"{tmp_type} don't match {value_type}", p.DEBUG)
				elif tmp_type == dict:
					src_attr[primary_key][secondary_key].update(value)
				elif tmp_type == list:
					src_attr[primary_key][secondary_key].extend(value)
			except KeyError:
				try:
					src_attr[primary_key].update({
						secondary_key: value,
					})
				except KeyError:
					src_attr.update({
						primary_key: {
							secondary_key: value,
						}
					})
		else:
			try:
				tmp_type = type(src_attr[primary_key])
				if tmp_type == dict:
					src_attr[primary_key].update(value)
				elif tmp_type == list:
					src_attr[primary_key].extend(value)
			except KeyError:
				src_attr.update({
					primary_key: value,
				})

	def	populate_files(self, excluded_files: list[str] = []) -> None:
		files = get_file(f"{self.src_dir}/**/*.c", excluded_files)
		self.nb_symbols_c_files += len(files)
		for file in files:
			self.populate_files_c(file)

		files = get_file(f"{self.inc_dir[0]}/**/*.h", excluded_files)
		self.nb_symbols_h_files += len(files)
		for file in files:
			self.populate_h_files(os.path.basename(file))

		self.print_stats_symbols("Successfully parsed:")

		self.update_headers()
		self.clean_headers()

	def	populate_files_c(self, c_file: str) -> None:
		with open(c_file, "r") as f:
			c_file_str = f.read()

		c_file_header = {}
		for header in reg.c_header.findall(c_file_str):
			c_file_header.update({
				self.get_path(header): []
			})
			self.populate_h_files(header)

		c_key = self.get_path(c_file)
		self.update_data("c_files", c_file_header, c_key)

	def	populate_h_files(self, h_file: str) -> None:
		if Is.private_header(h_file): return

		header_path = self.get_path(h_file)
		if not header_path: return
		with open(header_path, "r") as f:
			h_file_str = f.read()

		h_file_header = reg.c_header.findall(h_file_str)
		h_file_symbols = self.get_header_symbols(h_file_str)

		# update data
		self.update_data("h_files", h_file_header, header_path, "header")
		self.update_data("h_files", h_file_symbols, header_path, "symbols")
		# recursive part
		for header in h_file_header:
			path_header = self.get_path(header)
			if path_header and path_header not in self.h_files:
				self.populate_h_files(path_header)

	def	get_header_symbols(self, header_str: str) -> list:
		content: dict = {}

		data = reg.proto.findall(header_str)
		if (data): content.update({"function": data})

		data = reg.c_typedef.findall(header_str)
		if (data): content.update({"define": data})

		data = reg.c_define.findall(header_str)
		if (data): content.update({"typedef": data})

		data = reg.c_enum_values.findall(header_str)
		enum_names = reg.c_enum_name.findall(header_str)

		enum = {}
		for enums, enum_name in zip(data, enum_names):
			enum_values = [
				reg.c_enum_value.findall(enum_value)[0]
				for enum_value
				in enums.split(",")
			]
			enum.update({enum_name: enum_values})

		if len(enum): content["enum"] = enum

		parsed_content: list[str] = []
		for key in content.keys():
			changed = 0
			if key == "enum":
				for sym in content[key]:
					if not Is.private(sym):
						parsed_content.append(sym)
						parsed_content.extend(content[key][sym])
						changed += len(content[key][sym]) + 1
			else:
				for sym in content[key]:
					if not Is.private(sym):
						parsed_content.append(sym)
						changed += 1
			tmp_name = self.stats_prefix + key
			tmp = getattr(self, tmp_name)
			setattr(self, tmp_name, tmp + changed)
		return (parsed_content)

	def	print_stats_symbols(self, title: str):
		log.print(title, p.SUCCESS)
		tmp_ansi = f"{a.ITA}{a.YEL}"
		log.print(f"  function: {tmp_ansi}{self.nb_symbols_function}{a.RST}", p.INFO)
		log.print(f"  define:   {tmp_ansi}{self.nb_symbols_define}{a.RST}", p.INFO)
		log.print(f"  typedef:  {tmp_ansi}{self.nb_symbols_typedef}{a.RST}", p.INFO)
		log.print(f"  enum:     {tmp_ansi}{self.nb_symbols_enum}{a.RST}", p.INFO)
		log.print(f"in", p.SUCCESS)
		log.print(f"  c file:   {tmp_ansi}{self.nb_symbols_c_files}{a.RST}", p.INFO)
		log.print(f"  h file:   {tmp_ansi}{self.nb_symbols_h_files}{a.RST}", p.INFO)

	def	update_headers(self) -> None:
		for h_tree_key in self.h_files.keys():
			self.current_content = {}
			self.follow_content = {}
			self.recursion_lvl = []
			self.update_header_leaf(h_tree_key)

	def	update_header_leaf(self, header_name: str) -> any:
		"""
		Depth First Search algorithm (DFS)
		Merge foreign key according to headers in data struct,
		then recursivly merge symbols of each layer of header
		"""
		if Is.private_header(header_name): return {}

		try:
			self.recursion_lvl.index(header_name)
			return {}
		except ValueError:
			pass


		header_path = self.get_path(header_name)
		if not header_path: return {}

		if len(self.recursion_lvl) > self.max_recursion:
			log.print(
				f"exceeded recursion of {self.max_recursion}, aborting", p.WARN)
			return {}
		self.recursion_lvl.append(header_name)
		# self.print_recursion_lvl()

		current_content: dict = {}

		if "symbols" in self.h_files[header_path]:
			current_content[header_path] = \
				self.h_files[header_path]["symbols"]
		else:
			current_content[header_path] = []

		if "header" in self.h_files[header_path]:
			for header in self.h_files[header_path]["header"]:
				tmp_key = self.get_path(header)
				if not tmp_key:
					tmp_key = header
				tmp_content = self.update_header_leaf(tmp_key)
				current_content.update(tmp_content)
			del self.h_files[header_path]["header"]

		tmp_list = []
		for key in current_content.keys():
			tmp_list.extend(current_content[key])
		if len(tmp_list):
			self.h_files[header_path]["symbols"] = set(tmp_list)
		self.recursion_lvl.remove(header_name)
		return current_content

	def	clean_headers(self) -> None:
		for key in self.h_files:
			self.h_files[key] = [
				s for s in sorted(self.h_files[key]["symbols"])
			]

	def	print_data(self, include: list[str] = []):
		if not len(include):
			for file in self.c_files:
				log.print(f" C {file}", p.DEBUG, 1)
				for value in self.c_files[file]:
					log.print(" C   " + value, p.DEBUG, 2)
			for file in self.h_files:
				log.print(f" H {file}", p.DEBUG, 1)
				for key in self.h_files[file].keys():
					log.print(f" H   - {key}:", p.DEBUG, 2)
					for value in self.h_files[file][key]:
						log.print(" H     - " + value, p.DEBUG, 3)
		else:
			for file in include:
				tmp_key_c = self.get_path(file)
				tmp_key_header = self.get_path(file)

				if tmp_key_c in self.c_files.keys():
					log.print(f" C {file}", p.DEBUG, 1)
					for value in self.c_files[file]:
						log.print(" C   " + value, p.DEBUG, 2)
				elif tmp_key_header in self.h_files:
					log.print(f" H {tmp_key_header}", p.DEBUG, 1)
					for key in self.h_files[tmp_key_header].keys():
						log.print(f" H   - {key}", p.DEBUG, 2)
						for value in self.h_files[tmp_key_header][key]:
							log.print(" H     - " + value, p.DEBUG, 3)
				else:
					log.print(f"[E] {file} not found", p.DEBUG, 1)
					log.print(f"[E]   {tmp_key_c=}", p.DEBUG, 2)
					log.print(f"[E]   {tmp_key_header=}", p.DEBUG, 2)

	def	print_recursion_lvl(self):
		tmp_lvl = 1
		log.print(f"rec lvl {len(self.recursion_lvl)}", p.SUCCESS, 1)
		for lvl in self.recursion_lvl:
			log.print(f"  {tmp_lvl}. {lvl}", p.INFO, 2)
			tmp_lvl += 1

	def	get_unused_header(self):
		self.all_good = True
		for c_file in self.c_files.keys():
			self.process_file(c_file)
		if not self.all_good:
			log.print(f"{c_file} failed", p.DEBUG)
		else:
			log.print(f"None of the {a.GRE}{len(self.c_files)}{a.RST} C file, "
					   "include unused header",
					p.SUCCESS)

	def	process_file(self, c_file: str):
		with open(c_file, "r") as f:
			c_file_str = f.read()

		c_file_word = [
			w for w
			in set(reg.word.findall(c_file_str))
			if w not in BLACK_LISTED_WORD
			and w not in reg.proto.findall(c_file_str)
		]
		for header in self.c_files[c_file]:
			if not header:
				log.print(f"Wrong header in {c_file}", p.FAILURE)
				continue
			sym = self.h_files[header]
			for word in c_file_word:
				if word in sym:
					self.c_files[c_file][header].append(word)

			if len(self.c_files[c_file][header]):
				word_title = f"{a.GRE}"
				word_title += f"{a.RST}, {a.GRE}".join(self.c_files[c_file][header])
				word_title += f"{a.RST}"
				c_title = f"{a.YEL}{self.get_key(c_file)}{a.RST}"
				header_title = f"{a.YEL}{self.get_key(header)}{a.RST}"
				log.print(f"{word_title} used in"
							f" {c_title} and {header_title}", p.DEBUG)
			else:
				self.all_good = False
				c_title = f"{a.UND}{a.YEL}{self.get_key(c_file)}{a.RST}"
				header_title = f"{a.RED}{self.get_key(header)}{a.RST}"
				log.print(f"{c_title} have an unused header, {header_title}",
																	p.WARN)
				self.remove_unused_header(c_file, c_file_str, self.get_key(header))

	def	remove_unused_header(
			self,
			file_path: str,
			file_str: str,
			header_key: str
		) -> None:
		if not self.remove_unused:
			return
		to_write = re.sub(
				r'#\s*include\s+[<"]' + header_key + r'[>"]\n\n', "", file_str)
		with open(file_path, "w") as f:
			f.write(to_write)
