from rich.table import Table
from rich.console import Console

console = Console()

def print_contacts(contacts):
    if not contacts:
        print("No contacts found.")
        return

    table = Table(title="Contacts Manager")
    table.add_column('Id')
    table.add_column('Name')
    table.add_column('Number')

    for contact in contacts:        
        table.add_row(contact['id'],contact['name'],str(contact["number"]))

    console.print(table)
