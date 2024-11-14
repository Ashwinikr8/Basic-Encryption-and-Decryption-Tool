def encrypt(text, key):
    """
    Encrypts the input text using a simple substitution method.
    :param text: The text to be encrypted.
    :param key: A numeric key for shifting characters.
    :return: The encrypted text.
    """
    encrypted = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            base = ord('A') if char.isupper() else ord('a')
            encrypted += chr((ord(char) - base + key) % 26 + base)
        else:
            encrypted += char  # Non-alphabet characters remain unchanged
    return encrypted


def decrypt(text, key):
    """
    Decrypts the input text using a simple substitution method.
    :param text: The text to be decrypted.
    :param key: A numeric key for shifting characters.
    :return: The decrypted text.
    """
    return encrypt(text, -key)  # Reverse the shift for decryption


def main():
    print("Welcome to the Basic Encryption and Decryption Tool!")
    while True:
        print("\nChoose an option:")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Quit")
        choice = input("Enter your choice (1/2/3): ").strip()

        if choice == '3':
            print("Goodbye!")
            break
        elif choice not in ('1', '2'):
            print("Invalid choice. Please try again.")
            continue

        message = input("Enter your message: ")
        try:
            key = int(input("Enter the numeric key (a positive number): "))
        except ValueError:
            print("Invalid key. Please enter a valid number.")
            continue

        if choice == '1':
            result = encrypt(message, key)
            print(f"Encrypted Message: {result}")
        elif choice == '2':
            result = decrypt(message, key)
            print(f"Decrypted Message: {result}")


if __name__ == "__main__":
    main()
