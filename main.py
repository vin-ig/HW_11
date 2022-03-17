from flask import Flask, render_template
from utils import *

app = Flask(__name__)

candidates = load_candidates('candidates.json')


@app.route('/')
def index():
    """Главная страница"""
    result = {}
    for candidate in candidates:
        result[candidate.get('id')] = candidate.get('name')
    return render_template('index.html', candidates=result)


@app.route('/candidate/<int:uid>')
def candidate(uid):
    """Карточка кандидата"""
    name, position, picture, skills = get_candidate_by_id(candidates, uid)
    return render_template('candidate.html', name=name, position=position, picture=picture, skills=skills)


@app.route('/search_name/<name>')
def search_name(name):
    """Поиск по имени"""
    result = get_candidate_by_name(candidates, name)
    if result:
        return render_template('search_name.html', found_names=result, amount=len(result))
    else:
        return render_template('not_found.html')


@app.route('/search_skill/<skill>')
def search_skill(skill):
    """Поиск по навыкам"""
    result = get_candidate_by_skill(candidates, skill)
    if result:
        return render_template('search_skill.html', found_skills=result, amount=len(result), skill=skill)
    else:
        return render_template('not_found.html')


if __name__ == '__main__':
    app.run()
