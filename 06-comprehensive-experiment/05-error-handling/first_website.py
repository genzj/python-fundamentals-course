# -*- coding: utf-8 -*-
from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/')
def get_root():
    return render_template('main.html')


@app.route('/calculate', methods=['POST'])
def login():
    try:
        a = int(request.form['a'])
        b = int(request.form['b'])
    except ValueError:
        return render_template(
            'main.html',
            error='invalid equation "%s + %s"' % (request.form.get('a'), request.form.get('b'))
        )
    else:
        return render_template(
            'main.html',
            equation={
                'a': a,
                'b': b,
                'answer': a + b,
            }
        )


if __name__ == '__main__':
    app.run(debug=True)
