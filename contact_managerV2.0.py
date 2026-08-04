contacts =[]
def show_menu():
    print("\n=====CONTACT MANAGER=====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Edit Contact")
    print("6. Save Contact")
    print("7. Load Contacts")
    print("8. Exit")

def add_contact():
    name = input("Enter contact name: ")
    if name in contacts:
        print(f"{name} already exists!")
    else:
        contacts.append(name)
        print(f"{name} was successfully added!")

def view_contacts():
    if not contacts:
        print("No contacts found!")
    else:
        print("\nYour Contacts:")
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

def edit_contact():
    edit_name = input("Enter contact to edit: ")
    found = False
    for index, contact in enumerate(contacts):
        if contact == edit_name:
            new_name = input("Enter new name: ")
            # prevent changing to an already-existing contact
            if new_name in contacts and new_name != edit_name:
                print("Name already exists")
            else:
                contacts[index] = new_name
                print(f"{edit_name} updated to {new_name}")
            found = True
            break
    if not found:
        print("Not found!")

def save_contacts():
    with open("contacts.txt", "w") as file:
        for contact in contacts:
            file.write(contact + "\n")

def load_contacts():
    with open("contacts.txt", "r") as file:
        for line in file:
            contacts.append(line.strip())

def delete_contact():
    delete_name = input("Enter contact to delete: ")
    if delete_name in contacts:
        contacts.remove(delete_name)
        print(f"{delete_name} successfully deleted")
        print(contacts)
    else:
        print(f"{delete_name} not found!")

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
        edit_contact()
    elif choice == 6:
        save_contacts()
    elif choice == 7:
        load_contacts()
    elif choice == 8:
        print("Goodbye!")
        break
    else:
        print("Invalid option!")

