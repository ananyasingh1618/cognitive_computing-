import random
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True
random_numbers = [random.randint(100, 900) for _ in range(100)]
odd_numbers = [num for num in random_numbers if num % 2 != 0]
even_numbers = [num for num in random_numbers if num % 2 == 0]
prime_numbers = [num for num in random_numbers if is_prime(num)]
print("Odd numbers count:", len(odd_numbers))
print("Even numbers count:", len(even_numbers))
print("Prime numbers count:", len(prime_numbers))
