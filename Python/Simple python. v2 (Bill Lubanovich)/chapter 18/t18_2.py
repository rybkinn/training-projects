"""
Создайте скелет сайта с помощью веб-сервера Flask.
Убедитесь, что сервер начинает свою работу по адресу Localhost на
стандартном порте 5000. Если ваш компьютер уже использует этот порт
для чего-то еще, то воспользуйтесь другим портом.
"""
from flask import Flask

app = Flask(__name__)

app.run(debug=True)
