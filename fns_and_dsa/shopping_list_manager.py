def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def get_choice():
    choice = input("Enter your choice (1-4): ")
    if choice.isdigit() and int(choice) in [1, 2, 3, 4]:
        return int(choice)
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")
        return None

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = get_choice()
        if choice is None:
            continue
        
        if choice == 1:
            item = input("Enter the item to add: ")  
            shopping_list.append(item)
            print(f"'{item}' has been added to the shopping list.")
        
        elif choice == 2:
            item = input("Enter the item to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")
        
        elif choice == 3:
            print("Current Shopping List:")
            if shopping_list:
                for item in shopping_list:
                    print(f"- {item}")
            else:
                print("The shopping list is empty.")
        
        elif choice == 4:
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
