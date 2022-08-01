import json

def load_candidates_from_json() -> list[dict]:
    """Загружаем файл json"""
    with open('candidates.json', 'r', encoding='utf-8') as file:
        return json.load(file)



def get_candidate(candidate_id: int) -> dict:
    """перебираем кандидатов по id"""
    for candidate in load_candidates_from_json():
        if candidate['id'] == candidate_id:
            return candidate


def get_candidates_by_name(candidate_name: str) -> list[dict]:
    """Перебираем кандидатов по имени"""
    result = []
    for candidate in load_candidates_from_json():
        if candidate['name'] == candidate_name:
            result.append(candidate)
    return result


def get_candidates_by_skill(skill_name: str) -> list[dict]:
    """Перебираем кандидатов по скиллу"""
    result = []
    for candidate in load_candidates_from_json():
        if skill_name in candidate['skills'].lower():
            result.append(candidate)
    return result

