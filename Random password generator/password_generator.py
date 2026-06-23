import random
import string
import sys


def generate_password(length: int, include_digits: bool = True, include_special: bool = True) -> str:
    """
    Generates a random, secure password of the specified length.
    
    Ensures that the password contains at least one character from each enabled set:
    - Lowercase letters
    - Uppercase letters
    - Digits (optional)
    - Special characters/punctuation (optional)
    """
    if length < 4:
        raise ValueError("Password length must be at least 4 characters to guarantee character diversity.")

    # Define the character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits if include_digits else ""
    special = string.punctuation if include_special else ""

    # Ensure we have at least some characters to choose from
    all_characters = lowercase + uppercase + digits + special
    if not all_characters:
        raise ValueError("At least one character set must be selected.")

    # Guarantee at least one character from each active category to satisfy complexity requirements
    password_chars = [
        random.choice(lowercase),
        random.choice(uppercase)
    ]
    if include_digits:
        password_chars.append(random.choice(digits))
    if include_special:
        password_chars.append(random.choice(special))

    # Fill the remaining length with random choices from all allowed characters
    remaining_length = length - len(password_chars)
    password_chars.extend(random.choice(all_characters) for _ in range(remaining_length))

    # Shuffle the characters to prevent predictable patterns (e.g., first letter is always lowercase, etc.)
    random.shuffle(password_chars)

    # Join the list into a single string
    return "".join(password_chars)


def main():
    print("=" * 50)
    print("      🔒 SECURE RANDOM PASSWORD GENERATOR 🔒      ")
    print("=" * 50)
    print("This utility generates strong, randomized passwords.")
    print("Designed as an educational tool for Python built-in modules.")
    print("-" * 50)

    # Get password length with input validation
    while True:
        try:
            length_input = input("Enter the desired password length (minimum 8 recommended): ").strip()
            if not length_input:
                print("⚠️ Length cannot be empty. Please enter a number.")
                continue
            
            length = int(length_input)
            if length < 4:
                print("⚠️ For security and diversity, length must be at least 4.")
                continue
            break
        except ValueError:
            print("⚠️ Invalid input. Please enter a valid whole number.")

    # Get options for complexity
    def get_yes_no(prompt: str, default: bool = True) -> bool:
        choice = input(f"{prompt} (y/n, default={ 'y' if default else 'n' }): ").strip().lower()
        if not choice:
            return default
        return choice.startswith('y')

    include_digits = get_yes_no("Include numbers (e.g., 0-9)?")
    include_special = get_yes_no("Include special characters (e.g., !, @, #, $)?")

    try:
        password = generate_password(
            length=length, 
            include_digits=include_digits, 
            include_special=include_special
        )
        
        # Display the result securely
        print("-" * 50)
        print(" Password generated successfully!")
        print(f"Password: \033[1;32m{password}\033[0m")  # Green colored output in supported terminals
        print("-" * 50)
        
        # Educational section explaining how it works
        print("\n💡 Educational Breakdown (How it works):")
        print("1. 'import random' - Used for selecting characters and shuffling the password.")
        print("2. 'import string' - Used to fetch character groups (letters, digits, punctuation).")
        print("3. Guaranteeing Complexity - The code selects at least one character from each requested category")
        print("   first, then fills the rest randomly, and finally shuffles them to ensure high entropy.")
        print("\n🔒 Security Tip: In real-world production systems where cryptographic security is needed,")
        print("   prefer Python's 'secrets' module over 'random', as 'secrets' is cryptographically secure.")
        print("=" * 50)

    except ValueError as e:
        print(f"❌ Error: {e}", file=sys.stderr)


if __name__ == "__main__":
    main()
