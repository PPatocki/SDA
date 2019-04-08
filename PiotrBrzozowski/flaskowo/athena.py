#!flask/bin/python
from flask import Flask
from flask import render_template
import sys
import json

f = open(sys.argv[1], "r")
data = json.loads(f.read())



#app = Flask(sys.argv[2])
app = Flask(data["app_name"])

@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True, port=data["port"])


# sys.argv to sys oznacza podpiecie do linii polecien a argv to podawanie argumentow przy odpalaniu
