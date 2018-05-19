from flask import Flask, request, json
from app.api import api

app = Flask(__name__)
app.register_blueprint(api, url_prefix="/api/v1")

@app.route('/')
def main():
	return "Welcome to analytics api server"
	

if __name__ == '__main__':
	app.run()