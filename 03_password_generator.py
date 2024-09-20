import random
import string

# Function to generate a password
def generate_password(length):
    if length < 4:
        print("Password length should be at least 4 characters.")
        return None
    
    # Define the character sets for the password
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    symbols = string.punctuation

    # Ensure password contains at least one character from each character set
    all_characters = lowercase + uppercase + digits + symbols
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(symbols)
    ]

    # Fill the remaining characters randomly
    password += random.choices(all_characters, k=length - 4)

    # Shuffle the password to ensure randomness
    random.shuffle(password)

    # Join the list into a string and return
    return ''.join(password)

# Prompt user for the length of the password
try:
    length = int(input("Enter the desired length for the password: "))
    generated_password = generate_password(length)
    
    if generated_password:
        print("Generated Password:", generated_password)
except ValueError:
    print("Please enter a valid number.")