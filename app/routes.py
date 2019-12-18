"""
Route module for timeconverter web api
"""
from app import app
from flask import (request, jsonify, render_template, redirect,
                  url_for, flash)
from datetime import datetime
import socket

#
# HTML page
@app.route('/', methods=['GET', 'POST'])
@app.route('/index', methods=['GET', 'POST'])
def index():
    resonse_data = build_response_data()
    return render_template('index.html', title='Home', resp=resonse_data)

def build_response_data():
    localhost = socket.gethostname()
    return {
        'now': datetime.now().isoformat(sep=' '),
        'local_ip': socket.gethostbyname(localhost),
        'container_name': localhost,
        'remote_ip': request.remote_addr       
    }
