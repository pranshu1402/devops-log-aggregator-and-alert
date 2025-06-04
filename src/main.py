import sys
import os
#To set the path to root directory of the project as without this, importing config from config.config fails
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from config.config import config

# Initialize producers, consumers, sinks, queues

# Initialize the application

print(config.MONGO_URI)
