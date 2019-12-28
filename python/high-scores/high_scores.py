def latest(scores):
	return scores[-1] if len(scores) > 0 else []


def personal_best(scores):
	scores.sort()
	return scores[-1] if len(scores) > 0 else []

def personal_top_three(scores):
	scores.sort()
	result = []
	if len(scores) >= 3:
		result.append(scores[-1])
		result.append(scores[-2])
		result.append(scores[-3])
	elif len(scores) == 2:
		result.append(scores[-1])
		result.append(scores[-2])
	elif len(scores) == 1:
		result.append(scores[-1])
	return result
