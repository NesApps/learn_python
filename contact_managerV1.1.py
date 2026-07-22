contacts =[]
while True:
    name = input("Enter contact name: ")
    if name == "done":
        break
    contacts.append(name)
    print(contacts)
#Adding the view contacts logic
    for index, contact in enumerate(contacts):
        print(index + 1, contact)