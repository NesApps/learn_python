# language = 'Java'
# if language == 'Python':
#     print('Language is Python')
# elif language == 'Java':
#     print('Language is Java')
# elif language == 'JavaScript':
#     print('Language is JavaScript')
# else:
#     print("No match")

# user = 'Admin'
# logged_in = False
# if not logged_in:
#     print('Please log in')
# else:
#     print("Welcome")

a = [1,2,3]
b = a

print(id(a))
print(id(b))
print(id(a) == id(b))