import os


class Config(object):
    """Read and set configuration values"""
    SECRET_KEY = os.environ.get(
        'SECRET_KEY') or get_secret_key() or 'Only_the_default_secret_key'

    def get_secret_key(self):
        with open('/run/secrets/my_secret_key', 'r') as f:
            return f.read()
