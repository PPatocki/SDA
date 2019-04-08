#!flask/bin/python
from flask import Flask
from flask import jsonify
import sys
import json

app = Flask(__name__)

@app.route('/')
def index():
    return jsonify(sys.argv[1], sys.argv[2], sys.argv[3])

if __name__ == '__main__':
    app.run(debug=True)
