
from modules import *

class	a():
	# BASE
	ESC		= "\x1b"

	# COLOR
	BLA	= f"{ESC}[30"
	RED	= f"{ESC}[31m"
	GRE	= f"{ESC}[32m"
	YEL	= f"{ESC}[33m"
	BLU	= f"{ESC}[34m"
	PUR	= f"{ESC}[35m"
	CYA	= f"{ESC}[36m"
	WHI	= f"{ESC}[37m"

	# MODIFIER
	RST	= f"{ESC}[0m"
	BOL	= f"{ESC}[1m"
	ITA	= f"{ESC}[3m"
	UND	= f"{ESC}[4m"
	BLI	= f"{ESC}[5m"

	# COMPOSITE
	SEP	= f" "
