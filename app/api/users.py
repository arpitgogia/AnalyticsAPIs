from flask import Blueprint, request, jsonify
from app.db import user
import json
api = Blueprint('api', __name__)

@api.route('/returnToken', methods=["POST"])
def returnToken():
	return user.generateToken(request.form['install_time']);

@api.route('/eventlog', methods=["POST"])
def eventlog():
	return user.insertEventLog(request.get_json())
	