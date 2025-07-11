class Book:
    def __init__(self, author, title, numOfPages):
        self.author = author
        self.title = title
        self.numOfPages = numOfPages

class Shelf:
    def __init__(self):
        self.books = [None] * 5 # = [None, None, None, None, None]
        self.isShelfFull = False

    def addBook(self, book):
        # add book to shelf in the first empty slot
        if self.isShelfFull:
            print("Shelf is full. Cannot add more books.")
            return

        for i in range(len(self.books)):
            if self.books[i] == None:
                self.books[i] = book
                break

        isThereEmptySpace =  False
        for book in self.books:
            if book == None:
                isThereEmptySpace = True
                break
        if not isThereEmptySpace:
            self.isShelfFull = True

    def replaceBooks(self, bookIndex1, bookIndex2):
        bookIndex1 -= 1
        bookIndex2 -= 1

        if self.books[bookIndex1] == None or self.books[bookIndex2] == None:
            print("One of the book indexes is empty")
        else:
            self.books[bookIndex1], self.books[bookIndex2] = self.books[bookIndex2], self.books[bookIndex1]

class Reader:
    def __init__(self, id, name):
        self.id = id
        self.name = name
        self.books = []

    def readBook(self, bookTitle):
        self.books.append(bookTitle)

class Library:
    def __init__(self):
        self.shelves = [Shelf(), Shelf(), Shelf()]
        self.readers = []

    def isTherePlaceForNewBook(self):
        for shelf in self.shelves:
            if not shelf.isShelfFull:
                return True
        return False
    
    def addNewBook(self, book):
        for shelf in self.shelves:
            if not shelf.isShelfFull:
                shelf.addBook(book)
                break

    def deleteBook(self, bookTitle):
        for shelf in self.shelves:
            for i in range(5):
                if shelf.books[i] is not None and shelf.books[i].title == bookTitle:
                    shelf.books[i] = None
                    shelf.isShelfFull = False

    def registerReader(self, readerName, readerId):
        reader = Reader(readerId, readerName)
        self.readers.append(reader)

    def removeReader(self, readerName):
        for reader in self.readers:
            if reader.name == readerName:
                self.readers.remove(reader)

    def searchByAuthor(self, authorName):
        bookTitles = []
        for shelf in self.shelves:
            for book in shelf.books:
                if book is not None and book.author == authorName:
                    bookTitles.append(book.title)
        return bookTitles   

def main():
    library = Library()
    
    for shelf in library.shelves:
        book1 = Book("Avi Ron", "Plain", 100)
        shelf.addBook(book1)
        book2 = Book("Eli Kopter", "Helicopter", 100)
        shelf.addBook(book2)
    
    while True:
        num = int(input("- For adding a book - Press 1\n"
        "- For deleting a book - Press 2\n"
        "- For registering a new reader - Press 3\n"
        "- For removing a reader - Press 4\n"
        "- For searching books by author - Press 5\n"
        "- For exit - Press 6\n"))
        if num == 6:
            print("Goodbye!")
            break
        
        elif num == 1:
            author = input("please provide the book author:\n")
            title = input("please provide the book title:\n")
            numOfPages = int(input("please provide the number of pages:\n"))

            book = Book(author, title, numOfPages)
            library.addNewBook(book)

        elif num == 2:
            title = input("please provide the book title:\n")
            library.deleteBook(title)

        elif num == 3:
            readerName = input("please provide the reader name:\n")
            readerId = int(input("please provide the reader id:\n"))

            library.registerReader(readerName, readerId)

        elif num == 4:
            readerName = input("please provide the reader name:\n")
            library.removeReader(readerName)

        elif num == 5:
            authorName = input("please provide the author name:\n")

            bookTitles = library.searchByAuthor(authorName)
            print(f'The book titles of the author {authorName} are: {bookTitles}')
        
        # print library
        elif num == 7:
            for shelf in library.shelves:
                print('\nShelf:\n')
                for book in shelf.books:
                    if book is not None:
                        print(f'{book.author}: {book.title} with {book.numOfPages} pages')
                    else:
                        print('Empty space')
            print("\n\nReaders:")
            for reader in library.readers:
                print(f"Name: {reader.name}, ID: {reader.id}, Books: {', '.join(reader.books)}\n")
            print("\n\n")

if __name__ == "__main__":
    main()