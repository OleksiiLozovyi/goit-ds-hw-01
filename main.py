import pickle

class AddressBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone):
        self.contacts[name] = phone

    def __str__(self):
        return '\n'.join([f'{name}: {phone}' for name, phone in self.contacts.items()])

def save_data(book, filename="addressbook.pkl"):
    with open(filename, "wb") as f:
        pickle.dump(book, f)

def load_data(filename="addressbook.pkl"):
    try:
        with open(filename, "rb") as f:
            return pickle.load(f)
    except FileNotFoundError:
        return AddressBook()

def main():
    book = load_data() 

    while True:
        command = input("Enter command: ").strip().lower()

        if command == "add":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            book.add_contact(name, phone)
        elif command == "all":
            print("Address Book:")
            print(book)
        elif command == "exit":
            save_data(book) 
            print("Data saved. Exiting program.")
            break
        else:
            print("Unknown command, try again.")

if __name__ == "__main__":
    main()