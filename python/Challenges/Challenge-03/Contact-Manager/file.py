# contact manager 

#create a contact storage
contacts = []

#add contact 
def add_contact(name, phone, email,City):
    contact = {"name": name, "phone": phone, "email": email,"city":City}
    contacts.append(contact)

#create menu system
def Menu_System():
    print("Contact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Update Contacts")
    print("5. Delete Contacts")
    print("6. Exit")
    
input_choice=input("Enter your choice: ")
while input_choice != "6":
    if input_choice == "1":
        name = input("Enter name: ")
        try:
            if name=="":
                raise ValueError("Name cannot be empty.")
        except ValueError as e:
                print(e)
                continue
        phone = input("Enter phone: ")
        email = input("Enter email: ")
        city = input("Enter city: ")
        add_contact(name, phone, email,city)
    elif input_choice == "2":
        for contact in contacts:
            print(contact)
    elif input_choice == "3":
        search_name = input("Enter name to search: ")
        for contact in contacts:
            if contact["name"] == search_name:
                print(contact)
    elif input_choice == "4":
        update_name = input("Enter name to update: ")
        for contact in contacts:
            if contact["name"] == update_name:
                new_phone = input("Enter new phone: ")
                new_email = input("Enter new email: ")
                new_city = input("Enter new city: ")
                contact["phone"] = new_phone
                contact["email"] = new_email
                contact["city"] = new_city
    elif input_choice == "5":
        delete_name = input("Enter name to delete: ")
        for contact in contacts:
            if contact["name"] == delete_name:
                contacts.remove(contact)
    else:
        print("Invalid choice. Please try again.")
    
    Menu_System()
