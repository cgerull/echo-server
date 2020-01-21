"""
Route module for timeconverter web api
"""
from app import app
from flask import (request, jsonify, render_template, redirect,
                   url_for, flash, make_response)
from datetime import datetime
import socket
import os
import yaml

# Modules constants
secret_file = '/run/secrets/my_secret_key'
config_file = '/srv-config'
srv_config = {
    'title': 'Echo Webserver',
    'footer': 'Default configuration'
}
localhost = socket.gethostname()

#
# HTML page
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """Build response data and send page to requester."""
    response_data = build_response_data()
    resp = make_response(render_template('index.html', title=srv_config['title'], footer=srv_config['footer'], resp=response_data))
    resp.headers['Server-IP'] = socket.gethostbyname(localhost)
    return resp


#
# REST API
@app.route('/api/echo', methods=['GET'])
def api_echo():
    """Build api endpoint for echo data."""
    resp = make_response(jsonify(build_response_data()))
    resp.headers['Server-IP'] = socket.gethostbyname(localhost)
    return resp


#
# REST API
@app.route('/api/config', methods=['GET'])
def api_config():
    """Build api endpoint for config data."""
    resp = make_response(jsonify(read_config(config_file, srv_config)))
    resp.headers['Server-IP'] = socket.gethostbyname(localhost)
    return resp


def build_response_data():
    """
    Build a dictionary with timestamp, server ip,
    server name, secret and requester ip.
    """
    localhost = socket.gethostname()
    return {
        'now': datetime.now().isoformat(sep=' '),
        'local_ip': socket.gethostbyname(localhost),
        'container_name': localhost,
        'secret': get_secret_key(),
        'remote_ip': request.remote_addr
    }


def get_secret_key():
    secret = ''
    try:
        f = open(secret_file, 'r')
        secret = f.read()
    except:
        # no file, just return empty string
        secret = os.environ.get('SECRET_KEY') or 'Only_the_default_secret_key'
    
    return secret


# def get_config(cf_file):
#     try:
#         cf = open(cf_file, r)
#         if cf.readable():
#             config = read_config('/srv-config')
#     except Exception as exc:
#         print("Can't open configuration file. {}".format(exc))


def read_config(config_file, srv_config):
    result = {}
    with open(config_file, 'r') as stream:
        try:
            config_data = (yaml.safe_load(stream))
            for key in config_data.keys():
                srv_config[key] = config_data[key]
            
        except yaml.YAMLError as exc:
            print("Can't read configuration. {}".format(exc))
    return(result)
