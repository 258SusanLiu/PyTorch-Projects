import torch

why = input("Do you want to play? Yes [1], No [2].")
while why == "1":
    # label: start
    t = input("Do you want to use scientific(1) or programmer(2) calculator: ")

    if t == "1":
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
            continue  # Go back to the start label

        print(result)
        why = input("Do you want to play? Yes [1], No [2].")

    elif t == "2":
        print("You have chosen programmer calculator")
        n = int(input("Input in a number: "))
        result_binary = bin(n)[2:]  # Convert to binary

        print(result_binary)
        why = input("Do you want to play? Yes [1], No [2].")

    else:
        print("You have not chosen 1 or 2. Bye")
        print("Please try again.")
