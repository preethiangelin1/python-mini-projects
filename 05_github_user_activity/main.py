import argparse
import requests
from colorama import Fore, init

init(autoreset=True)

parser = argparse.ArgumentParser(prog="github-useractivity")
parser.add_argument("username", help="GitHub username")
args = parser.parse_args()

username = args.username

url = f"https://api.github.com/users/{username}/events"

try:
    response = requests.get(url, timeout=10)
    if response.status_code == 404:
        print(Fore.RED + f"❌ User {username} not found.")
        exit()

    response.raise_for_status()

    events = response.json()

    if not events:
        print(Fore.YELLOW + "⚠ No recent activity found.")
        exit()

    print(Fore.CYAN + f"\nRecent activity for {args.username}:\n")

    for event in events:
        event_type = event.get("type")

        if event_type == "CreateEvent":
            ref_type = event["payload"].get("ref_type")
            ref = event["payload"].get("ref")
            repo = event["repo"].get("name")
            
            print(f"CreateEvent: Created {ref_type} {ref} in {repo}")

        elif event_type == "PushEvent":
            repo = event["repo"].get("name")
            print(f"PushEvent: Pushed to {repo}")

except requests.exceptions.HTTPError as e:
    print(Fore.RED + f"🌐 HTTP error occurred: {e}")

except requests.exceptions.RequestException as e:
    print(Fore.RED + f"🌐 Network error: {e}")