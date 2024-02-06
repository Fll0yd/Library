from tkinter import *
from tkinter import ttk

class Library:

    def __init__(self, books_list, name):
        self.books_list = books_list
        self.name = name
        self.lend_dict = {}

    def display_books(self, output_text):
        output_text.delete(1.0, END)
        output_text.insert(INSERT, f"We have the following books currently available in our library: {self.name}\n")
        
        # Read the list of books from the text file
        with open(r"F:/Code/Python/Library/pythonxDatabase.txt", "r") as file:
            books_list = file.readlines()

        print(books_list)  # Debugging: Print the contents of books_list
        
        for book in books_list:
            output_text.insert(INSERT, f"{book.strip()}\n")  # Strip newline characters

    def lend_book(self, book, user, output_text):
        if book in self.books_list and book not in self.lend_dict:
            self.lend_dict[book] = user
            output_text.insert(INSERT, "Book has been lent. Database updated.\n")
        else:
            output_text.insert(INSERT, f"Book is unavailable or already being used by {self.lend_dict.get(book, 'N/A')}\n")

    def add_book(self, book, output_text):
        self.books_list.append(book)
        output_text.insert(INSERT, "Book added\n")

    def return_book(self, book, output_text):
        if book in self.lend_dict:
            self.lend_dict.pop(book)
            output_text.insert(INSERT, "Book returned successfully\n")
        else:
            output_text.insert(INSERT, "The book is not borrowed from this library.\n")

def main():
    books_list = ['Book 1', 'Book 2', 'Book 3']  # Sample list
    library = Library(books_list, "PythonX")

    root = Tk()
    root.title("Library Management")

    frame = ttk.Frame(root, padding="10")
    frame.grid(row=0, column=0, sticky=(N, W, E, S))

    user_entry = ttk.Entry(frame, width=30)
    user_entry.grid(row=0, column=1)
    ttk.Label(frame, text="User Name:").grid(row=0, column=0)

    book_entry = ttk.Entry(frame, width=30)
    book_entry.grid(row=1, column=1)
    ttk.Label(frame, text="Book Name:").grid(row=1, column=0)

    output_text = Text(frame, wrap=WORD, width=40, height=10)
    output_text.grid(row=4, columnspan=4)

    def click_display():
        library.display_books(output_text)

    def click_lend():
        book = book_entry.get()
        user = user_entry.get()
        library.lend_book(book, user, output_text)

    def click_add():
        book = book_entry.get()
        library.add_book(book, output_text)

    def click_return():
        book = book_entry.get()
        library.return_book(book, output_text)

    ttk.Button(frame, text="Display Books", command=click_display).grid(row=2, column=0)
    ttk.Button(frame, text="Lend Book", command=click_lend).grid(row=2, column=1)
    ttk.Button(frame, text="Add Book", command=click_add).grid(row=3, column=0)
    ttk.Button(frame, text="Return Book", command=click_return).grid(row=3, column=1)

    root.mainloop()

if __name__ == '__main__':
    main()
