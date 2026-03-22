from storage import load_contacts, save_contacts
from models import Contact

def add_contact(name, number):
    contacts = load_contacts()
    contact = Contact(name,number)
    contacts.append(contact.to_dict())
    save_contacts(contacts)

def list_contacts():
    contacts = load_contacts()
    return contacts

def update_contacts(id,name,number):
    contacts = load_contacts()
    for contact in contacts:
        if contact["id"] == id:
            contact["name"] = name
            contact["number"] = number
    save_contacts(contacts)

def delete_contact(id):
    contacts = load_contacts()
    for contact in contacts:
        if contact["id"] == id:
            contacts.remove(contact)
    save_contacts(contacts)
    
    







