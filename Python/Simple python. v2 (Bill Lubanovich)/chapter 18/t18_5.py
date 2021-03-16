"""
Модифицируйте функцию home() вашего сервера,
чтобы она использовала шаблон home.html.
Передайте ей три параметра для команды GET: thing, height и color.
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def home():
    kwargs = {'thing': request.args.get('thing'),
              'height': request.args.get('height'),
              'color': request.args.get('color')}
    return render_template('home.html', **kwargs)


app.run(debug=True)
