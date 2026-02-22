for i in range(3):
    for j in range(2):
        print(i,j)

fruits = ["apple", "banana"]
print(f"Original: {fruits}")
fruits.append("orange")
print(f"After .append('orange'): {fruits}") # ['apple', 'banana', 'orange']