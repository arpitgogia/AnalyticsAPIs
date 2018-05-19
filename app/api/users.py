from flask import Blueprint, request, jsonify
import json
api = Blueprint('api', __name__)

@api.route('/returnToken', methods=["POST"])
def returnToken():
	return {"test": "test"};

@api.route('/eventlog', methods=["POST"])
def eventlog():
	return {"test": "test"};
	