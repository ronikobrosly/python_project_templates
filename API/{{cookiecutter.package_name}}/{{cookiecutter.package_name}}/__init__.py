"""
Global variables and configuration variarbles for the {{cookiecutter.package_name}}
"""

import configparser
import os
import sys

import requests


CONFIG = configparser.ConfigParser()

try:
    CONFIG.read("./{{cookiecutter.package_name}}/{{cookiecutter.package_name}}.cfg")

except Exception as e:
    print(f"Failed to read configuration file: {e}, aborting")
    sys.exit(1)



HEALTHCHECK_URL = os.getenv("HEALTHCHECK_URL", "#")

LOG_STASH_URL = os.getenv("LOG_STASH_URL", "#")

{{cookiecutter.package_name}}_VERSION = CONFIG.get("Versions", "APP_VERSION")

API_KEY_ID = "abc"
API_KEY_SECRET = "123"

TIMEOUT = float(os.getenv("TIMEOUT", "300"))
