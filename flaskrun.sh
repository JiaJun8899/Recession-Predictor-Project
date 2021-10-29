#!/bin/bash
# flask settings
export FLASK_APP=/var/www/1002/flaskrun.py
export FLASK_DEBUG=1

flask run --host=0.0.0.0 --port=80
