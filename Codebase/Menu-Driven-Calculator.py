def addition(a, b):
    return a + b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

def power(a, b):
    return a ** b

def modulus(a, b):
    return a % b

while True:
    print("===== MENU-DRIVEN CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Modulus")
    print("7. Exit")
    
    try:
        choice = int(input("Enter your choice: "))

    except ValueError:
        print("Invalid input! Please enter a number.")
        continue

    if choice == 1:
        try:
            a = input("Enter first number: ")
            b = input("Enter second number: ")

            a = float(a)
            b = float(b)

            result = addition(a, b)
            print(f"Addition: {result:.2f}")

        except ValueError:
            print("Invalid number. Enter numeric values only.")

    elif choice == 2:
        try:
            a = input("Enter first number: ")
            b = input("Enter second number: ")

            a = float(a)
            b = float(b)

            result = subtraction(a, b)
            print(f"Subtraction: {result:.2f}")

        except ValueError:
            print("Invalid number. Enter numeric values only.")

    elif choice == 3:
        try:
            a = input("Enter first number: ")
            b = input("Enter second number: ")

            a = float(a)
            b = float(b)
            result = multiplication(a, b)
            print(f"Multiplication: {result:.2f}")

        except ValueError:
            print("Invalid number. Enter numeric values only.")

    elif choice == 4:
        try:
            a = input("Enter first number: ")
            b = input("Enter second number: ")

            a = float(a)
            b = float(b)

            if b == 0:
                print("Error: Division by zero is not allowed.")

            else:
                result = division(a, b)
                print(f"Division: {result:.2f}")

        except ValueError:
            print("Invalid number. Enter numeric values only.")

    elif choice == 5:
        try:
            a = input("Enter first number: ")
            b = input("Enter second number: ")

            a = float(a)
            b = float(b)
            
            result = power(a, b)
            print(f"Power: {result:.2f}")

        except ValueError:
            print("Invalid number. Enter numeric values only.")
        
    elif choice == 6:
        try:
            a = input("Enter first number: ")
            b = input("Enter second number: ")

            a = float(a)
            b = float(b)

            if b == 0:
                print("Error: Modulus by zero is not allowed.")

            else:
                result = modulus(a, b)
                print(f"Modulus: {result:.2f}")

        except ValueError:
            print("Invalid number. Enter numeric values only.")   

    elif choice == 7:
        print("Thank you for using the calculator. Exiting...")
        break
    else:
        print("Invalid choice. Select 1 to 7.")