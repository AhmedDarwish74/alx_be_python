def display_menu():
    print("shoping list manager")
    print("1. Add Items")
    print("2. Remove Items")
    print("3. View List")
    print("4. Exit ")
def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice (1-4): ")
        if choice.isdigit() and int(choice) in [1, 2, 3, 4]:
            choice = int(choice)
        if choice == "1":
            item = input("Enter the item name to add:  ")
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list")
        elif choice == "2":
            item = input("Enter the item name to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list")
            else:
                print(f"'{item}' not found in the shopping list. ")
        elif choice == "3":
            print("current shopping list ")
            if shopping_list:
                if item in shopping_list:
                    print(f"- {item}")
                else:
                    print("the shopping list is empty")
        elif choice == "4":
            print("Good bye!")
            break
        else:
             print("Invalid choice. Please try again.")
        

if __name__ == "__main__":
    main()  
