import sys
import random
import os
import logging
from flask import Flask, render_template
from flask_restful import Resource, Api
import peewee as pw
app = Flask(__name__)
api = Api(app)


logging.basicConfig(level=logging.INFO)

host = os.getenv('HOSTNAME', 'localhost')
title = ("Flask on %s" % host)

db_config = {
  'user': os.getenv('DATABASE_USER', None),
  'password': os.getenv('DATABASE_PASSWORD', None),
  'name': os.getenv('DATABASE_NAME', 'numbers.db'),
  'host': os.getenv('DATABASE_HOST', 'localhost'),
  'port': os.getenv('DATABASE_PORT', None)
}

db = None

try:
  db = pw.PostgresqlDatabase(
    db_config['name'],
    user=db_config['user'],
    password=db_config['password'],
    host=db_config['host'],
    port=int(db_config['port'])
  )

except:
  db = pw.SqliteDatabase(
    db_config['name'],
    pragmas={
      'journal_mode': 'wal',
      'cache_size': -1024 * 64
    }
  )

class NumberCollection(pw.Model):
    number = pw.BigIntegerField(unique=True)

    class Meta:
        database = db # This model uses the "people.db" database.

db.connect()
db.create_tables([NumberCollection])

api = Api(app)

app.logger.info(db_config)

class Number(Resource):
  def get(self, num):
    nums = []
    query = NumberCollection.select().order_by(pw.fn.Random()).limit(num).dicts()
    for row in query:
      nums.append(row)
    return {'numbers': nums, 'host': host}

  def put(self, num):
    nums = 0;
    for i in range(0,num):
      try:
        NumberCollection.insert(number = random.randint(0,sys.maxsize)).execute()
        nums = nums + 1;
      except:
        pass
    return {'numbers': nums, 'host': host}

api.add_resource(Number, '/api/num/<int:num>')

@app.route('/')
def index():
    return render_template('index.html', title=title, host=host, db_config = db_config, count = NumberCollection.select().count())

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
