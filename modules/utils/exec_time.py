from modules import *

def	print_elapsed(title: str, begin, end) -> None:
	elapsed_time = end - begin
	if elapsed_time > 5:
		elapsed_str = a.RED
	elif elapsed_time > 1:
		elapsed_str = a.YELLOW
	else:
		elapsed_str = a.GREEN
	elapsed_time *= 1_000
	elapsed_str += str(round(elapsed_time, 3)) + a.RST
	log.print(f"Module {a.YELLOW}{title}{a.RST} "
			  f"took {elapsed_str} ms", p.INFO)
