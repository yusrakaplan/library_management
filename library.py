
class Library():
    def __init__(self):
        self.file=open("book.txt","+a",encoding="utf_8")
    def __del__(self):
        self.file.close()
    def list_books(self):
        self.file.seek(0)
        books=self.file.readlines()
        for book in books:
            book_info=book.strip().split(",")
            book_name,book_author=book_info[:2]
            print(f"Book Name:{book_name},Author:{book_author}")

    def add_book(self):
        book_name=input("Enter the book name: ")
        book_author=input("Enter the book authr: ")
        release_year=input("Enter the first release year: ")
        num_pages=input("Enter the number of pages: ")
        book_info=f"{book_name},{book_author},{release_year},{num_pages}"
        self.file.write(book_info)

    def remove_book(self):
        book_name = input("Enter the book you want to remove: ")
        self.file.seek(0)
        book_list = self.file.readlines()
        updated_list = []
        removed = False
        for book in book_list:
            book_info = book.strip().split(",")
            if book_info[0] != book_name:
                updated_list.append(','.join(book_info))
            else:
                removed = True
        if removed:
            self.file.seek(0)
            self.file.truncate()
            self.file.write('\n'.join(updated_list))  # Join the updated_list with newline character

            print(f"{book_name} removed successfully")
        else:
            print(f"{book_name} not found")




