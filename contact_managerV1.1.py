contacts =["Nestor", "Sarah", "John"]

######ADD CONTACT LOGIC#####
# while True:
#     name = input("Enter contact name: ")
#     if name == "done":
#         break
#     contacts.append(name)
# print("Your Contacts:")

##ADD VIEW CONTACT LOGIC#####
# for index, contact in enumerate(contacts):
#     print(f"{index + 1}. {contact}")
# search_name = input("Enter contact name: ")
# found = False

#######SEARCH CONTACT LOGIC########
# for contact in contacts:
#     if contact == search_name:
#         print(f"{search_name} found!")
#         found = True
#         break
# if not found:
#     print(f"{search_name} not found!")

#######DELETE CONTACT LOGIC########
delete_name = input("Enter contact to delete: ")
if delete_name in contacts:
    contacts.remove(delete_name)
    print(f"{delete_name} successfully deleted")
    print(contacts)

else:
    print(f"{delete_name} not found!")
