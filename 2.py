num1 = 20
num2 = 3

sum_result = num1 + num2
print(f"{num1} + {num2} = {sum_result}")          # 20 + 3 = 23

difference = num1 - num2
print(f"{num1} - {num2} = {difference}")          # 20 - 3 = 17

product = num1 * num2
print(f"{num1} * {num2} = {product}")             # 20 * 3 = 60

quotient = num1 / num2
print(f"{num1} / {num2} = {quotient}")            # 20 / 3 = 6.666...

remainder = num1 % num2
print(f"{num1} % {num2} = {remainder}")           # 20 % 3 = 2

power = num1 ** 2
print(f"{num1} ** 2 = {power}")                   # 20 ** 2 = 400

age = 25
has_license = True

if age >= 18 and has_license:
    print("You can drive")  # This will print

# More examples
print(True and True)    # True
print(True and False)   # False
print(False and False)  # False

day = input("Enter the day of the week: ")

if day == "Saturday" or day == "Sunday":
    print("It's the weekend!")  # This will print

# More examples
print(True or False)    # True
print(False or False)   # False
print(True or True)     # True

is_raining = False

if not is_raining:
    print("Go outside!")  # This will print

# More examples
print(not True)         # False
print(not False)        # True
print(not (5 > 3))      # Falseage = 15

if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")  # This will print    age = 20
    
    if age >= 18:
        print("You are an adult")      
       