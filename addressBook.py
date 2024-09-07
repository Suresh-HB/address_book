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
        """
        Description: Function for returning the actual data as per requirement.
        Parameters : 
           None:
        Return: returning a string representation of the contact.
        """
        return (f"Name: {self.first_name} {self.last_name}\n"
                f"Address: {self.address}, {self.city}, {self.state} {self.zip_code}\n"
                f"Phone: {self.phone_number}\n"
                f"Email: {self.email}")

class AddressBook:

    def __init__(self):
        self.address_book = []

    def add_contact(self, contact):
        self.address_book.append(contact)

def main():
    ab = AddressBook()

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

    print("\nAddress Book:")
    for data in ab.address_book:
        print(data)

if __name__ == "__main__":
    main()
