import argparse
from service import add_contact,list_contacts,update_contacts,delete_contact
from utils import print_contacts


parser = argparse.ArgumentParser(prog="contacts-cli")

subparsers = parser.add_subparsers(dest="command")

add_parser = subparsers.add_parser("add", help="Add a contact name")
add_parser.add_argument("name", help="contact name")
add_parser.add_argument("number", help="contact number")

list_parser = subparsers.add_parser("list", help="list all tasks")

update_parser = subparsers.add_parser("update",  help="Update a task")
update_parser.add_argument("id", help="Id of the contact to be updated")
update_parser.add_argument("name", help="name of the contact to be updated")
update_parser.add_argument("number", help="number of the contact to be updated")

delete_parser = subparsers.add_parser("delete",  help="Delete a task")
delete_parser.add_argument("id", help="Id of the contact to be deleted")

args = parser.parse_args()

if args.command == "add":
    add_contact(args.name, args.number)

elif args.command == "list":
    contacts = list_contacts()
    print_contacts(contacts)

elif args.command == "update":
    update_contacts(args.id,args.name,args.number)

elif args.command == "delete":
    delete_contact(args.id)



