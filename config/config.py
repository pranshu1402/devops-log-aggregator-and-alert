# Creates a config class to load environment variables

import os
from dotenv import load_dotenv
#For parsing the complex password of MongoDB 
from urllib.parse import quote_plus
load_dotenv()

class Config:
    MONGO_URI = ''
    AWS_REGION = ''
    AWS_PROFILE = ''

    def __init__(self):
        #MongoDB URI is given as mongodb+srv://<user>:<password>@<cluster-host>/ and then MONGO_USER and MONGO_PASS given separately
        raw_uri = os.getenv("MONGO_DB_URI")

        # Split to inject encoded credentials
        user = quote_plus(os.getenv("MONGO_USER"))
        password = quote_plus(os.getenv("MONGO_PASS"))
        #Constructing the whole URI
        self.MONGO_URI = raw_uri.replace("<user>", user).replace("<password>", password)
        self.AWS_REGION = os.getenv("AWS_REGION")
        self.AWS_PROFILE = os.getenv("AWS_PROFILE")
        
        #print(self.MONGO_URI, self.AWS_REGION, self.AWS_PROFILE)

# Create a single instance that will be used throughout the application
config = Config()
