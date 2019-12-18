import os

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'p5Gnci8743bcRcQ76J'