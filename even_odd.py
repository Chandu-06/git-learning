def check_even_odd(num):
    return "Even" if num % 2 == 0 else "Odd"

try:
    number = int(input("Enter a number: "))
    print(check_even_odd(number))
except ValueError:
    print("Invalid input! Please enter a number.")
