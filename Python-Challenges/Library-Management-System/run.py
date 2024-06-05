from library import Library


def main():
    """
    Main function to run the Library Management System.
    """
    library = Library()

    while True:
        print("\nLibrary Management System")
        print("1. Add Book")
        print("2. Display All Books")
        print("3. Search For Book by Title")
        print("4. Checkout Copy")
        print("5. Return Copy")
        print("6. Display Checked Out Copies")
        print("7. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            title = input("Enter book title: ")
            author = input("Enter book author: ")
            num_copies = int(input("Enter number of copies: "))
            library.add_book(title, author, num_copies)
        elif choice == "2":
            library.display_books()
        elif choice == "3":
            title = input("Enter book title to search: ")
            library.search_book(title)
        elif choice == "4":
            title = input("Enter book title to check out a copy: ")
            library.check_out_copy(title)
        elif choice == "5":
            title = input("Enter book title to return a copy: ")
            library.return_copy(title)
        elif choice == "6":
            library.display_checked_out_copies()
        elif choice == "7":
            print("Leaving Library..")
            break
        else:
            print("Invalid choice. Try Again.")


if __name__ == "__main__":
    main()
