from library import Library

def main():
    lib=Library()
    while True:

        print("Menu\n 1.List Books\n 2.Add Book\n 3.Remove Book\n 4.Quick")
        choice=input("Enter your choice: ")

        if choice=="1":
            lib.list_books()
        elif choice=="2":
            lib.add_book()
        elif choice=="3":
            lib.remove_book()
        elif choice=="4":
            break
        else:
            print("Invalid choice.Please enter a a number from 1 to 4")




if __name__=="__main__":
    main()
