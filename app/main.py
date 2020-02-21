import os
import logging
from flask import Flask, render_template
from peewee import *
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

db = None

try:
  db = PostgresqlDatabase(
    db_config['name'],
    user=db_config['user'],
    password=db_config['password'],
    host=db_config['host'],
    port=int(db_config['port'])
  )

except:
  db = SqliteDatabase(
    'app.db',
    pragmas={
      'journal_mode': 'wal',
      'cache_size': -1024 * 64
    }
  )

class NumberCollection(Model):
    number = BigIntegerField(unique=True)

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()
db.create_tables([NumberCollection])

@app.route('/')
def hello():
    app.logger.info(db_config)
    return render_template('index.html', title=title, host=host, db_config = db_config)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
