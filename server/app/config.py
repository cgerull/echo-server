import os


class Config(object):
    """Read and set configuration values"""
    SECRET_KEY = 'Only_the_default_secret_key'
    SECRET_FILE = '/run/secrets/my_secret_key'

    # def get_secret_key():
    #     return os.getenv('SECRET_KEY') or _SECRET_KEY

    # def get_secret_file():
    #     return  _SECRET_FILE