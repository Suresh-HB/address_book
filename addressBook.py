"""

@Author: Suresh
@Date: 11-09-2024
@Last Modified by: Suresh
@Last Modified Date:11-09-2024
@Title : Ability to Read/Write the Address Book with Persons Contact as CSV File.

"""

import csv
import json
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

    def to_dict(self):
        return {
            "first_name": self.first_name,
            "last_name": self.last_name,
            "address": self.address,
            "city": self.city,
            "state": self.state,
            "zip_code": self.zip_code,
            "phone_number": self.phone_number,
            "email": self.email
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            first_name=data["first_name"],
            last_name=data["last_name"],
            address=data["address"],
            city=data["city"],
            state=data["state"],
            zip_code=data["zip_code"],
            phone_number=data["phone_number"],
            email=data["email"]
        )

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

    def view_contacts(self, sorted_by=None):
        if not self.contacts:
            print("No contacts in this address book.")
            return
        
        if sorted_by == "name":
            sorted_contacts = sorted(self.contacts, key=lambda c: c.full_name().lower())
        elif sorted_by == "city":
            sorted_contacts = sorted(self.contacts, key=lambda c: c.city.lower())
        elif sorted_by == "state":
            sorted_contacts = sorted(self.contacts, key=lambda c: c.state.lower())
        elif sorted_by == "zip":
            sorted_contacts = sorted(self.contacts, key=lambda c: c.zip_code)
        else:
            sorted_contacts = self.contacts

        for contact in sorted_contacts:
            print(contact)
            print("*" * 40)

    def search_by_city(self, city):
        return self.city_index.get(city.lower(), [])

    def search_by_state(self, state):
        return self.state_index.get(state.lower(), [])

    def to_dict(self):
        return {
            "contacts": [contact.to_dict() for contact in self.contacts]
        }

    @classmethod
    def from_dict(cls, data):
        address_book = cls()
        address_book.contacts = [Contact.from_dict(contact) for contact in data["contacts"]]
        for contact in address_book.contacts:
            address_book.city_index[contact.city.lower()].append(contact)
            address_book.state_index[contact.state.lower()].append(contact)
        return address_book

    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            json.dump(self.to_dict(), file, indent=4)
        print(f"Address book saved to {filename}.")

    def load_from_file(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
        return self.from_dict(data)

    def save_to_csv(self, filename):
        with open(filename, 'w', newline='') as file:
            writer = csv.DictWriter(file, fieldnames=[
                "first_name", "last_name", "address", "city", "state", "zip_code", "phone_number", "email"])
            writer.writeheader()
            for contact in self.contacts:
                writer.writerow(contact.to_dict())
        print(f"Address book saved to CSV file {filename}.")

    @classmethod
    def load_from_csv(cls, filename):
        address_book = cls()
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                contact = Contact.from_dict(row)
                address_book.add_contact(contact)
        return address_book

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
        print("5. Save Address Book to File")
        print("6. Load Address Book from File")
        print("7. Save Address Book to CSV File")
        print("8. Load Address Book from CSV File")
        print("9. Exit")

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
                print("5. View Address Book Sorted by Name")
                print("6. View Address Book Sorted by City")
                print("7. View Address Book Sorted by State")
                print("8. View Address Book Sorted by Zip Code")
                print("9. Go Back to Main Menu")

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
                    print("\nAddress Book Sorted by Name:")
                    address_book.view_contacts(sorted_by="name")

                elif sub_choice == "6":
                    print("\nAddress Book Sorted by City:")
                    address_book.view_contacts(sorted_by="city")

                elif sub_choice == "7":
                    print("\nAddress Book Sorted by State:")
                    address_book.view_contacts(sorted_by="state")

                elif sub_choice == "8":
                    print("\nAddress Book Sorted by Zip Code:")
                    address_book.view_contacts(sorted_by="zip")

                elif sub_choice == "9":
                    break
                
                else:
                    print("Invalid option. Please try again.")

        elif choice == "3":
            search_type = input("Search by city or state? (city/state): ").strip().lower()
            search_value = input("Enter the value to search: ").strip()
            results = search_across_address_books(address_books, search_type, search_value)
            if results:
                print("\nSearch Results:")
                for contact in results:
                    print(contact)
                    print("*" * 40)
            else:
                print("No contacts found.")

        elif choice == "4":
            view_type = input("View by city or state? (city/state): ").strip().lower()
            view_value = input("Enter the value to view: ").strip()
            count = count_by_city_or_state(address_books, view_type, view_value)
            print(f"Total contacts in {view_value}: {count}")

        elif choice == "5":
            name = input("Enter the name of the address book to save: ").strip()
            address_book = address_books.get(name, None)
            if address_book:
                filename = input("Enter the filename to save to (JSON): ").strip()
                address_book.save_to_file(filename)
            else:
                print("Address book not found.")

        elif choice == "6":
            name = input("Enter the name of the address book to load: ").strip()
            filename = input("Enter the filename to load from (JSON): ").strip()
            try:
                address_books[name] = AddressBook().load_from_file(filename)
                print(f"Address book '{name}' loaded from {filename}.")
            except FileNotFoundError:
                print("File not found.")
            except json.JSONDecodeError:
                print("Error decoding JSON from file.")

        elif choice == "7":
            name = input("Enter the name of the address book to save: ").strip()
            address_book = address_books.get(name, None)
            if address_book:
                filename = input("Enter the filename to save to (CSV): ").strip()
                address_book.save_to_csv(filename)
            else:
                print("Address book not found.")

        elif choice == "8":
            name = input("Enter the name of the address book to load: ").strip()
            filename = input("Enter the filename to load from (CSV): ").strip()
            try:
                address_books[name] = AddressBook.load_from_csv(filename)
                print(f"Address book '{name}' loaded from {filename}.")
            except FileNotFoundError:
                print("File not found.")
            except csv.Error:
                print("Error reading CSV file.")

        elif choice == "9":
            print("Exiting program.")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
