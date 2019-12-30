"""
Route module for timeconverter web api
"""
from app import app
from flask import (request, jsonify, render_template, redirect,
                   url_for, flash, make_response)
from datetime import datetime
import socket
import os

# Modules constants
secret_file = '/run/secrets/my_secret_key'
localhost = socket.gethostname()

#
# HTML page
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    """Build response data and send page to requester."""
    response_data = build_response_data()
    return render_template('index.html', title='Home', resp=response_data)

#
# REST API
@app.route('/api/echo', methods=['GET'])
def rest_api():
    """Build api endpoint and send json response."""
    resp = make_response(jsonify(build_response_data()))
    resp.headers['Server-IP'] = socket.gethostbyname(localhost)
    return resp
    # return jsonify(build_response_data())


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
