from flask import Flask, render_template
from utils import load_candidates_from_json, get_candidate, get_candidates_by_name, get_candidates_by_skill

app = Flask(__name__)

# Создаем роут и выводим в него список кандидатов

@app.route('/')
def main_page():
    candidates: list[dict]=load_candidates_from_json()
    return render_template('list.html', candidates=candidates)

# Создаем роут для вывода кандидатов по uid

@app.route('/candidate/<int:uid>')
def get_candidate_by_id(uid):
    candidate: dict = get_candidate(idx)
    if not candidate:
            return 'Кандидат не найден'
    render_template('card.html', candidates=candidates)

# Создаем роут для поиска каддата по имени


@app.route('/search/<candidate_name>')
def search_candidates_page(candidate_name):
    candidates: list[dict] = get_candidates_by_name(candidate_name)
    return render_template('search.html, candidates=candidates')

# Создаем роут для поиска каддата по имени


@app.route('/skill/<skill_name>')
def search_candidates_by_skill_page(skill_name):
    candidates: list[dict] = get_candidates_by_skill(skill_name)
    return render_template('skill.html, candidates=candidates')


app.run(host='127.0.0.2', port=8100)