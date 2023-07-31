from modules import *

class Prototype():
	def	__init__(self, inc_dir, src_dir):
		self.inc_dir = os.path.join(CWD, inc_dir)
		self.src_dir = os.path.join(CWD, src_dir)
		log.print(f"Prototype base inc dir {a.SEP}[{self.inc_dir}]", p.DEBUG, 1)
		log.print(f"Prototype base src dir {a.SEP}[{self.src_dir}]", p.DEBUG, 1)
		self.headers = []

	def	add_header(self, header, folder=None):
		log.print(f"{header}{a.SEP}{folder}", p.DEBUG, 1)
		self.headers.append({header: folder})

	def	get_header(self):
		with open(self.header, 'r') as f:
			header_str = f.read()
		founded = reg.get_src_header.search(header_str)
		if not founded:
			return 1
		self.src_pos = founded.start()
		with open(self.header, 'r') as f:
			self.src_pos = f.read(self.src_pos).count('\n')
		log.print(f"found first block at lineno [{self.src_pos}] in [{self.header}]", p.DEBUG, 2)
		log.print(f"found [{len(reg.get_src_header.findall(header_str))}] block in [{self.header}]", p.DEBUG, 2)
		self.header_str = [ item + '\n'
							for item in
							reg.get_src_header.sub('', header_str).split('\n') ]
		self.header_str[len(self.header_str) - 1] = self.header_str[len(self.header_str) - 1].removesuffix('\n')
	def	get_proto_file(self, src_path):
		src_id = src_path.removeprefix(self.src_dir + '/')
		with open(src_path, 'r') as f:
			src_str = f.read()
		self.to_replace[src_id] = []
		func = reg.proto_func.findall(src_str)
		if not len(func):
			log.print(f"prototype not found in [{src_path}]", p.FAILURE, 1)
			return
		for item in func:
			func_type = reg.proto_type.findall(item)
			func_not_type = reg.proto_not_type.findall(item)
			if not len(func_type):
				log.print(f"type not found in [{item}]", p.FAILURE, 1)
				return
			if not len(func_not_type):
				log.print(f"prototype without type not found in [{item}]", p.FAILURE, 1)
				return
			log.print(
				f"found {a.RED}{func_type[0]} {a.GREEN}{func_not_type[0]}{a.RST}",
				p.DEBUG, 3)
			self.to_replace[src_id].append((func_type[0], func_not_type[0] + ";\n"))

	def	get_header_len(self):
		self.max_len = 0
		for function in self.to_replace.values():
			for proto in function:
				if self.max_len < len(proto[0]):
					self.max_len = len(proto[0])
		self.max_len = int(self.max_len / 4) + (self.max_len % 4 != 0) + 1

	def	get_proto(self):
		self.to_replace = {}
		file_path = []
		for (dirpath, dirname, filename) in os.walk(self.header_src_dir):
			for file in filename:
				file_path.append(os.path.join(dirpath, file))
		file_path = sorted(file_path)
		for path in file_path:
			log.print(f"file found [{path}]", p.DEBUG, 3)
			self.get_proto_file(path)
		self.get_header_len()
		to_replace = []
		for file_path, function in self.to_replace.items():
			to_replace.append(f"// {os.path.basename(file_path)}\n")
			for proto in function:
				tab = '\t' * (self.max_len - int(len(proto[0]) / 4))
				new_line = f"{proto[0]}{tab}{proto[1]}"
				for line in new_line.split('\n'):
					len_line = len(line.expandtabs(4))
					if len_line > 80:
						log.print(f"line too long{a.SEP}{len_line}\n\t[{line}]", p.WARN, 2)
				to_replace.append(f"{new_line}")
			to_replace.append('\n')
		self.to_replace = to_replace

	def	update_include(self):
		for item in self.headers:
			for header, folder in item.items():
				self.header = os.path.join(self.inc_dir, header)
				if folder:
					self.header_src_dir = os.path.join(self.src_dir, folder)
				else:
					self.header_src_dir = self.src_dir
				if not os.path.isfile(self.header):
					log.print(f"file not found {self.header}", p.WARN)
					return
				if not os.path.isdir(self.header_src_dir):
					log.print(f"folder not found {self.header_src_dir}", p.WARN)
					return
				if self.get_header():
					log.print(f"block not found in {self.header}", p.WARN)
					return
				if self.get_proto():
					log.print(f"no prototype found in {self.header}", p.WARN)
					return
				self.header_str.insert(self.src_pos, ''.join(self.to_replace))
				with open(self.header, 'w') as f:
					f.write(''.join(self.header_str))
