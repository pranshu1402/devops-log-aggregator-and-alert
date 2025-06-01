# Creates a config class to load environment variables

import os
from dotenv import load_dotenv
load_dotenv()

class Config:
    MONGO_URI = ''
    AWS_REGION = ''
    AWS_PROFILE = ''

    def __init__(self):
        self.MONGO_URI = os.getenv("MONGO_DB_URI")
        self.AWS_REGION = os.getenv("AWS_REGION")
        self.AWS_PROFILE = os.getenv("AWS_PROFILE")
        
        print(self.MONGO_URI, self.AWS_REGION, self.AWS_PROFILE)

# Create a single instance that will be used throughout the application
config = Config()
