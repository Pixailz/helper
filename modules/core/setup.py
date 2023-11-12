from modules import *

from modules import __HELPER_DIR__
from modules import __MODULES__

class	Setup():
	def	__init__(self):
		self.config = {}

		parsing.parse_args()

		self.setup_json_path = os.path.join(__HELPER_DIR__, "modules/core/setup.json")
		if not os.path.isfile(self.setup_json_path):
			log.print(f"{self.setup_json_path} is not a file exiting", p.FAILURE)
			return

		self.populate_conf_json()

	def	populate_conf_json(self):
		with open(self.setup_json_path, "r") as f:
			setup_json = f.read()
		self.config_json = json.loads(setup_json)

		if parsing.args["setup_name"] not in self.config_json:
			log.print(f"{parsing.args['setup_name']} found in config_json, aborting", p.FAILURE)
			return

		conf_json = self.config_json[parsing.args["setup_name"]]
		conf_setup = self.config[parsing.args["setup_name"]] = {
			"_config_": conf_json["_config_"],
			"_profile_": {},
		}

		conf_setup["_config_"].update({
			"no_color": parsing.args["no_color"],
			"log_file": parsing.args["log_file"],
		})

		for key in conf_json:
			if not Is.private(key):
				conf_setup["_profile_"][key] = tmp_profile = {
					"_config_": conf_setup["_config_"].copy()
				}

				if "_config_" in conf_json[key]:
					tmp_profile["_config_"].update(conf_json[key]["_config_"])

				for mod_json in conf_json[key]:
					if not Is.private(mod_json):
						if mod_json in __MODULES__:
							tmp_profile[mod_json] = conf_json[key][mod_json]

setup = Setup()
