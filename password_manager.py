import json
from tkinter import messagebox

class PasswordManager:
    def __init__(self, data_file="data.json"):
        """
        Initialize the PasswordManager.
        Args:
            data_file (str): The file where passwords are stored.
        """
        self.data_file = data_file

    def save(self, website, email, password):
        """
        Saves a new password entry to the data file.
        Args:
            website (str): The website name.
            email (str): The email/username for the website.
            password (str): The password for the website.
        """
        if not website or not email or not password:
            messagebox.showerror(title="Error", message="Please fill in all fields.")
            return

        new_data = {website: {"email": email, "password": password}}

        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)  # Attempt to load JSON data
                except json.JSONDecodeError:
                    data = {}  # If the file is empty or invalid, initialize an empty dictionary
        except FileNotFoundError:
            data = {}  # If the file doesn't exist, initialize an empty dictionary

        data.update(new_data)

        with open(self.data_file, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

    def find(self, website):
        """
        Searches for a password entry by website name.
        Args:
            website (str): The website to search for.
        Returns:
            dict or None: The found entry or None if not found.
        """
        try:
            with open(self.data_file, "r", encoding="utf-8") as file:
                try:
                    data = json.load(file)  # Attempt to load JSON data
                except json.JSONDecodeError:
                    data = {}  # If the file is empty or invalid, initialize an empty dictionary
        except FileNotFoundError:
            messagebox.showerror(title="Error", message="No data file found.")
            return None

        return data.get(website, None)

