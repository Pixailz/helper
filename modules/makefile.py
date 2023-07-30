import os

from pprint import pprint

from modules.config import CWD
from modules.regex import reg
from modules.log import log, p, a

class Makefile():
	def	__init__(self, makefile, src_dir, makefile_path_depth=0):
		self.makefile = os.path.join(CWD, makefile)
		self.src_dir = os.path.join(CWD, src_dir)
		log.print(f"Makefile target{a.SEP}{makefile}", mode = p.DEBUG, level = 1)
		log.print(f"Makefile src   {a.SEP}{src_dir}", mode = p.DEBUG, level = 1)
		self.makefile_var = []
		self.makefile_path_depth = makefile_path_depth
		with open(self.makefile, 'r') as f:
			self.makefile_str = f.read()

	def	add_var(self, var, folder):
		log.print(f"{var}{a.SEP}{folder}", mode = p.DEBUG, level = 1)
		self.makefile_var.append({var: folder})

	def	format_src(self, var, *srcs):
		srcs = [ item for item in sorted(srcs) ]
		formated = []
		formated.append(f"{var} := {srcs[0]}")
		if (len(srcs) != 1):
			srcs.pop(0)
			var_len = len(var) + 4
			tab_str = "\t" * int(var_len / 4) + " " * (var_len % 4)
			formated[0] += " \\"
			for item in srcs:
				formated.append(f"{tab_str}{item} \\")
		last_id = len(formated) - 1
		formated[last_id] = formated[last_id].removesuffix(" \\")
		formated = [ item + '\n' for item in formated ]
		formated[last_id] = formated[last_id].removesuffix('\n')
		formated = ''.join(formated)
		log.print(f"[{var}] formated\n{formated}", mode = p.DEBUG, level = 2)
		return formated

	def	get_src(self, var, folder):
		target_dir = os.path.join(self.src_dir, folder)
		log.print(f"target dir{a.SEP}[{target_dir}]", mode = p.DEBUG, level = 1)
		files = []
		for (dirpath, dirname, filename) in os.walk(target_dir):
			for file in filename:
				file_path = f"{dirpath}/{file}".removeprefix(self.src_dir + '/')
				log.print(f"file found [{file_path}]", mode = p.DEBUG, level = 3)
				files.append(file_path)
		log.print(f"{len(files)} file found for {a.RED}{folder}{a.RST}")
		return (self.format_src(var, *files))

	def	update_makefile(self):
		for item in self.makefile_var:
			for var, folder in item.items():
				from_replace = reg.get_var_make(var, self.makefile_str)
				if not from_replace:
					log.print(f"[{var}] not found", mode = p.WARN)
					continue
				to_replace = self.get_src(var, folder)
				self.makefile_str = self.makefile_str.replace(from_replace, to_replace)
		log.print(f"[{self.makefile}] formated\n{self.makefile_str}", mode = p.DEBUG, level = 4)
		with open(self.makefile, 'w') as f:
			f.write(self.makefile_str)
