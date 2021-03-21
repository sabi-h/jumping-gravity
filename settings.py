import os

from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


TOKEN = os.getenv("PUBLISHABLE_TOKEN")
PROJECT_ID = os.getenv("PROJECT_ID")
