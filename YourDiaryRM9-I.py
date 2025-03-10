
import os
from datetime import datetime

Password = "0812"

def authenticate():
    """Authenticate the user with a password."""
    attempt = input("Hi! Welcome to your diary! Please insert your password.")
    return attempt == Password

def create_diary_file():
    """Create the diary.txt file if it does not exist."""
    if not os.path.exists("diary.txt"):
        open("diary.txt", "w").close()

def write_entry():
    """Write a new entry to the diary."""
    entry = input("Write your new entry: ")
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with open("diary.txt", "a") as file:
        file.write(f"[{timestamp}] {entry}\n")
    print("Entry added!\n")

def view_entries():
    """View all diary entries."""
    with open("diary.txt", "r") as file:
        content = file.read()
    print("\n--- Entries ---\n" + (content if content else "No entries found."))

def main():
    """Main function to run the diary application."""
    create_diary_file()

    if not authenticate():
        print("Wrong password, Closing...")
        return

    while True:
        print("\n1. Write Entry")
        print("2. View Entries")
        print("3. Close")
        choice = input("Choose an option: ")

        if choice == "1":
            write_entry()
        elif choice == "2":
            view_entries()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()