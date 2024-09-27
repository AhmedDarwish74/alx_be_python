def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []  
    while True:
        display_menu() 
        choice = input("Enter your choice (1-4): ")  

        # التأكد من أن الإدخال هو عدد صحيح
        if choice.isdigit() and int(choice) in [1, 2, 3, 4]:
            choice = int(choice)  # تحويل الإدخال إلى عدد صحيح
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")  # رسالة خطأ إذا كانت الإدخال غير صالح
            continue  # العودة إلى بداية الحلقة

        if choice == 1:
            # إضافة عنصر
            item = input("Enter the item name to add: ")
            shopping_list.append(item)  # إضافة العنصر إلى القائمة
            print(f"'{item}' has been added to the shopping list.")
        
        elif choice == 2:
            # إزالة عنصر
            item = input("Enter the item name to remove: ")
            if item in shopping_list:
                shopping_list.remove(item)  # إزالة العنصر من القائمة
                print(f"'{item}' has been removed from the shopping list.")
            else:
                print(f"'{item}' not found in the shopping list.")  # رسالة إذا لم يكن العنصر موجود

        elif choice == 3:
            # عرض قائمة التسوق
            print("Current Shopping List:")
            if shopping_list:  # تحقق مما إذا كانت القائمة غير فارغة
                for item in shopping_list:
                    print(f"- {item}")  # طباعة كل عنصر في القائمة
            else:
                print("The shopping list is empty.")  # رسالة إذا كانت القائمة فارغة
        
        elif choice == 4:
            print("Goodbye!")  # رسالة وداع
            break  # إنهاء البرنامج

if __name__ == "__main__":
    main()  # بدء البرنامج
