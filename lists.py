# courses = ['History', 'Biology', 'Maths', 'Physics', 'CompSci']
# courses2 =['Arts', 'Education']
# courses.extend(courses2)
# courses.remove('Maths')
# popped = courses.pop()
# print(popped)
# courses.reverse()
# courses.sort()
# nums = [1,5,3,4,6,2]
# nums.sort(reverse=True)
# courses.sort(reverse=True)
# sorted_course = sorted(courses)
# print(sorted_course)
# print(sum(nums))
# print(courses.index('CompSci'))
# for item in courses:
#     print(item)
# for index, item in enumerate(courses, start=1):
#     print(index, item)
# course_str = ', '.join(courses)
# new_list = course_str.split(' - ')
# print(course_str)
# print(new_list)

         # TUPLES - this is immutable why lists are mutable
         # SETS - this does not care about order, and it's used to remove duplicate values
cs_courses = {'History', 'Maths', 'Physics', 'CompSci'}
art_courses = {'History', 'Maths', 'Art', 'Design'}

# print('Maths' in cs_courses)
print(cs_courses.intersection(art_courses))
print(cs_courses.difference(art_courses))
print(cs_courses.union(art_courses))