class Library:
    def __init__(self, list_of_books, name):
        self.bookList = list_of_books
        self.name = name
        self.lendDict = {}

    def displayBooks(self):
        print(f"We have the following books in our library: {self.name}")
        for books in self.bookList:
            print(books)

    def lendBook(self, user, books):
        if books not in self.bookList:
            print("Sorry, we do not have that book")
        elif books in self.lendDict:
            print(f"The book is already being used by {self.lendDict[books]}")
        else:
            self.lendDict[books] = user
            print("Lender-book Database has been updated. You can take the book now")

    def addBook(self, books):
        self.bookList.append(books)
        print(f"{books} has been added to the book list")

    def returnBook(self, books):
        if books in self.lendDict:
            del self.lendDict[books]
            print("Book has been returned")
        else:
            print("That book wasn't borrowed from us")

    
if __name__ == '__main__':
    books = Library(['Python',
                     'Rich Dad Poor Dad',
                     'Harry Potter',
                     'C++ Basics',
                     'Algorithms by CLRS'], 'Lets Upskil')
    
user_name = input("Welcome to our library! Pleaase enter your name:")

while True:
    print(f"\nHello {user_name}, welcome to the {books.name} Library! Please choose an option:")
    print("1. Display books \n2. Lend a book \n3. Add a book \n4. Return a book \n5. Quit")

    user_choice = input("Enter your choice to continue:")
    
    if user_choice not in ['1', '2', '3', '4', '5']:
        print("Please enter a valid option.")
        continue

    if user_choice == '1':
        books.displayBooks()
    elif user_choice == '2':
        book = input("Enter the name of the book you want to lend:")
        books.lendBook(user_name, book)
    elif user_choice == '3':
        book = input("ENter the name of the book you want to add:")
        books.addBook(book)
    elif user_choice == '4':
        book = input("Enter the name of the book you want to return:")
        books.returnBook(book)
    elif user_choice == '5':
        print(f"Thank you for using the library, {user_name}. Goodbye!")
        break