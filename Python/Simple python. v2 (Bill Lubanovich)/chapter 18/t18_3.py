"""
Добавьте функцию home() для обработки запросов к главной странице.
Пусть она возвращает строку It's alive!.
"""
from flask import Flask

app = Flask(__name__)


@app.route('/')
def home():
    return "It's alive!"


app.run(debug=True)
