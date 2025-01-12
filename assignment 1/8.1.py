try:
    numerator = int(input(" numerator: "))
    denominator = int(input("denominator: "))
    result = numerator / denominator
    print("Result", result)
except ZeroDivisionError:
    print(" Cannot divide by zero")
except ValueError:
    print(" enter valid integers.")
