

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
# search_name = input("Enter the name you want to search: ")
# for contact in contacts:
#     if contact == search_name:
#         print(f"{search_name} found!")
#         found = True
#         break
# if not found:
#     print(f"{search_name} not found!")

#######DELETE CONTACT LOGIC########
# delete_name = input("Enter contact to delete: ")
# if delete_name in contacts:
#     contacts.remove(delete_name)
#     print(f"{delete_name} successfully deleted")
#     print(contacts)
#
# else:
#     print(f"{delete_name} not found!")

contacts =[]
def show_menu():
    print("=====CONTACT MANAGER=====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Exit")

def add_contact():
    name = input("Enter contact name: ")
    contacts.append(name)
    print(f"{name} was successfully added!")

def view_contacts():
    if not contacts:
        print("No contacts found!")
    else:
        for index, contact in enumerate(contacts):
            print(f"{index + 1}. {contact}")

def search_contact():
    search_name = input("Enter the name you want to search: ")
    found = False
    for contact in contacts:
        if contact == search_name:
            print(f"{search_name} found!")
            found = True
            break
    if not found:
        print(f"{search_name} not found!")

def delete_contact():
    delete_name = input("Enter contact to delete: ")
    if delete_name in contacts:
        contacts.remove(delete_name)
        print(f"{delete_name} successfully deleted")
        print(contacts)

while True:
    show_menu()
    choice = int(input("Choose an option: "))

    if choice == 1:
        add_contact()
    elif choice == 2:
        view_contacts()
    elif choice == 3:
        search_contact()
    elif choice == 4:
        delete_contact()
    elif choice == 5:
        print("Goodbye!")
        break
    else:
        print("Invalid option!")


