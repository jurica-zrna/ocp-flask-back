import os
from flask import Flask, render_template
app = Flask(__name__)

host = os.getenv('HOSTNAME', 'localhost')
title = ("Flask on %s" % host)

db_config = {
  'user': os.getenv('databse-user', None),
  'password': os.getenv('databse-password', None),
  'name': os.getenv('databse-name', None),
  'host': os.getenv('databse-host', None),
  'port': os.getenv('databse-port', None)
}

print(db_config)

@app.route('/')
def hello():
    return render_template('index.html', title=title, host=host, db_config = db_config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
