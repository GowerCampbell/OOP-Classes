# Define a class for books in the library.
class Book:
    def __init__(self, title, author, copies):
        """
        Initialize a book instance with a title, author, and number of copies.
        :param title: str, the title of the book
        :param author: str, the author's name
        :param copies: int, the number of available copies
        """
        self.title = title
        self.author = author
        self.copies = copies

    def copy_in_library(self):
        """
        Check if there is at least one copy of the book available in the library.
        :return: bool, True if copies > 0, otherwise False
        """
        return self.copies > 0


# A global dictionary to store books by their titles.
library = {}


# Function to populate the library with initial data.
def populate_library():
    """
    Populate the library dictionary with a set of predefined books.
    """
    library["Atomic Habits"] = Book("Atomic Habits", "James Clear", 5)
    library["Knotebook"] = Book("Knotebook", "Toby", 6)
    library["Brave New World"] = Book("Brave New World", "Aldous Huxley", 7)
    library["The Twilight Saga"] = Book("The Twilight Saga", "M.K", 7)


# Function to list all books in the library.
def list_books():
    """
    Display all books in the library, including their authors and number of copies.
    """
    print(f"{'Title':<30}{'Author':<20}{'Copies':<10}")
    print("-" * 60)
    for title, book in library.items():
        print(f"{title:<30}{book.author:<20}{book.copies:<10}")


# Function to list all available books with copies > 0.
def list_available_books():
    """
    Display only the books that have at least one copy available in the library.
    """
    print(f"{'Title':<30}{'Author':<20}{'Copies':<10}")
    print("-" * 60)
    for title, book in library.items():
        if book.copy_in_library():
            print(f"{title:<30}{book.author:<20}{book.copies:<10}")


# Function to borrow a book from the library.
def borrow_a_book(title):
    """
    Borrow a book by reducing its available copy count by one.
    :param title: str, the title of the book to borrow
    """
    if title in library and library[title].copy_in_library():
        library[title].copies -= 1
        print(f"\nYou have borrowed '{title}' by {library[title].author}.")
    else:
        print("\nThat book is not available or does not exist.")


# Function to return a borrowed book to the library.
def return_a_book(title):
    """
    Return a borrowed book by increasing its available copy count by one.
    :param title: str, the title of the book to return
    """
    if title in library:
        library[title].copies += 1
        print(f"\nYou have returned '{title}' by {library[title].author}.")
    else:
        print("\nThat book does not exist in the library.")


# Main Menu
def main_menu():
    """
    Display the main menu and allow the user to interact with the library system.
    """
    populate_library()

    while True:
        print("\nLibrary Menu:")
        print("1. List All Books")
        print("2. List Available Books")
        print("3. Borrow a Book")
        print("4. Return a Book")
        print("5. Quit")

        choice = input("Enter the number of your choice: ").strip()

        if choice == '1':
            list_books()
        elif choice == '2':
            list_available_books()
        elif choice == '3':
            title = input("Enter the title of the book to borrow: ").strip()
            borrow_a_book(title)
        elif choice == '4':
            title = input("Enter the title of the book to return: ").strip()
            return_a_book(title)
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


# Start the program
if __name__ == "__main__":
    main_menu()
