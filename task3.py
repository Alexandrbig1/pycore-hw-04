import sys
from pathlib import Path
from colorama import Fore, Style, init

init(autoreset=True)

def print_directory_structure(path, indent=0):
    try:
        for item in path.iterdir():
            if item.is_dir():
                print(f"{' ' * indent}{Fore.CYAN}{item.name}/")
                print_directory_structure(item, indent + 4)
            else:
                print(f"{' ' * indent}{Fore.GREEN}{item.name}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    if len(sys.argv) != 2:
        print("Usage: python task3.py <directory_path>")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"Error: The path {directory_path} does not exist.")
        return

    if not directory_path.is_dir():
        print(f"Error: The path {directory_path} is not a directory.")
        return

    print_directory_structure(directory_path)

if __name__ == "__main__":
    main()