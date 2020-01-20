"""
Route module for timeconverter web api
"""
from app import app, config
from flask import (request, jsonify, render_template, redirect,
                   url_for, flash, make_response)
from datetime import datetime
import socket
import os

# Modules constants
secret_file = '/run/secrets/my_secret_key'
config_file = '/srv-config.yml'
localhost = socket.gethostname()
srv_config = {
    'title': 'Echo Server',
    'footer': 'Default configuration'
}

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
def rest_api():
    """Build api endpoint and send json response."""
    resp = make_response(jsonify(build_response_data()))
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
            f = open(config.Config.SECRET_FILE, 'r')
            secret = f.read()
        except:
            # no file, just return empty string
            secret = config.Config.SECRET_KEY
        return secret
