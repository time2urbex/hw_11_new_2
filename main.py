from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/hello/, ")
def page_hello():
    return "Привет"

@app.route("/goodbye/, ")
def page_goodbye():
    return "Пока"

@app.route("/seeyou/, ")
def page_seeyou():
    return "Увидимся"

@app.route("/profile/, ")
def page_profile():
    return "Профиль пользователя"


app.run(host='127.0.0.2', port=8000)
