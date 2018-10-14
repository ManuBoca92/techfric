import os
import logging

# Define the application directory
BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    DEBUG = False
    TESTING = False
    SECRET_KEY = "Affiong"

    # MONGODB_SETTINGS = {
    #     'db': 'magebutton_cloud',
    #     'host': '10.1.0.56',
    #     'port': 27017
    # }


