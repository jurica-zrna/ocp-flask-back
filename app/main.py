import os
from flask import Flask
app = Flask(__name__)

host = os.getenv('HOSTNAME', 'localhost')

@app.route('/')
def hello():
    return ("Hello World! I'm %s" % host)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
