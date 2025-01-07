import sys
import os
from dotenv import load_dotenv

load_dotenv()
HOST=os.getenv("HOST")
PORT=os.getenv("PORT")
USERNAME=os.getenv("USER")
PASSWORD=os.getenv("PASSWORD")