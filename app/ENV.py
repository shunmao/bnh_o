from os import getenv
from dotenv import (load_dotenv, find_dotenv)
from pathlib import Path

# env_path = Path('.') / '.env'

load_dotenv(find_dotenv())  # dotenv_path=env_path

# flask
SECRET_KEY = getenv('SECRET_KEY')
# WTF_CSRF_SECRET_KEY = getenv('WTF_CSRF_SECRET_KEY')
# SQLALCHEMY_TRACK_MODIFICATIONS = getenv('SQLALCHEMY_TRACK_MODIFICATIONS')

# # database
SQLALCHEMY_DATABASE_URI = getenv('SQLALCHEMY_DATABASE_URI')


