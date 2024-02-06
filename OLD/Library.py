class Library:

    def __init__(self, books_list, name):
        self.books_list = books_list
        self.name = name
        self.lend_dict = {}

    def display_books(self):
        print(f"We have the following books currently available in our library: {self.name}")
        for book in self.books_list:
            print(book)

    def lend_book(self, book, user):
        if book in self.books_list and book not in self.lend_dict:
            self.lend_dict[book] = user
            print("Book has been lent. Database updated.")
        else:
            print(f"Book is unavailable or already being used by {self.lend_dict.get(book, 'N/A')}")

    def add_book(self, book):
        self.books_list.append(book)
        print("Book added")

    def return_book(self, book):
        if book in self.lend_dict:
            self.lend_dict.pop(book)
            print("Book returned successfully")
        else:
            print("The book is not borrowed from this library.")

def load_books(database_name):
    with open(database_name, "r") as db:
        return [line.strip() for line in db.readlines()]

def main():
    database_name = input("Enter the name of the database file with extension:")
    try:
        books_list = load_books(database_name)
    except FileNotFoundError:
        print("Database file not found!")
        return

    library = Library(books_list, "PythonX")

    while True:
        print(f"\nWelcome to the {library.name} library. Following are the options:")
        user_choice = input('''\n1. Display Books
2. Lend a Book
3. Add a Book
4. Return a Book
\nSelect an option or press Q to quit: ''')

        if user_choice.upper() == "Q":
            break
        elif user_choice.isdigit() and 1 <= int(user_choice) <= 4:
            if int(user_choice) == 1:
                library.display_books()
            elif int(user_choice) == 2:
                book = input("Enter the name of the book you want to lend: ")
                user = input("Enter your name: ")
                library.lend_book(book, user)
            elif int(user_choice) == 3:
                book = input("Enter the name of the book you want to add: ")
                library.add_book(book)
            elif int(user_choice) == 4:
                book = input("Enter the name of the book you want to return: ")
                library.return_book(book)
        else:
            print("Please enter a valid option.")

if __name__ == '__main__':
    main()
