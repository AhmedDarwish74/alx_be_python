from arithmetic_operations import perform_operation

def main():
    print("arthmetic operations")
    num1 = float(input("Enter the first number : "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (add,subtract,multiply,divide): ").strip().lower()
    result = perform_operation(num1,num2 ,operation)
    print(f"result: {result}")
if __name__ == "__main__":
    main()
