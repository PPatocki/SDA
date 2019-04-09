#!flask/bin/python
from flask import Flask

app = Flask(__name__) 
@app.route('/')
def index():
    return "Flask example docker!"

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

