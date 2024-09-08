"""

@Author: Suresh
@Date: 08-09-2024
@Last Modified by: Suresh
@Last Modified Date:08-09-2024
@Title : Addressbook.

"""

class Contact:
    def __init__(self, first_name, last_name, address, city, state, zip_code, phone_number, email):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.city = city
        self.state = state
        self.zip_code = zip_code
        self.phone_number = phone_number
        self.email = email

    def __str__(self):
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Address: {self.address}, {self.city}, {self.state} {self.zip_code}\n"
                f"Phone: {self.phone_number}\n"
                f"Email: {self.email}")

class AddressBook:
    def __init__(self):
        self.address_book = []

    def add_contact(self, contact):
        self.address_book.append(contact)

    def find_contact(self, first_name, last_name):
        for contact in self.address_book:
            if contact.first_name == first_name and contact.last_name == last_name:
                return contact
        return None

    def edit_contact(self, first_name, last_name):
        contact = self.find_contact(first_name, last_name)
        if contact is None:
            print("Contact not found.")
            return

        print("Editing contact:")
        contact.first_name = input(f"First Name ({contact.first_name}): ") or contact.first_name
        contact.last_name = input(f"Last Name ({contact.last_name}): ") or contact.last_name
        contact.address = input(f"Address ({contact.address}): ") or contact.address
        contact.city = input(f"City ({contact.city}): ") or contact.city
        contact.state = input(f"State ({contact.state}): ") or contact.state
        contact.zip_code = input(f"Zip Code ({contact.zip_code}): ") or contact.zip_code
        contact.phone_number = input(f"Phone Number ({contact.phone_number}): ") or contact.phone_number
        contact.email = input(f"Email ({contact.email}): ") or contact.email

    def delete_contact(self, first_name, last_name):
        contact = self.find_contact(first_name, last_name)
        if contact is None:
            print("Contact not found.")
            return
        self.address_book.remove(contact)
        print(f"Contact {first_name} {last_name} has been deleted.")

def main():
    ab = AddressBook()

    while True:
        print("\n1. Add Contact")
        print("2. Edit Contact")
        print("3. Delete Contact")
        print("4. View Address Book")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            print("Enter contact details:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            address = input("Address: ")
            city = input("City: ")
            state = input("State: ")
            zip_code = input("Zip Code: ")
            phone_number = input("Phone Number: ")
            email = input("Email: ")

            c = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
            ab.add_contact(c)

        elif choice == "2":
            print("Enter the name of the contact to edit:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")

            ab.edit_contact(first_name, last_name)

        elif choice == "3":
            print("Enter the name of the contact to delete:")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")

            ab.delete_contact(first_name, last_name)

        elif choice == "4":
            print("\nAddress Book:")
            for data in ab.address_book:
                print(data)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
