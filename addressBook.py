"""

@Author: Suresh
@Date: 07-09-2024
@Last Modified by: Suresh
@Last Modified Date:07-09-2024
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


class AddressBook:

    def __init__(self):
        self.address_book = []


def main():
    ab = AddressBook()

if __name__ == "__main__":
    main()
