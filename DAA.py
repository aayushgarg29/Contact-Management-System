import json

class Contact:
    def __init__(self, name, phone):
        self.name = name
        self.phone = phone

    def __str__(self):
        return f"{self.name}: {self.phone}"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, name, phone):
        contact = Contact(name, phone)
        self.contacts.append(contact)
        print(f"Contact {name} added.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted.")
                return
        print("Contact not found.")

    def search_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
        print("Contact not found.")

    def display_contacts(self):
        if self.contacts:
            print("Contacts:")
            for contact in sorted(self.contacts, key=lambda c: c.name):
                print(contact)
        else:
            print("No contacts available.")

    def save_contacts(self, filename):
        with open(filename, 'w') as file:
            json.dump([{'name': contact.name, 'phone': contact.phone} for contact in self.contacts], file)
        print("Contacts saved.")

    def load_contacts(self, filename):
        try:
            with open(filename, 'r') as file:
                contact_list = json.load(file)
                self.contacts = [Contact(c['name'], c['phone']) for c in contact_list]
            print("Contacts loaded.")
        except FileNotFoundError:
            print("No saved contacts found.")

def main():
    contact_book = ContactBook()
    contact_book.load_contacts('contacts.json')

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Search Contact")
        print("4. Display All Contacts")
        print("5. Save Contacts")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == '1':
            name = input("Enter contact name: ")
            phone = input("Enter phone number: ")
            contact_book.add_contact(name, phone)
        elif choice == '2':
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)
        elif choice == '3':
            name = input("Enter contact name to search: ")
            contact_book.search_contact(name)
        elif choice == '4':
            contact_book.display_contacts()
        elif choice == '5':
            contact_book.save_contacts('contacts.json')
        elif choice == '6':
            contact_book.save_contacts('contacts.json')
            print("Exiting the contact book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
