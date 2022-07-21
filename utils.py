import json

def load_candidates_from_json(path) -> list:
    """Загружаем файл json"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        candidates: list[dict] = json.load(file)
        return candidates


def get_candidate_by_id(uid):
    candidates = get_all_candidates()
    for candidate in candidates:
        if candidate['id'] == uid:
            return candidate
    return render_template('card.html')

def get_candidates_by_name(candidate_name):
    candidates = get_all_candidates()
    result_name = []
    for candidate in candidates:
        if candidate_name in candidate['name'].split(','):
            result_name.append(candidate)
    return result_name


def get_candidates_by_skill(skill_name):
    candidates = get_all_candidates()
    result_skill = []
    for candidate in candidates:
        if skill_name in candidate['skills'].split(','):
            result_skill.append(candidate)
    return result_skill


#123

