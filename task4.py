from colorama import Fore, Style, init

init(autoreset=True)

def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, args

def add_contact(args, contacts):
    if len(args) != 2:
        return Fore.RED + "Invalid command. Usage: add [name] [phone]"
    name, phone = args
    contacts[name] = phone
    return Fore.BLUE + "Contact added."

def change_contact(args, contacts):
    if len(args) != 2:
        return Fore.RED + "Invalid command. Usage: change [name] [new phone]"
    name, phone = args
    if name in contacts:
        contacts[name] = phone
        return Fore.YELLOW + "Contact updated."
    else:
        return Fore.RED + "Contact not found."

def show_phone(args, contacts):
    if len(args) != 1:
        return Fore.RED + "Invalid command. Usage: phone [name]"
    name = args[0]
    if name in contacts:
        return Fore.MAGENTA + contacts[name]
    else:
        return Fore.RED +  "Contact not found."

def show_all(contacts):
    if not contacts:
        return Fore.RED + "No contacts found."
    return Fore.MAGENTA + "\n".join([f"{name}: {phone}" for name, phone in contacts.items()])

def main():
    contacts = {}
    print("Welcome to the assistant bot!")
    while True:
        user_input = input(Fore.GREEN + "Enter a command: ")
        command, args = parse_input(user_input)

        if command in ["close", "exit"]:
            print(Fore.CYAN +"Good bye!")
            break
        elif command == "hello":
            print(Fore.CYAN + "How can I help you?")
        elif command == "add":
            print(add_contact(args, contacts))
        elif command == "change":
            print(change_contact(args, contacts))
        elif command == "phone":
            print(show_phone(args, contacts))
        elif command == "all":
            print(show_all(contacts))
        else:
            print(Fore.CYAN + "Invalid command.")

if __name__ == "__main__":
    main()
