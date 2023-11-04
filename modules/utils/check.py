from modules import *

class	Is():
	def	__init__(self) -> None: pass

	def	private(self, src: str) -> bool:
		return (src[0] == '_')

	def	private_header(self, src: str) -> bool:
		basename = os.path.basename(src)
		if not basename: return False
		return self.private(basename)
