# Contact-Management-System

The Contact Book Application is a simple command-line program written in Python that allows users to manage their contacts efficiently. Users can add, delete, search for, and display contacts. The application also supports saving contacts to a JSON file for persistent storage and loading them back into the program.

Features
Add Contacts: Users can input a contact name and phone number to create a new contact entry.
Delete Contacts: Users can remove a contact by providing the contact's name.
Search Contacts: The application allows users to search for a specific contact by name and displays the contact’s details if found.
Display All Contacts: Users can view all stored contacts in alphabetical order.
Save Contacts: Contacts can be saved to a JSON file, ensuring that data is preserved between sessions.
Load Contacts: On starting the application, contacts can be loaded from a JSON file, making it easy to continue where the user left off.

Classes and Methods
Contact Class:

Represents a single contact with attributes for the name and phone number.
The __str__ method provides a string representation of the contact for easy display.
ContactBook Class:

Manages a list of Contact objects.
Methods include:
add_contact(name, phone): Adds a new contact.
delete_contact(name): Deletes an existing contact by name.
search_contact(name): Searches for a contact and prints their details.
display_contacts(): Displays all contacts sorted by name.
save_contacts(filename): Saves contacts to a specified JSON file.
load_contacts(filename): Loads contacts from a specified JSON file.
Main Function:

Initializes a ContactBook instance and loads existing contacts from contacts.json.
Presents a menu to the user with options to interact with the contact book.
Continuously prompts the user for input until they choose to exit.

Conclusion
This Contact Book Application provides a simple yet effective way for users to manage their contacts through a command-line interface. Its use of JSON for data storage allows for easy data management and persistence, making it a practical tool for anyone needing to organize contact information.
