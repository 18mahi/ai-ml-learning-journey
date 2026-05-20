# contact manager system using python

#create a contact storage
contacts = []

#add contact function
def add_contact(name, phone, email,City):
    contact = {"name": name, "phone": phone, "email": email,"city":City}
    contacts.append(contact)
    
#view contacts function
def view_contact():
    if contacts == []:
        print("No contacts found.")
    for contact in sorted_contacts:
        print("-" * 10+"Saved Contacts"+"-" * 10)
        print(f"Name: {contact['name']}")
        print(f"Phone: {contact['phone']}")
        print(f"Email: {contact['email']}")
        print(f"City: {contact['city']}")
        print("-" * 20)

#search contact function
def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            return contact
    return None

#create menu system
def Menu_System():
    print("Contact Manager")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contacts")
    print("4. Update Contacts")
    print("5. Delete Contacts")
    print("6. Favourite Contacts")
    print("7. Exit")
    
    input_choice=input("Enter your choice: ")
    while input_choice != "6":
        #add contact option
        if input_choice == "1":
            duplicate=False
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
            # Check for duplicate contact
            for contact in contacts:
                if contact["name"] == name:
                    print("Contact with this name already exists.")
                    duplicate = True
                    break
            if not duplicate:
                add_contact(name, phone, email,city)
            
        #view contacts list
        elif input_choice == "2":
            sorted_contacts = sorted(contacts, key=lambda x: x["name"].lower())
            view_contact()
            print(f'Total contacts: {len(contacts)}')
            
        #search contact 
        elif input_choice == "3":
            search_name = input("Enter name to search: ")
            contact = search_contact(search_name)
            if contact:
                print(contact)
            else:
                print("Contact not found.")
                    
        #update contact
        elif input_choice == "4":
            update_name = input("Enter name to update: ")
            contact = search_contact(update_name)
            if contact:
                new_phone = input("Enter new phone: ")
                new_email = input("Enter new email: ")
                new_city = input("Enter new city: ")
                contact["phone"] = new_phone
                contact["email"] = new_email
                contact["city"] = new_city
            else:
                print("Contact not found.")
                
        #delete contact
        elif input_choice == "5":
            delete_name = input("Enter name to delete: ")
            contact = search_contact(delete_name)
            if contact:
                contacts.remove(contact)
                print("Contact deleted successfully.")
            else:
                print("Contact not found.")
        elif input_choice == "6":
            favourite_contacts=[]
            fav_name = input("Enter name to add to favourite contacts: ")
            for contact in contacts:
                if contact["name"] == fav_name:
                    favourite_contacts.append(contact)
                    print("Contact added to favourites.")
                    break
            else:
                print("Contact not found.")
        else:
            print("Thank you for using Contact Manager!")
    
Menu_System()
