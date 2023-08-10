import random
import string

def generate_password(length, charsets):
    return ''.join(random.choice(charsets) for _ in range(length))

def main():
    print("Password Generator Tool")
    charsets = ''
    charsets += string.ascii_uppercase if input("Include uppercase letters? (y/n): ").lower() == 'y' else ''
    charsets += string.ascii_lowercase if input("Include lowercase letters? (y/n): ").lower() == 'y' else ''
    charsets += string.digits if input("Include numbers? (y/n): ").lower() == 'y' else ''
    charsets += string.punctuation if input("Include special characters? (y/n): ").lower() == 'y' else ''

    if not charsets:
        print("Error: Please select at least one character set for password generation.")
    else:
        length = int(input("Enter the password length: "))
        password = generate_password(length, charsets)
        print("Generated Password:", password)

if __name__ == "__main__":
    main()
