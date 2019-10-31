# -*- coding: utf-8 -*-
from flask import Flask

app = Flask(__name__)


@app.route('/')
def get_root():
    return 'Hello World'


if __name__ == '__main__':
    app.run(debug=True)
