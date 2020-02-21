import os
from flask import Flask, render_template
app = Flask(__name__)

host = os.getenv('HOSTNAME', 'localhost')
title = ("Flask on %s" % host)

@app.route('/')
def hello():
    return render_template('index.html', title=title, host=host)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)
