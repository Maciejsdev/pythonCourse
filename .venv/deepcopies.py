from copy import deepcopy

info = {
    'name': 'Maciej',
    'is_Student':True
}

info_copy = info.copy()

info_copy['math_score'] = 91

print(info_copy)
print(info)

teacher_info = {
    'name': 'Bogdan',
    'is_instructor':True,
    'reviews': []
}
teacher_info_deepcopy = deepcopy(teacher_info)
teacher_info_deepcopy['reviews'].append('Great course')
teacher_info['reviews'].append('Thanks')

print(teacher_info)
print(teacher_info_deepcopy)

print(id(teacher_info['reviews']), id(teacher_info_deepcopy['reviews']))

