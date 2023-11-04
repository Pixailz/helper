from modules import *

from modules import __SETUP_DEFAULT_NAME__
from modules import __HELPER_DIR__
from modules import __MODULES__
from modules import __NO_ANSI__

class	Setup():
	def	__init__(self):
		self.config = {}

		if len(sys.argv):
			self.parsing = Parsing()
			self.parsing.parse_args()

		self.setup_json_path = os.path.join(__HELPER_DIR__, "modules/setup.json")
		if not os.path.isfile(self.setup_json_path):
			log.print(f"{self.setup_json_path} is not a file exiting", p.FAILURE)
			return

		self.populate_conf_json()

	def	populate_conf_json(self):
		with open(self.setup_json_path, "r") as f:
			setup_json = f.read()
		self.config_json = json.loads(setup_json)

		self.setup_name = os.getenv("HELPER_SETUP_NAME")
		if not self.setup_name:
			self.setup_name = __SETUP_DEFAULT_NAME__

		if self.setup_name not in self.config_json:
			log.print(f"{self.setup_name} found in config_json, aborting", p.FAILURE)
			return

		conf_json = self.config_json[self.setup_name]
		conf_setup = self.config[self.setup_name] = {
			"_config_": conf_json["_config_"],
			"_profile_": {},
		}

		conf_setup["_config_"].update({
			"no_ansi": __NO_ANSI__,
			"log_file": None,
		})

		for key in conf_json:
			if not Is.private(key):
				conf_setup["_profile_"][key] = tmp_profile = {
					"_config_": conf_json["_config_"].copy()
				}

				if "_config_" in conf_json[key]:
					tmp_profile["_config_"].update(conf_json[key]["_config_"])

				for mod_json in conf_json[key]:
					if not Is.private(mod_json):
						if mod_json in __MODULES__:
							tmp_profile[mod_json] = conf_json[key][mod_json]

"""
{
	"_default_": {
		"_config_": {
			"src_dir": "src",
			"inc_dir": "inc",
			"makefile": "mk/srcs.mk",
		},
		"_profile_": {
			"mandatory": {
				"_config_": {
					"makefile": "mk/srcs.mk",
					"src_dir": "src/mandatory"
				},
				"makefile": [
					["SRC_C_MANDATORY"]
				],
				"prototype": [
					["ft_ping.h"]
				],
				"header": []
				}
			},
		},
	}
}
"""

"""
{
    "_default_":{
        "_config_":{
            "inc_dir":"inc",
            "log_file":"None",
            "makefile":"mk/srcs.mk",
            "no_ansi":false,
            "src_dir":"src"
        },
        "_profile_":{
            "bonus":{
                "_config_":{
                    "inc_dir":"inc",
                    "log_file":"None",
                    "makefile":"mk/srcs.mk",
                    "no_ansi":false,
                    "src_dir":"src/bonus"
                },
                "header":[

                ],
                "makefile":[
                    [
                        "SRC_C_BONUS"
                    ]
                ],
                "prototype":[
                    [
                        "template_bonus.h"
                    ]
                ]
            },
            "mandatory":{
                "_config_":{
                    "inc_dir":"inc",
                    "log_file":"None",
                    "makefile":"mk/srcs.mk",
                    "no_ansi":false,
                    "src_dir":"src/mandatory"
                },
                "header":[

                ],
                "makefile":[
                    [
                        "SRC_C_MANDATORY"
                    ]
                ],
                "prototype":[
                    [
                        "template.h"
                    ]
                ]
            },
            "test":{
                "_config_":{
                    "inc_dir":"inc",
                    "log_file":"None",
                    "makefile":"mk/srcs.mk",
                    "no_ansi":false,
                    "src_dir":"src"
                },
                "header":[

                ],
                "makefile":[
                    [
                        "SRC_C"
                    ]
                ],
                "prototype":[
                    [
                        "test.h"
                    ]
                ]
            }
        }
    }
}
"""
