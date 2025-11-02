file = "contacts.txt"

def add():
    name = input("name: ")
    phone = input("phone: ")
    email = input("email: ")

    with open(file, "a") as f:
        f.write(f"{name}|{phone}|{email}\n")
    print("contact saved")


def view():
    print("contacts:")
    try:
        with open(file, "r") as f:
            contacts = f.readlines()
            if not contacts:
                print("no contacts found")
            else:
                for i, contact in enumerate(contacts, start=1):
                    name, phone, email = contact.strip().split("|")
                    print(f"{i}. {name} | {phone} | {email}")
        print()
    except FileNotFoundError:
        print("no contacts found.")


def search():
    search = input("enter name to search for: ").lower()
    found = False

    try:
        with open(file, "r") as f:
            for contact in f:
                name, phone, email = contact.strip().split("|")
                if search in name.lower():
                    print(f"found: {name} | {phone} | {email}")
                    found = True
        if not found:
            print("no contact found.")
    except FileNotFoundError:
        print("no contacts found.")


def delete():
    name_to_delete = input("enter name to delete: ").lower()
    updated_contacts = []
    deleted = False

    try:
        with open(file, "r") as f:
            for contact in f:
                name, phone, email = contact.strip().split("|")
                if name.lower() != name_to_delete:
                    updated_contacts.append(contact)
                else:
                    deleted = True

        with open(file, "w") as f:
            f.writelines(updated_contacts)

        if deleted:
            print("contact deleted!")
        else:
            print("contact not found")

    except FileNotFoundError:
        print("no contacts found")


def update():
    name_to_update = input("enter name to update: ").lower()
    updated_contacts = []
    updated = False

    try:
        with open(file, "r") as f:
            for contact in f:
                name, phone, email = contact.strip().split("|")
                if name.lower() == name_to_update:
                    new_name = input("new name: ") 
                    new_phone = input("new phone: ") 
                    new_email = input("new email: ")
                    updated_contacts.append(f"{new_name}|{new_phone}|{new_email}\n")
                    updated = True
                else:
                    updated_contacts.append(contact)

        with open(file, "w") as f:
            f.writelines(updated_contacts)

        if updated:
            print("contact updated")
        else:
            print("contact not found")

    except FileNotFoundError:
        print("no contacts file found")


def main():
    while True:
        print("contact book manager")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Update Contact")
        print("6. Exit")
        choice = input("Choice: ")

        if choice == "1":
            add()
        elif choice == "2":
            view()
        elif choice == "3":
            search()
        elif choice == "4":
            delete()
        elif choice == "5":
            update()
        elif choice == "6":
            print("exit")
            break
        else:
            print("invalid choice")


if __name__ == "__main__":
    main()
