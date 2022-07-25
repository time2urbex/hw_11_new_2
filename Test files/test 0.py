from flask import Flask

app = Flask(__name__)

@app.route('/',)
def page_index():
    print("Главная страница запрошена")
    return "Главная страница"

@app.route('/store')
def page_store():
    print("Страница магазина запрошена")
    return "Страница магазина "

@app.route('/store/<cat>')
def page_cat(cat):
    print(f"Страница категории {cat} запрошена")
    return f"Страница категории {cat} "

app.run(port=4000)