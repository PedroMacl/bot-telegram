from dotenv import load_dotenv
from os import getenv
load_dotenv(".env",override=True)

BOT_TOKEN=getenv("BOT_TOKEN")