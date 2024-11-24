# Copyright (c) 2021 - Present Itz-fork
# Author: https://github.com/Itz-fork
# Project: https://github.com/Itz-fork/Mega.nz-Bot
# Description: __init__.py

import os
import logging
import requests

# start msg
print("Mega.nz Bot - Cypher is starting...")
env_file_path = 'yi.env'
env_file_url = 'https://github.com/Itzmepromgitman/Mega.nz-Bot/blob/main/megadl/config.env'


# loading config
from dotenv import load_dotenv
print("--------------------")
print("> Loading config")
if os.path.isfile('.env'):
    load_dotenv()
else:
    logging.warning("WARNING: No .env file found. Attempting to download from URL.")
    try:
        response = requests.get(env_file_url)
        response.raise_for_status()  # Check if the request was successful
        with open(env_file_path, 'w') as env_file:
            env_file.write(response.text)
        load_dotenv()  # Load the newly downloaded .env file
        logging.info(".env file downloaded and loaded successfully.")
    except requests.exceptions.RequestException as e:
        logging.error(f"Failed to download .env file: {e}")


# client
from .helpers.cypher import MeganzClient
import os
CypherClient: "MeganzClient" = MeganzClient()
