from user import User

if __name__ == "__main__":
    alice = User("Alice")
    bob = User("Bob")
    charlie = User("Charlie")

    alice.follow(bob)
    alice.follow(charlie)
    bob.follow(alice)

    alice.send_message("Hello world!", "10:00 AM")
    bob.send_message("Learning OOP!", "10:30 AM")

    print(f"{alice.name} is following:")
    for u in alice.following:
        print(f"  - {u.name}")

    print(f"{bob.name}'s followers:")
    for u in bob.followers:
        print(f"  - {u.name}")

    print(f"{alice.name}'s messages:")
    for m in alice.messages:
        print(f"  [{m.timestamp}] {m.content}")