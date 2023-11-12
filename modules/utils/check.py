from modules import *

class	Is():
	def	__init__(self) -> None: pass

	@staticmethod
	def	private(src: str) -> bool:
		return (src[0] == '_')

	@staticmethod
	def	private_header(src: str) -> bool:
		basename = os.path.basename(src)
		if not basename: return False
		return Is.private(basename)
