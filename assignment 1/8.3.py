try:
    numerator = int(input("Enter numerator: "))
    denominator = int(input("Enter denominator: "))
    result = numerator / denominator
    print("Result:", result)
except ZeroDivisionError:
    print(" Cannot divide by zero!")
except ValueError:
    print("enter valid integers.")
finally:
    print("This block executes no matter what.")
