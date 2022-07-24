import logging

from flask import Flask, request, render_template

# add filemode="w" to overwrite
logging.basicConfig(filename="../basic.log")

app = Flask(__name__)

@app.route('/',)
def page_index():
    return "������� ��������"

@app.route('/store')
def page_store():
    return "�������� �������� "

@app.route('/store/<cat>')
def page_cat(cat):
    return f"�������� ��������� {cat} "

app.run()