from modules import *

class Header():
	def	__init__(self,
			inc_dir: str,
			src_dir: str,
			excluded_files: list[str]	= [],
			max_recursion: int			= 10,
		):
		self.inc_dir: str = os.path.join(CWD, inc_dir)
		self.src_dir: str = src_dir

		self.c_files: dict[any] = {}
		self.h_tree_files: dict[any] = {}

		self.recursion_lvl: list[str] = []

		self.max_recursion = max_recursion
		self.lib_dir = self.get_lib_dir()

		self.reset_stats()
		self.populate_files(excluded_files)
		self.update_header_tree()
		self.print_data()
		self.clean_header_tree()

	def	get_lib_dir(self):
		result = []
		io = reg.c_inc_dir.findall(
			subprocess.run(
				["echo | clang -xc -E -v -"],
				shell=True,
				capture_output=True,
			).stderr.decode("utf-8")
		)
		if len(io):
			for item in io[0].split('\n'):
				if len(item):
					result.append(item.removeprefix(" "))
		io = reg.c_inc_dir.findall(
			subprocess.run(
				["echo | gcc -xc -E -v -"],
				shell=True,
				capture_output=True,
			).stderr.decode("utf-8")
		)
		if len(io):
			for item in io[0].split('\n'):
				if len(item):
					result.append(item.removeprefix(" "))
		return (sorted(set(result), reverse=True))

	def	reset_stats(self):
		self.stats_prefix = "nb_symbols_"

		# LIBFT:
		## NB_SYMBOLS_FUNCTION: 286
		## NB_SYMBOLS_DEFINE:   131
		## NB_SYMBOLS_TYPEDEF:  576
		## NB_SYMBOLS_ENUM:     158
		## NB_SYMBOLS_C_FILES:  123
		## NB_SYMBOLS_H_FILES:  23

		self.nb_symbols_function = 0
		self.nb_symbols_define = 0
		self.nb_symbols_typedef = 0
		self.nb_symbols_enum = 0
		self.nb_symbols_c_files = 0
		self.nb_symbols_h_files = 0

	def	print_stats(self, title: str):
		log.print(title, p.SUCCESS)
		log.print(f"  function: {self.nb_symbols_function}", p.INFO)
		log.print(f"  define:   {self.nb_symbols_define}", p.INFO)
		log.print(f"  typedef:  {self.nb_symbols_typedef}", p.INFO)
		log.print(f"  enum:     {self.nb_symbols_enum}", p.INFO)
		log.print(f"in", p.SUCCESS)
		log.print(f"  c file:   {self.nb_symbols_c_files}", p.INFO)
		log.print(f"  h file:   {self.nb_symbols_h_files}", p.INFO)

	def	print_data(self, include: list[str] = []):
		if not len(include):
			for file in self.c_files:
				log.print(f" C {file}", p.DEBUG, 1)
				for value in self.c_files[file]:
					log.print(" C   " + value, p.DEBUG, 2)
			for file in self.h_tree_files:
				log.print(f" H {file}", p.DEBUG, 1)
				for key in self.h_tree_files[file].keys():
					log.print(f" H   - {key}:", p.DEBUG, 2)
					for value in self.h_tree_files[file][key]:
						log.print(" H     - " + value, p.DEBUG, 3)
		else:
			for file in include:
				tmp_key_c = self.get_c_key(file)
				tmp_key_header = self.get_path_header(file)

				if tmp_key_c in self.c_files.keys():
					log.print(f" C {file}", p.DEBUG, 1)
					for value in self.c_files[file]:
						log.print(" C   " + value, p.DEBUG, 2)
				elif tmp_key_header in self.h_tree_files:
					log.print(f" H {tmp_key_header}", p.DEBUG, 1)
					for key in self.h_tree_files[tmp_key_header].keys():
						log.print(f" H   - {key}", p.DEBUG, 2)
						for value in self.h_tree_files[tmp_key_header][key]:
							log.print(" H     - " + value, p.DEBUG, 3)
				else:
					log.print(f"[E] {file} not found", p.DEBUG, 1)
					log.print(f"[E]   {tmp_key_c=}", p.DEBUG, 2)
					log.print(f"[E]   {tmp_key_header=}", p.DEBUG, 2)

	def	get_c_key(self, c_file: str) -> None:
		if c_file[:len(self.src_dir)] == self.src_dir:
			return(c_file.removeprefix(self.src_dir + '/'))
		else:
			return (c_file)

	def	get_path_header(self, header) -> str:
		header_path = os.path.join(self.inc_dir, header)
		if os.path.isfile(header_path):
			return (header_path)
		for lib_dir in self.lib_dir:
			header_path = os.path.join(lib_dir, header)
			if os.path.isfile(header_path):
				return (header_path)
		return (None)

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

	def	print_recursion_lvl(self):
		tmp_lvl = 1
		log.print(f"rec lvl {len(self.recursion_lvl)}", p.SUCCESS, 1)
		for lvl in self.recursion_lvl:
			log.print(f"  {tmp_lvl}. {lvl}", p.INFO, 2)
			tmp_lvl += 1

	def	is_private(self, src: str) -> bool:
		return (src[0] == '_')

	def	is_private_header(self, src: str) -> bool:
		basename = os.path.basename(src)
		if not basename: return False
		return self.is_private(basename)

	def	populate_files(self, excluded_files: list[str] = []) -> None:
		files = get_file(f"{self.src_dir}/**/*.c", excluded_files)
		self.nb_symbols_c_files += len(files)
		for file in files:
			self.populate_files_c(file)
		files = get_file(f"{self.inc_dir}/**/*.h", excluded_files)
		self.nb_symbols_h_files += len(files)
		for file in files:
			self.populate_files_h_tree(file)
		self.print_stats("Successfully parsed:")

	def	populate_files_c(self, c_file: str) -> None:
		with open(c_file, "r") as f:
			c_file_str = f.read()
		c_file_header = reg.c_header.findall(c_file_str)
		c_key = self.get_c_key(c_file)
		self.update_data("c_files", c_file_header, c_key)

	def	get_symbols(self, header_str: str) -> list:
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
				for key_2 in content[key]:
					if not self.is_private(key_2):
						parsed_content.append(key_2)
						parsed_content.extend(content[key][key_2])
						changed += len(content[key][key_2]) + 1
			else:
				for key_2 in content[key]:
					if not self.is_private(key_2):
						parsed_content.append(key_2)
						changed += 1
			tmp_name = self.stats_prefix + key
			tmp = getattr(self, tmp_name)
			setattr(self, tmp_name, tmp + changed)
		# pprint([i for i in content if not self.is_private(i)])
		return (parsed_content)

	def	populate_files_h_tree(self, h_file: str) -> None:
		if self.is_private_header(h_file): return

		header_path = self.get_path_header(h_file)
		if not header_path: return
		with open(header_path, "r") as f:
			h_file_str = f.read()

		h_file_header = reg.c_header.findall(h_file_str)
		h_file_symbols = self.get_symbols(h_file_str)

		# update data
		self.update_data("h_tree_files", h_file_header, header_path, "header")
		self.update_data("h_tree_files", h_file_symbols, header_path, "symbols")
		# recursive part
		for header in h_file_header:
			path_header = self.get_path_header(header)
			if path_header and path_header not in self.h_tree_files:
				self.populate_files_h_tree(path_header)

	def	update_header_leaf(self, header_name: str) -> any:
		"""
		Depth First Search algorithm (DFS)
		Merge foreign key according to headers in data struct,
		then recursivly merge symbols of each layer of header
		"""
		if self.is_private_header(header_name): return {}

		try:
			self.recursion_lvl.index(header_name)
			return {}
		except ValueError:
			pass


		header_path = self.get_path_header(header_name)
		if not header_path: return {}

		if len(self.recursion_lvl) > self.max_recursion:
			log.print(
				f"exceeded recursion, MAX"
				f"{self.max_recursion},CUR{len(self.recursion_lvl)}",
				p.WARN)
			return {}
		self.recursion_lvl.append(header_name)
		# self.print_recursion_lvl()

		current_content: dict = {}

		if "symbols" in self.h_tree_files[header_path]:
			current_content[header_path] = \
				self.h_tree_files[header_path]["symbols"]
		else:
			current_content[header_path] = []

		if "header" in self.h_tree_files[header_path]:
			for header in self.h_tree_files[header_path]["header"]:
				tmp_key = self.get_path_header(header)
				if not tmp_key:
					tmp_key = header
				tmp_content = self.update_header_leaf(tmp_key)
				current_content.update(tmp_content)
			del self.h_tree_files[header_path]["header"]

		tmp_list = []
		for key in current_content.keys():
			tmp_list.extend(current_content[key])
		if len(tmp_list):
			self.h_tree_files[header_path]["symbols"] = set(tmp_list)
		self.recursion_lvl.remove(header_name)
		return current_content

	def	update_header_tree(self) -> None:
		for h_tree_key in self.h_tree_files.keys():
			self.current_content = {}
			self.follow_content = {}
			self.recursion_lvl = []
			self.update_header_leaf(h_tree_key)

	def	clean_header_tree(self) -> None:
		for key in self.h_tree_files:
			self.h_tree_files[key] = [
				s for s in sorted(self.h_tree_files[key]["symbols"])
			]

if __name__ == "__main__":
	config = {
		"inc_dir": "inc",
		"src_dir": "src",
	}
	header = Header(**config)
	header.print_data([
		# "test/libft_a.h",
		# "test/libft_b.h",
		# "test/libft_c.h",
		# "test/libft_d.h",
		# "test/libft_e.h",
		# "test/libft_f.h",
		# "test/libft_g.h",
		# "test/libft_h.h",
		# libft
		"libft_print.h",
		"string/ft_strlen.c",
		"print/ft_printf.c",
		"libft_string.h",

		# # standard
		"stdarg.h",
		"stdlib.h",
	])
