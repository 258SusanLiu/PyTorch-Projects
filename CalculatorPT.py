import torch

def matrix_calculator():
    print("Matrix Calculator using PyTorch")
    print("1. Matrix Addition")
    print("2. Matrix Subtraction")
    print("3. Matrix Multiplication")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == "4":
        print("Exiting Matrix Calculator.")
        
        why = input("Do you want to play? Yes [1], No [2].")
        return why
        return why

    try:
        rows_A = int(input("Enter the number of rows for Matrix A: "))
        cols_A = int(input("Enter the number of columns for Matrix A: "))
        matrix_A = torch.zeros((rows_A, cols_A))

        for i in range(rows_A):
            for j in range(cols_A):
                matrix_A[i, j] = float(input(f"Enter element A[{i+1},{j+1}]: "))

        if choice in ["1", "2"]:
            rows_B = int(input("Enter the number of rows for Matrix B: "))
            cols_B = int(input("Enter the number of columns for Matrix B: "))
            matrix_B = torch.zeros((rows_B, cols_B))

            for i in range(rows_B):
                for j in range(cols_B):
                    matrix_B[i, j] = float(input(f"Enter element B[{i+1},{j+1}]: "))

        if choice == "1":
            result = matrix_A + matrix_B
            print("Result of Matrix Addition:")
            print(result)
        elif choice == "2":
            result = matrix_A - matrix_B
            print("Result of Matrix Subtraction:")
            print(result)
        elif choice == "3":
            cols_B = int(input("Enter the number of columns for Matrix B: "))
            matrix_B = torch.zeros((cols_A, cols_B))

            for i in range(cols_A):
                for j in range(cols_B):
                    matrix_B[i, j] = float(input(f"Enter element B[{i+1},{j+1}]: "))

            result = torch.matmul(matrix_A, matrix_B)
            print("Result of Matrix Multiplication:")
            print(result)
        else:
            print("Invalid choice. Please enter a number between 1 and 4.")

    except ValueError:
        print("Invalid input. Please enter numeric values for matrix elements.")

    matrix_calculator()

def scientific_calculator():
    print("You have chosen scientific calculator")
    # label: tryagain
    x = int(input("What is the 1st number you want to calculate: "))
    y = int(input("What is the 2nd number you want to calculate: "))
    num = int(input("What type of calculation do you want? Addition [1], Subtraction [2], Multiplication [3], Division [4]"))
    
    if num == 1:
        result = x + y
    elif num == 2:
        result = x - y
    elif num == 3:
        result = x * y
    elif num == 4:
        result = x / y
    else:
        print("You did not select Addition [1], Subtraction [2], Multiplication [3], or Division [4]")
        print("Please try again.")
        # continue  # Go back to the start label

    print(result)
    why = input("Do you want to play? Yes [1], No [2].")
    return why

def binary_calculator():
    print("You have chosen programmer calculator")
    n = int(input("Input in a number: "))
    result_binary = bin(n)[2:]  # Convert to binary

    print(result_binary)
    why = input("Do you want to play? Yes [1], No [2].")
    return why

if __name__ == "__main__":
    why = input("Do you want to play? Yes [1], No [2].")
    while why == "1":
        # label: start
        t = input("Do you want to use matrix(1), scientific(2) or programmer(3) calculator: ")
        if t == "1":
            matrix_calculator()

        if t == "2":
            scientific_calculator()

        elif t == "3":
            binary_calculator()

        else:
            print("You have not chosen 1, 2 or 3. Bye")
            print("Please try again.")

    
