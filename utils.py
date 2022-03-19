import json


def load_candidates(path: str) -> list:
	"""Загружает список кандидатов из json-файла"""
	with open(path, encoding='utf-8') as file:
		return json.load(file)


def get_candidate_by_id(candidates: list, uid: int) -> tuple | None:
	"""Ищет кандидата по ID"""
	for candidate in candidates:
		if uid == candidate.get('id'):
			return candidate.get('name'),\
					candidate.get('position'),\
					candidate.get('picture'),\
					candidate.get('skills')

	return None  # Если кандидат не найден


def get_candidate_by_name(candidates: list, name: str) -> list | None:
	"""Ищет кандидата по имени"""
	result = []
	for candidate in candidates:
		if name.lower() in candidate.get('name').lower():
			result.append({candidate.get('id'): candidate.get('name')})
	# Проверяем, найдены ли кандидаты
	if len(result) != 0:
		return result
	else:
		return None


def get_candidate_by_skill(candidates: list, skill: str) -> list | None:
	"""Ищет кандидата по навыкам"""
	result = []
	for candidate in candidates:
		skills = [elem.lower() for elem in candidate.get('skills').split(', ')]
		if skill.lower() in skills:
			result.append({'id': candidate.get('id'), 'name': candidate.get('name')})
	# Проверяем, найдены ли кандидаты
	if len(result) != 0:
		return result
	else:
		return None
