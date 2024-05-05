import secrets
import string

passwords = {}

def generate_password(length=12):
    """Generate a random password"""
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

def save_password(keyword, username, password):
    """Save keyword, username, and password"""
    passwords[keyword] = {'username': username, 'password': password}

def add_password():
    """Add a new password"""
    keyword = input("Enter keyword: ")
    username = input("Enter username: ")
    password = input("Enter password (press Enter to generate a random password): ")
    
    if not password:
        password = generate_password()
        print(f"Generated password: {password}")
    
    save_password(keyword, username, password)
    print("Password saved successfully!")

def display_password(keyword):
    """Display username and password for a given keyword"""
    if keyword in passwords:
        username = passwords[keyword]['username']
        password = passwords[keyword]['password']
        print(f"Username: {username}")
        print(f"Password: {password}")
    else:
        print(f"Keyword '{keyword}' not found.")

def main():
    while True:
        print("\n1. Add a new password")
        print("2. Display a password")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_password()

        elif choice == '2':
            keyword = input("Enter keyword: ")
            display_password(keyword)

        elif choice == '3':
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()
