import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv(dotenv_path='.env.development')

# Creating a configuration class where the config settings are its attributes


class Config:
    SECRET_KEY = os.getenv('SECRET_KEY')
