student = {'name': 'John', 'age': 25, 'courses': ['math', 'CompSci']}

# student.update({'name': 'jane', 'age': 26, 'phone': '555-5555'})
# del student['age']
# age = student.pop('age')
# print(age)
# print(student)
# print(student.get('phone', 'Not Found '))
for k,v in student.items():
    print(k,v)
# print(student.items())