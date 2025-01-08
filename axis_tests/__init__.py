import os
from dotenv import load_dotenv
import logging

# Set up logging configuration
logging.basicConfig(
    filename='app.log',  # Specify the log file name
    level=logging.DEBUG,  # Set the logging level (DEBUG, INFO, WARNING, ERROR, CRITICAL)
    format='%(asctime)s - %(levelname)s - %(message)s',  # Customize the log message format
)

load_dotenv()
HOST=os.getenv("HOST")
PORT=os.getenv("PORT")
USERNAME=os.getenv("USER")
PASSWORD=os.getenv("PASSWORD")