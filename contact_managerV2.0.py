
contacts =[]
def show_menu():
    print("\n=====CONTACT MANAGER=====")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Delete Contact")
    print("5. Edit Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter contact name: ").strip().title()
    if name.lower() in [contact.lower() for contact in contacts]:
        print(f"{name} already exists!")
    else:
        contacts.append(name)
        save_contacts()
        print(f"{name} was successfully added!")

def view_contacts():
    if not contacts:
        print("No contacts found!")
    else:
        print("\nYour Contacts:")
        for index, contact in enumerate(contacts):
            print(f"{index + 1}. {contact}")

def search_contact():
    search_name = input("Enter the name you want to search: ").strip()
    found = False
    for contact in contacts:
        if contact.lower() == search_name.lower():
            print(f"{search_name} found!")
            found = True
            break
    if not found:
        print(f"{search_name} not found!")

def edit_contact():
    edit_name = input("Enter contact to edit: ").strip().lower()
    found = False
    for index, contact in enumerate(contacts):
        if contact.lower() == edit_name:
            new_name = input("Enter new name: ").strip().title()
            # prevent changing to an already-existing contact
            if new_name.lower() in [contact.lower() for contact in contacts] and new_name.lower() != edit_name:
                print("Name already exists")
            else:
                confirm = input(f"Are you sure you want to change {edit_name} to {new_name}? (y/n): ")
                if confirm == "y":
                    contacts[index] = new_name
                    save_contacts()
                    print(f"{edit_name} updated to {new_name}")
                else:
                    print("Edit cancelled")

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
    delete_name = input("Enter contact to delete: ").strip().title()

    if delete_name in contacts:
        confirm = input(f"Are you sure you want to delete {delete_name}? (y/n): ")

        if confirm == "y":
            contacts.remove(delete_name)
            save_contacts()
            print(f"{delete_name} successfully deleted")
        else:
            print("Deletion cancelled")
    else:
        print(f"{delete_name} not found!")
try:
    load_contacts()
except FileNotFoundError:
    contacts = []
while True:
    show_menu()
    try:
        choice = int(input("Choose an option: "))
    except ValueError:
        print("Please enter a valid number from 1 to 6")
        continue
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
        print("Goodbye!")
        break
    else:
        print("Invalid option!")

