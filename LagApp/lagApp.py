#!/usr/bin/env python3
from flask import Flask, request, url_for, redirect, render_template, jsonify, abort, Response
import os
import time

# Setup delay in seconds
DELAY = 6


app = Flask(__name__, template_folder='templates')


# On BlueMix, get the port number from the environment variable VCAP_APP_PORT
# when running the app locally, default the port to 8080
port = int(os.getenv('VCAP_APP_PORT', 8080))


@app.route('/')
def index():
    global DELAY

    time.sleep(DELAY)

    return render_template('index.html', delay=DELAY)


if __name__ == "__main__":
#     app.run(host='0.0.0.0', port=port, debug=True, threaded=True)
    app.run(host='0.0.0.0', port=port, threaded=True)

