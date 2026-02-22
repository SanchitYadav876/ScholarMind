print("PYTHON PROBLEM SOLVING")
print()

print("LEVEL 1 - SIMPLE PROBLEMS")
print("=" * 50)

print("\n1. Check if number is positive, negative or zero")

def check_number(num):
    if num > 0:
        print(num, "is positive")
    elif num < 0:
        print(num, "is negative")
    else:
        print(num, "is zero")

check_number(10)
check_number(-5)
check_number(0)

print("\n2. Find largest number from 3 numbers")

def largest(a, b, c):
    if a > b and a > c:
        return a
    elif b > a and b > c:
        return b
    else:
        return c

print("Largest of 15, 42, 8 is:", largest(15, 42, 8))
print("Or using max():", max(15, 42, 8))

print("\n3. Sum of first n numbers")

def sum_n(n):
    total = 0
    for i in range(1, n + 1):
        total = total + i
    return total

print("Sum of first 5 numbers:", sum_n(5))
print("Sum of first 10 numbers:", sum_n(10))

print("\n" + "=" * 50)
print("LEVEL 2 - HARDER PROBLEMS")
print("=" * 50)

print("\n4. Factorial of a number")

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result

print("3! =", factorial(3))
print("5! =", factorial(5))
print("6! =", factorial(6))

print("\n5. Reverse a number (123 becomes 321)")

def reverse(num):
    reversed_num = 0
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return reversed_num

print("123 reversed is:", reverse(123))
print("4567 reversed is:", reverse(4567))
print("1000 reversed is:", reverse(1000))

print("\n6. Count digits in a number")

def count_digits(num):
    return len(str(abs(num)))

print("123 has", count_digits(123), "digits")
print("4567 has", count_digits(4567), "digits")
print("10 has", count_digits(10), "digits")

print("\n" + "=" * 50)
print("LEVEL 3 - STRING PROBLEMS")
print("=" * 50)

print("\n7. Count vowels in a string")

def count_vowels(text):
    vowels = "aeiouAEIOU"
    count = 0
    for char in text:
        if char in vowels:
            count = count + 1
    return count

print("'Hello World' has", count_vowels("Hello World"), "vowels")
print("'Python' has", count_vowels("Python"), "vowels")
print("'AEIOU' has", count_vowels("AEIOU"), "vowels")

print("\n8. Check if string is palindrome")

def is_palindrome(text):
    text = text.lower().replace(" ", "")
    return text == text[::-1]

words = ["racecar", "hello", "level", "madam", "python"]
for word in words:
    if is_palindrome(word):
        print(word, "is palindrome")
    else:
        print(word, "is not palindrome")

print("\n" + "=" * 50)
print("LEVEL 4 - REAL PROGRAMS")
print("=" * 50)

print("\n9. ATM SIMULATION")
print()

def atm():
    balance = 10000
    print("Welcome to ATM")
    print("Your balance:", balance)
    print()
    
    withdraw = int(input("Enter amount to withdraw: "))
    
    if withdraw <= 0:
        print("Invalid amount")
    elif withdraw > balance:
        print("Not enough balance")
        print("Your balance:", balance)
    else:
        balance = balance - withdraw
        print("Withdrawal successful")
        print("You withdrew:", withdraw)
        print("New balance:", balance)

print("Example ATM:")
print("Balance: 10000")
print("Withdraw: 2000")
print("New balance: 8000")
print()

print("\n10. LOGIN SYSTEM")
print()

def login():
    correct_user = "admin"
    correct_pass = "1234"
    attempts = 0
    max_attempts = 3
    
    while attempts < max_attempts:
        username = input("Enter username: ")
        password = input("Enter password: ")
        
        if username == correct_user and password == correct_pass:
            print("Login successful!")
            return True
        else:
            attempts = attempts + 1
            remaining = max_attempts - attempts
            if remaining > 0:
                print("Wrong! Remaining attempts:", remaining)
            else:
                print("Account locked")
                return False
    
    return False

print("Example Login:")
print("Username: admin")
print("Password: 1234")
print("Login successful!")
print()
print("Wrong attempt:")
print("Username: user")
print("Password: wrong")
print("Wrong! Remaining attempts: 2")
