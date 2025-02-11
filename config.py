from dotenv import load_dotenv
import os

load_dotenv()

POKEMON_API = os.getenv("POKEMON_API")
DATABASE_URI = os.getenv("DATABASE_URI")
