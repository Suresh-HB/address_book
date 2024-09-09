"""

@Author: Suresh
@Date: 08-09-2024
@Last Modified by: Suresh
@Last Modified Date:08-09-2024
@Title : Ability to get number of contact persons count by City or State.

"""


from collections import defaultdict

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

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

class AddressBook:
    def __init__(self):
        self.contacts = []
        self.city_index = defaultdict(list)
        self.state_index = defaultdict(list)

    def add_contact(self, contact):
        if self.find_contact(contact.first_name, contact.last_name):
            print(f"Contact {contact.full_name()} already exists.")
            return
        self.contacts.append(contact)
        self.city_index[contact.city.lower()].append(contact)
        self.state_index[contact.state.lower()].append(contact)
        print(f"Contact {contact.full_name()} added.")

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
        contact.first_name = input(f"First Name ({contact.first_name}): ")
        contact.last_name = input(f"Last Name ({contact.last_name}): ")
        contact.address = input(f"Address ({contact.address}): ") 
        contact.city = input(f"City ({contact.city}): ") 
        contact.state = input(f"State ({contact.state}): ") 
        contact.zip_code = input(f"Zip Code ({contact.zip_code}): ") 
        contact.phone_number = input(f"Phone Number ({contact.phone_number}): ") 
        contact.email = input(f"Email ({contact.email}): ") 

    def delete_contact(self, first_name, last_name):
        contact = self.find_contact(first_name, last_name)
        if contact is None:
            print("Contact not found.")
            return
        self.contacts.remove(contact)
        self.city_index[contact.city.lower()].remove(contact)
        self.state_index[contact.state.lower()].remove(contact)
        print(f"Contact {first_name} {last_name} has been deleted.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts in this address book.")
        for contact in self.contacts:
            print(contact)
            print("*" * 40)

    def search_by_city(self, city):
        return self.city_index.get(city.lower(), [])

    def search_by_state(self, state):
        return self.state_index.get(state.lower(), [])

def search_across_address_books(address_books, search_type, search_value):
    results = []
    for name, address_book in address_books.items():
        if search_type == "city":
            results.extend(address_book.search_by_city(search_value))
        elif search_type == "state":
            results.extend(address_book.search_by_state(search_value))
    return results

def count_by_city_or_state(address_books, view_type, view_value):
    count = 0
    for address_book in address_books.values():
        if view_type == "city":
            count += len(address_book.search_by_city(view_value))
        elif view_type == "state":
            count += len(address_book.search_by_state(view_value))
    return count

def main():
    address_books = {}

    while True:
        print("\n1. Create New Address Book")
        print("2. Select Address Book")
        print("3. Search Across Address Books")
        print("4. View Persons by City or State")
        print("5. Exit")

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
            print("\nSearch Across All Address Books")
            search_type = input("Search by (city/state): ").strip().lower()
            search_value = input(f"Enter the {search_type} to search for: ").strip()

            if search_type not in ["city", "state"]:
                print("Invalid search type. Please choose 'city' or 'state'.")
                continue

            results = search_across_address_books(address_books, search_type, search_value)

            count = count_by_city_or_state(address_books, search_type, search_value)

            if not results:
                print(f"No contacts found in {search_value}.")
            else:
                print(f"\nContacts in {search_value} ({count} found):")
                for contact in results:
                    print(contact)
                    print("*" * 60)

        elif choice == "4":
            print("\nView Persons by City or State Across All Address Books")
            view_type = input("View by (city/state): ").strip().lower()
            view_value = input(f"Enter the {view_type} to view: ").strip()

            if view_type not in ["city", "state"]:
                print("Invalid view type. Please choose 'city' or 'state'.")
                continue

            results = search_across_address_books(address_books, view_type, view_value)

            count = count_by_city_or_state(address_books, view_type, view_value)

            if not results:
                print(f"No contacts found in {view_value}.")
            else:
                print(f"\nContacts in {view_value} ({count} found):")
                for contact in results:
                    print(contact)
                    print("*" * 60)

        elif choice == "5":
            break

        else:
            print("Invalid choice. Please choose again.")

if __name__ == "__main__":
    main()
