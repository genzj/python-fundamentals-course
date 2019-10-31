# -*- coding: utf-8 -*-
from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def get_root():
    return 'Hello World'


@app.route('/calculate', methods=['POST'])
def login():
    a = int(request.form['a'])
    b = int(request.form['b'])
    return '%d + %d = %d' % (a, b, a + b)


if __name__ == '__main__':
    app.run(debug=True)
