class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_issued = False


class Member:
    def __init__(self, name):
        self.name = name
        self.borrowed_books = []


class Library:
    def __init__(self):
        self.books = []
        self.members = []

    def add_book(self):
        title = input("Enter book title: ")
        author = input("Enter author name: ")
        self.books.append(Book(title, author))
        print("Book added successfully!")

    def add_member(self):
        name = input("Enter member name: ")
        self.members.append(Member(name))
        print("Member added successfully!")

    def display_books(self):
        if not self.books:
            print("No books available.")
            return
        for i, book in enumerate(self.books):
            status = "Issued" if book.is_issued else "Available"
            print(f"{i+1}. {book.title} by {book.author} - {status}")

    def lend_book(self):
        self.display_books()
        book_index = int(input("Select book number: ")) - 1

        if book_index < 0 or book_index >= len(self.books):
            print("Invalid book selection!")
            return

        book = self.books[book_index]
        if book.is_issued:
            print("Book already issued!")
            return

        name = input("Enter member name: ")
        member = next((m for m in self.members if m.name == name), None)

        if not member:
            print("Member not found!")
            return

        book.is_issued = True
        member.borrowed_books.append(book)
        print("Book issued successfully!")

    def return_book(self):
        name = input("Enter member name: ")
        member = next((m for m in self.members if m.name == name), None)

        if not member:
            print("Member not found!")
            return

        if not member.borrowed_books:
            print("No borrowed books.")
            return

        for i, book in enumerate(member.borrowed_books):
            print(f"{i+1}. {book.title}")

        book_index = int(input("Select book to return: ")) - 1

        if book_index < 0 or book_index >= len(member.borrowed_books):
            print("Invalid selection!")
            return

        book = member.borrowed_books.pop(book_index)
        book.is_issued = False
        print("Book returned successfully!")


# Menu-driven program
library = Library()

while True:
    print("\n--- Library Menu ---")
    print("1. Add Book")
    print("2. Add Member")
    print("3. Display Books")
    print("4. Lend Book")
    print("5. Return Book")
    print("6. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        library.add_book()
    elif choice == "2":
        library.add_member()
    elif choice == "3":
        library.display_books()
    elif choice == "4":
        library.lend_book()
    elif choice == "5":
        library.return_book()
    elif choice == "6":
        print("Exiting...")
        break
    else:
        print("Invalid choice!")