count = 1
while count <= 5:
            print(f"Count: {count}")
            count = count + 1
        
        # Output:
        # Count: 1
        # Count: 2
        # Count: 3
        # Count: 4
        # Count: 5score = 75      
count = 1


while count < 5:
    count = count + 1
    print(count)
    if count == 3:
        continue  # Skip when count is 3
    print(count)

password = "python123"
attempts = 0

while attempts < 3:
    user_pass = input("Enter password: ")
    if user_pass == password:
        print("Access granted!")
        break
    else:
        attempts = attempts + 1
        print(f"Wrong! {3 - attempts} attempts left")

if attempts == 3:
    print("Too many wrong attempts. Access denied.")

def table(n):
    for i in range(1,11):
        print(n*i)
table(7)

def add(a,b):
     print(a+b)

add(5,4)
    
def is_adult(age):
    if age >= 18:
        return True
    else:
        return False

print(is_adult(25))  # Output: True
print(is_adult(15))  # Output: False

is_adult(22)