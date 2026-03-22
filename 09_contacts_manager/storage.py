import json
import os

CONTACT_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE) as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as f:
        json.dump(contacts, f, indent=2)

