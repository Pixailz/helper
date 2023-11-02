from modules import *

def	get_file(
		glob_path: str,
		exclude: list[str] = [],
	) -> list[str]:

	files = glob.glob(glob_path, recursive=True)
	for file in exclude:
		files.remove(file)
	return (sorted(files))
