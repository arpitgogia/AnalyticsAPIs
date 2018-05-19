from flask import Flask, request, json
from app.api import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api/v1")

if __name__ == '__main__':
	app.run()