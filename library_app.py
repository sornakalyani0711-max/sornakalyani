import tkinter as tk
from tkinter import messagebox, simpledialog

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False

    def __str__(self):
        status = "Borrowed" if self.is_borrowed else "Available"
        return f"'{self.title}' by {self.author} [{status}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def borrow_book(self, title):
        for book in self.books:
            if book.title == title and not book.is_borrowed:
                book.is_borrowed = True
                return True
        return False

    def return_book(self, title):
        for book in self.books:
            if book.title == title and book.is_borrowed:
                book.is_borrowed = False
                return True
        return False

class LibraryApp:
    def __init__(self, root):  # <-- corrected constructor name
        self.library = Library()
        self.root = root
        self.root.title("Library Management System")
        self.root.geometry('530x450')

        frm = tk.Frame(root)
        frm.pack(pady=10)

        tk.Button(frm, text="View Books", width=25, command=self.view_books).grid(row=0, column=0, pady=5)
        tk.Button(frm, text="Add Book", width=25, command=self.add_book).grid(row=1, column=0, pady=5)
        tk.Button(frm, text="Borrow Book", width=25, command=self.borrow_book).grid(row=2, column=0, pady=5)
        tk.Button(frm, text="Return Book", width=25, command=self.return_book).grid(row=3, column=0, pady=5)
        tk.Button(frm, text="Exit", width=25, command=root.quit).grid(row=4, column=0, pady=5)

        self.books_listbox = tk.Listbox(root, width=70, height=15)
        self.books_listbox.pack(pady=10)
        self.view_books()

    def view_books(self):
        self.books_listbox.delete(0, tk.END)
        if not self.library.books:
            self.books_listbox.insert(tk.END, "No books available.")
        else:
            for idx, book in enumerate(self.library.books, 1):
                self.books_listbox.insert(tk.END, f"{idx}. {book}")

    def add_book(self):
        title = simpledialog.askstring("Add Book", "Enter book title:")
        if not title: return
        author = simpledialog.askstring("Add Book", "Enter author name:")
        if not author: return
        self.library.add_book(Book(title, author))
        messagebox.showinfo("Success", "Book added successfully!")
        self.view_books()

    def borrow_book(self):
        title = simpledialog.askstring("Borrow Book", "Enter book title to borrow:")
        if not title: return
        result = self.library.borrow_book(title)
        if result:
            messagebox.showinfo("Borrowed", f"Borrowed: {title}")
        else:
            messagebox.showerror("Error", "Book not available or already borrowed!")
        self.view_books()

    def return_book(self):
        title = simpledialog.askstring("Return Book", "Enter book title to return:")
        if not title: return
        result = self.library.return_book(title)
        if result:
            messagebox.showinfo("Returned", f"Returned: {title}")
        else:
            messagebox.showerror("Error", "Book not found or not borrowed!")
        self.view_books()

if __name__ == "__main__":  # <-- corrected main guard
    root = tk.Tk()
    app = LibraryApp(root)
    root.mainloop()