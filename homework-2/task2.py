subjects = {
    'math': {'George': 85, 'Salome': 78, 'David': 92},
    'physics': {'George': 90, 'David': 75, 'Salome': 88},
    'chemistry': {'David': 82, 'George': 80, 'Salome': 91}
}

output = {}


for key, value in subjects.items():
    for student, grade in value.items():
        if student not in output:
            output[student] = {}
        output[student][key] = grade

print(output)