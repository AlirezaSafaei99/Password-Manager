import random
from alphabet import letters, symbols, numbers
import pyperclip

class PasswordGenerator:
    def generate(self):
        """
        Generates a secure password using random letters, symbols, and numbers.
        Returns:
            str: A shuffled, secure password.
        """
        nr_letters = random.randint(8, 10)
        nr_symbols = random.randint(2, 4)
        nr_numbers = random.randint(2, 4)

        password_list = (
            [random.choice(letters) for _ in range(nr_letters)] +
            [random.choice(symbols) for _ in range(nr_symbols)] +
            [random.choice(numbers) for _ in range(nr_numbers)]
        )

        random.shuffle(password_list)
        password = "".join(password_list)
        pyperclip.copy(password)  # Copy password to clipboard
        return password
