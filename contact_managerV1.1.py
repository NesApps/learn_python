contacts =["Nestor", "Sarah", "John"]
# while True:
#     name = input("Enter contact name: ")
#     if name == "done":
#         break
#     contacts.append(name)
# print("Your Contacts:")
# #Adding the view contacts logic
# for index, contact in enumerate(contacts):
#     print(f"{index + 1}. {contact}")
search_name = input("Enter contact name: ")
found = False

for contact in contacts:
    if contact == search_name:
        print(f"{search_name} found!")
        found = True
        break
if not found:
    print(f"{search_name} not found!")