import json

def load_candidates_from_json(path):
    """Возвращает всех кандидатов"""
    with open(path, 'r', encoding="utf-8") as file:
        data = json.load(file)
        return data


def get_all_candidates():
    candidates = load_candidates_from_json()
    return candidates

def get_candidate(candidate_id):
    """Возвращает одного кандидата по id"""
    candidates = load_candidates_from_json()
    for candidate in candidates:
        if get_candidate("id") == candidate_id:
            return candidate

def get_candidate_by_name(candidate_name):
    """Возвращает одного кандидата по имени"""
    candidates = load_candidates_from_json()
    candidates_found = []

    for candidate in candidates:
        if candidate_name.lower() in candidate.get("name").lower():
            return candidates_found.append(candidate)

def get_candidates_by_skill(skill_name):
    """Возвращает скилл одного кандидата"""
    skill_name = skill_name.lower()
    candidates = load_candidates_from_json()
    candidates_found = []

    for candidate in candidates:
        skills = candidate.get("skills")
        list_of_skills = skills.lower().split(", ")
        if skill_name in list_of_skills:
            candidates_found.append(candidate)
    return candidates_found
