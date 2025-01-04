from tkinter import Tk, Canvas, PhotoImage, Label, Entry, Button, messagebox
from password_generator import PasswordGenerator
from password_manager import PasswordManager

class PasswordManagerUI:
    def __init__(self):
        """
        Initialize the PasswordManagerUI class.
        """
        self.generator = PasswordGenerator()
        self.manager = PasswordManager()

        # Create main window
        self.window = Tk()
        self.window.title("Password Manager")
        self.window.config(padx=50, pady=50)

        # Canvas for the logo
        self.canvas = Canvas(width=200, height=200, highlightthickness=0)
        self.logo_image = PhotoImage(file="logo.png")
        self.canvas.create_image(100, 100, image=self.logo_image)
        self.canvas.grid(row=0, column=1)

        # Labels
        Label(text="Website:").grid(row=1, column=0)
        Label(text="Email/Username:").grid(row=2, column=0)
        Label(text="Password:").grid(row=3, column=0)

        # Entries
        self.website_entry = Entry(width=21)
        self.website_entry.grid(row=1, column=1)
        self.website_entry.focus()

        self.email_entry = Entry(width=35)
        self.email_entry.grid(row=2, column=1, columnspan=2)
        self.email_entry.insert(0, "example@example.com")

        self.password_entry = Entry(width=21)
        self.password_entry.grid(row=3, column=1)

        # Buttons
        Button(text="Search", command=self.handle_search).grid(row=1, column=2)
        Button(text="Generate Password", command=self.handle_generate_password).grid(row=3, column=2)
        Button(text="Add", width=36, command=self.handle_save).grid(row=4, column=1, columnspan=2)

    def handle_generate_password(self):
        """
        Generate a password and display it in the password entry field.
        """
        password = self.generator.generate()
        self.password_entry.delete(0, "end")
        self.password_entry.insert(0, password)

    def handle_save(self):
        """
        Save the entered password using PasswordManager.
        """
        website = self.website_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()

        self.manager.save(website, email, password)
        self.website_entry.delete(0, "end")
        self.password_entry.delete(0, "end")

    def handle_search(self):
        """
        Search for a password using PasswordManager and display the result.
        """
        website = self.website_entry.get()
        result = self.manager.find(website)

        if result:
            messagebox.showinfo(title=website, message=f"Email: {result['email']}\nPassword: {result['password']}")
        else:
            messagebox.showerror(title="Error", message=f"No details found for {website}.")

    def run(self):
        """
        Run the main event loop.
        """
        self.window.mainloop()
