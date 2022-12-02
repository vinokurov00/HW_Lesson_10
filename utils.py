import json


def load_candidates() -> list[dict]:
    with open("candidates.json", 'r', encoding='utf-8') as file:
        return json.load(file)


def format_candidates(candidates: list[dict]) -> str:
    result = '<pre>'

    for candidate in candidates:
        result += f"""
                {candidate["name"]}\n
                {candidate["position"]}\n
                {candidate["skills"]}\n        
        """
    result += '</pre>'

    return result




def get_all():
    """
    покажет всех кандидатов
    """
    return load_candidates()



def get_by_pk(pk):
    """
    :param pk:
    :return: вернет кандидата по pk
    """
    for candidate in load_candidates():
        if candidate["pk"] == pk:
            return candidate

    return 'Not found'

def get_by_skill(skill_name):
    """
    :param skill_name:
    :return:вернет кандидатов по навыку
    """
    result = []
    for candidate in load_candidates():
        skills = candidate['skills'].lower().split(', ')
        if skill_name in skills:
            result.append(candidate)

    return result

