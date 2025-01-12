import sys

if len(sys.argv) != 2:
    print(" provide a string as a command-line argument.")
else:
    user_string = sys.argv[1]
    print(f"The length of the string '{user_string}' is {len(user_string)}")