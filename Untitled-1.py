age_input = input("Enter your age: ")

if age_input.isdigit():
    age = int(age_input)
    print(f"The type of age is {type(age)}")
else:
    print("Invalid input. Please enter numbers only.")




temperature = int(input("Enter the temperature: "))

if age >= 18:
    print("You are an adult")

if temperature <= 0:
    print("It's freezing")
elif temperature > 30:
    print("It's very hot")
else:
    print("Temperature is moderate")  # This will print

