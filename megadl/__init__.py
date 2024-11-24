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
    os.environ['APP_ID'] = '25769635'
    os.environ['API_HASH'] = '863eec9ad6c6d54ceef169cb244d9349'
    os.environ['BOT_TOKEN'] = '7744440054:AAGPb8szzj-35KJbcsH8mcnsMljb9gZrXQM'
    
    
    os.environ['AUTH_USERS'] = '7037784425'
    os.environ['USE_ENV'] = 'False'
    os.environ['LOG_CHAT'] = '0'
    
    os.environ['DOWNLOAD_LOCATION'] = '${PWD}/NexaBots'
    os.environ['CHUNK_SIZE'] = '524288'
    os.environ['TG_MAX_SIZE'] = '2040108421'

# client
from .helpers.cypher import MeganzClient
import os
CypherClient: "MeganzClient" = MeganzClient()
