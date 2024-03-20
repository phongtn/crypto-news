import yaml
from datetime import datetime

import os


def load_config():
    # Get the current directory of main.py
    current_directory = os.path.dirname(os.path.abspath(__file__))
    # Go up one directory to access ROOT directory
    root_directory = os.path.dirname(current_directory)
    # Specify the path to the config.yaml file relative to the ROOT directory
    config_path = os.path.join(root_directory, "config.yaml")
    with open(config_path, "r") as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    return cfg


from datetime import datetime


def convert_iso8601_to_unix_timestamp(iso8601):
    """
    Convert an ISO8601 formatted timestamp (e.g. 2020-01-01T00:00:00Z or 2020-01-01T00:00:00+01:00) to a Unix timestamp (e.g. 1600000000).
    """
    try:
        return str(int(datetime.fromisoformat(iso8601).timestamp()))
    except ValueError:
        return str(int(datetime.strptime(iso8601, "%Y-%m-%dT%H:%M:%S%z").timestamp()))
