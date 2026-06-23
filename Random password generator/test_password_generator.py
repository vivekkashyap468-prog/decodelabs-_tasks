import unittest
import string
from password_generator import generate_password

class TestPasswordGenerator(unittest.TestCase):
    def test_length(self):
        # Verify length requested matches generated password length
        for length in [4, 8, 16, 32]:
            password = generate_password(length)
            self.assertEqual(len(password), length)

    def test_guaranteed_characters(self):
        # Verify that when options are enabled, at least one character from each set is included
        password = generate_password(10, include_digits=True, include_special=True)
        
        has_lower = any(c in string.ascii_lowercase for c in password)
        has_upper = any(c in string.ascii_uppercase for c in password)
        has_digit = any(c in string.digits for c in password)
        has_special = any(c in string.punctuation for c in password)
        
        self.assertTrue(has_lower, "Must contain at least one lowercase letter")
        self.assertTrue(has_upper, "Must contain at least one uppercase letter")
        self.assertTrue(has_digit, "Must contain at least one digit")
        self.assertTrue(has_special, "Must contain at least one special character")

    def test_exclude_digits_and_special(self):
        password = generate_password(20, include_digits=False, include_special=False)
        
        has_digit = any(c in string.digits for c in password)
        has_special = any(c in string.punctuation for c in password)
        
        self.assertFalse(has_digit, "Should not contain digits")
        self.assertFalse(has_special, "Should not contain special characters")

    def test_invalid_length(self):
        with self.assertRaises(ValueError):
            generate_password(3)

if __name__ == "__main__":
    unittest.main()
