import sys
import os
sys.path.append('../app')

from config import Config

def test_accesslog_default():
    assert Config.ACCESSLOG == ''

def test_config_secretkey_default():
    assert Config.SECRET_KEY == 'Only_the_default_secret_key'

# def test_accesslog_environment():
#     value = '/usr/log/accesslog'
#     os.environ['ACCESSLOG'] = value
#     #os.putenv('ACCESSLOG',value)
#     print(os.environ)
#     c = Config()
#     assert c.ACCESSLOG == value