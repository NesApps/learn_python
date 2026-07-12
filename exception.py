from logging import exception

x=input("Enter a number1: ")
y=input("Enter a number2: ")
try:
    z=int(x) / int(y)
except Exception as e:
    print('exception occurred: ', e)
    z=None
print("Division is: ", z)

# Handling exception is like this
# try:
#     while road_is_clear():
#         drive()
# except Accident  as e:
#     take_detour()