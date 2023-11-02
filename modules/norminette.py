from modules import *

def	norminette_isinstalled() -> bool:
	try:
		import norminette
	except ImportError:
		return (False)
	return (True)

def	check_norminette(args: list[str] = []) -> bool:
	if (not norminette_isinstalled()):
		log.print("""
				Norminette is not installed, norminette module cannot go further.
				check this link for more information, https://github.com/42School/norminette
				""", p.FAILURE)
		return (False)
	result = subprocess.run(
		[
			"python3",
			"-m",
			"norminette",
			*args,
		],
		capture_output=True,
	)
	if (result.returncode != 0):
		print(result.stdout.decode("utf-8"))
		log.print("bad project, exiting", p.FAILURE)
		sys.exit(1)
	log.print("good project", p.SUCCESS)
	return (result.returncode)

if __name__ == "__main__":
	check_norminette()
