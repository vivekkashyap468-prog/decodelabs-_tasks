# 🔒 Secure Random Password Generator

A customizable, interactive command-line utility written in Python that generates strong, random passwords. Designed as an educational resource to teach Python built-in libraries, string manipulation, and complexity validation.

---

## ✨ Features

- **Interactive Console Interface**: Prompts the user for length and complexity parameters with validation.
- **Customizable Complexity**: Options to include/exclude digits and special characters.
- **Guaranteed Diversity**: Ensures that generated passwords always contain at least one uppercase letter, one lowercase letter, one digit, and one special character (if enabled).
- **Shuffled Output**: Shuffles final characters to prevent any predictable pattern structures.
- **Educational Explanations**: Demonstrates the use of Python standard libraries directly in the output.
- **Comprehensive Unit Tests**: Includes tests verifying length correctness, character distribution, and input validations.

---

## 🛠️ Key Python Concepts Demonstrated

- **Module Importing**: Imports built-in modules `random` and `string`.
- **String Manipulation**: Combines groups of characters using constants from the `string` module (`ascii_lowercase`, `ascii_uppercase`, `digits`, `punctuation`).
- **Data Validation & Error Handling**: Uses `try-except` blocks to handle invalid user input.

---

## 🚀 Getting Started

### Prerequisites

- Python 3.6 or higher (No third-party packages required).

### Installation

Clone or copy the files to your local environment:
- `password_generator.py` (The main utility)


---

## 📖 Usage

Run the script from your terminal:

```bash
python password_generator.py
```

### Example Interaction

```text
==================================================
      🔒 SECURE RANDOM PASSWORD GENERATOR 🔒      
==================================================
This utility generates strong, randomized passwords.
Designed as an educational tool for Python built-in modules.
--------------------------------------------------
Enter the desired password length (minimum 8 recommended): 12
Include numbers (e.g., 0-9)? (y/n, default=y): y
Include special characters (e.g., !, @, #, $)? (y/n, default=y): y
--------------------------------------------------
🎉 Password generated successfully!
Password: gH7$xP2!mK9q
--------------------------------------------------
```



## 🔒 Security Notice

For production-grade software and cryptographic operations, **do not use** the `random` module because it uses a pseudo-random number generator (PRNG) which can be predictable. Instead, use Python's built-in **`secrets`** module, which is designed to generate cryptographically strong random numbers suitable for managing secrets such as passwords, account authentication, security tokens, and related secrets.
