"""
@Author: Suresh
@Date: 09-09-2024
@Last Modified by: Suresh
@Last Modified Date: 09-09-2024
@Title: Addressbook with Multiple Books.
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
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)

    def find_contact(self, first_name, last_name):
        for contact in self.contacts:
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
        self.contacts.remove(contact)
        print(f"Contact {first_name} {last_name} has been deleted.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in this address book.")
        for contact in self.contacts:
            print(contact)
            print("*" * 40)

def main():
    address_books = {}

    while True:
        print("\n1. Create New Address Book")
        print("2. Select Address Book")
        print("3. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            name = input("Enter the name for the new address book: ").strip()
            if name in address_books:
                print(f"Address book '{name}' already exists")
                print("            -----------")
            else:
                address_books[name] = AddressBook()
                print(f"Address book '{name}' created.")

        elif choice == "2":
            name = input("Enter the name of the address book to select: ").strip()
            address_book = address_books.get(name, None)

            if address_book is None:
                print("Address book not found.")
                continue

            while True:
                print(f"\nManaging address book '{name}':")
                print("1. Add Contact")
                print("2. Edit Contact")
                print("3. Delete Contact")
                print("4. View Address Book")
                print("5. Go Back to Main Menu")

                sub_choice = input("Choose an option: ")

                if sub_choice == "1":
                    while True:
                        print("Enter contact details:")
                        first_name = input("First Name: ")
                        last_name = input("Last Name: ")
                        address = input("Address: ")
                        city = input("City: ")
                        state = input("State: ")
                        zip_code = input("Zip Code: ")
                        phone_number = input("Phone Number: ")
                        email = input("Email: ")

                        contact = Contact(first_name, last_name, address, city, state, zip_code, phone_number, email)
                        address_book.add_contact(contact)
                        add_more = input("Do you wish to add another contact? (yes/no): ").strip().lower()
                        if add_more != 'yes':
                            break

                elif sub_choice == "2":
                    print("Enter the name of the contact to edit:")
                    first_name = input("First Name: ")
                    last_name = input("Last Name: ")
                    address_book.edit_contact(first_name, last_name)

                elif sub_choice == "3":
                    print("Enter the name of the contact to delete:")
                    first_name = input("First Name: ")
                    last_name = input("Last Name: ")
                    address_book.delete_contact(first_name, last_name)

                elif sub_choice == "4":
                    print("\nAddress Book:")
                    address_book.view_contacts()

                elif sub_choice == "5":
                    break
                
                else:
                    print("Invalid choice. Please choose again.")

        elif choice == "3":
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
