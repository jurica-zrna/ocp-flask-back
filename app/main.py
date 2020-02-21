import os
import logging
from flask import Flask, render_template
app = Flask(__name__)

logging.basicConfig(level=logging.INFO)

host = os.getenv('HOSTNAME', 'localhost')
title = ("Flask on %s" % host)

db_config = {
  'user': os.getenv('DATABASE_USER', None),
  'password': os.getenv('DATABASE_PASSWORD', None),
  'name': os.getenv('DATABASE_NAME', None),
  'host': os.getenv('DATABASE_HOST', None),
  'port': os.getenv('DATABASE_PORT', None)
}

@app.route('/')
def hello():
    app.logger.info(db_config)
    return render_template('index.html', title=title, host=host, db_config = db_config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
