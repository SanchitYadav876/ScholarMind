# ═══════════════════════════════════════════════════════════════════════════════
# COMPLETE GUIDE TO STRINGS AND LISTS IN PYTHON
# ═══════════════════════════════════════════════════════════════════════════════

print("="*70)
print("PART 1: STRINGS - COMPLETE GUIDE")
print("="*70)

# ═══════════════════════════════════════════════════════════════════════════════
# 1. STRING BASICS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 1. STRING CREATION ---")
# Strings can be created with single, double, or triple quotes
string1 = "Hello"
string2 = 'World'
string3 = """This is a
multi-line string"""

print(f"String 1: {string1}")
print(f"String 2: {string2}")
print(f"String 3: {string3}")

# ═══════════════════════════════════════════════════════════════════════════════
# 2. STRING INDEXING
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 2. STRING INDEXING ---")
# Strings are indexed from 0
text = "Python"
print(f"Text: {text}")
print(f"First character (index 0): {text[0]}")      # P
print(f"Third character (index 2): {text[2]}")      # t
print(f"Last character (index -1): {text[-1]}")     # n
print(f"Second last character (index -2): {text[-2]}")  # o

# ═══════════════════════════════════════════════════════════════════════════════
# 3. STRING SLICING
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 3. STRING SLICING ---")
# Syntax: string[start:end:step]
text = "Hello World"
print(f"Original: {text}")
print(f"First 5 characters [0:5]: {text[0:5]}")         # Hello
print(f"From index 6 [6:]: {text[6:]}")                # World
print(f"Every 2nd character [::2]: {text[::2]}")       # HloWrd
print(f"Reversed [::-1]: {text[::-1]}")                # dlroW olleH

# ═══════════════════════════════════════════════════════════════════════════════
# 4. STRING LENGTH
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 4. STRING LENGTH ---")
text = "Python"
print(f"Text: {text}")
print(f"Length: {len(text)}")  # 6

# ═══════════════════════════════════════════════════════════════════════════════
# 5. STRING CONCATENATION
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 5. STRING CONCATENATION ---")
# Method 1: Using + operator
first_name = "Ali"
last_name = "Khan"
full_name = first_name + " " + last_name
print(f"Using +: {full_name}")

# Method 2: Using f-strings (BEST METHOD)
age = 25
message = f"{first_name} is {age} years old"
print(f"Using f-string: {message}")

# Method 3: Using .format()
text = "I have {} apples and {} oranges".format(5, 3)
print(f"Using .format(): {text}")

# Method 4: Using .join()
fruits = ["apple", "banana", "orange"]
result = ", ".join(fruits)
print(f"Using .join(): {result}")

# ═══════════════════════════════════════════════════════════════════════════════
# 6. STRING METHODS (PART 1)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 6. STRING METHODS (UPPERCASE, LOWERCASE, CAPITALIZE) ---")
text = "hello world"
print(f"Original: {text}")
print(f".upper(): {text.upper()}")              # HELLO WORLD
print(f".lower(): {text.lower()}")              # hello world
print(f".capitalize(): {text.capitalize()}")    # Hello world
print(f".title(): {text.title()}")              # Hello World

# ═══════════════════════════════════════════════════════════════════════════════
# 7. STRING METHODS (PART 2)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 7. STRING METHODS (SEARCH & REPLACE) ---")
text = "Hello World Hello"
print(f"Original: {text}")
print(f".find('Hello'): {text.find('Hello')}")          # 0 (first position)
print(f".count('Hello'): {text.count('Hello')}")        # 2 (appears 2 times)
print(f".startswith('Hello'): {text.startswith('Hello')}")  # True
print(f".endswith('Hello'): {text.endswith('Hello')}")      # True
print(f".replace('Hello', 'Hi'): {text.replace('Hello', 'Hi')}")  # Hi World Hi

# ═══════════════════════════════════════════════════════════════════════════════
# 8. STRING METHODS (PART 3)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 8. STRING METHODS (SPLIT & STRIP) ---")
text = "  Hello World Python  "
print(f"Original: '{text}'")
print(f".strip(): '{text.strip()}'")            # Removes spaces from both ends
print(f".lstrip(): '{text.lstrip()}'")          # Removes spaces from left
print(f".rstrip(): '{text.rstrip()}'")          # Removes spaces from right

text = "apple,banana,orange"
print(f"\nOriginal: {text}")
print(f".split(','): {text.split(',')}")        # ['apple', 'banana', 'orange']

# ═══════════════════════════════════════════════════════════════════════════════
# 9. CHECK IF CHARACTER/WORD EXIST IN STRING
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 9. CHECK IF CHARACTER/WORD EXISTS ---")
text = "Hello World"
print(f"Text: {text}")
print(f"'H' in text: {'H' in text}")            # True
print(f"'x' in text: {'x' in text}")            # False
print(f"'World' in text: {'World' in text}")    # True

# ═══════════════════════════════════════════════════════════════════════════════
# 10. STRING METHODS (ADVANCED)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 10. STRING ADVANCED METHODS ---")
text = "hello123world"
print(f"Original: {text}")
print(f".isalpha(): {text.isalpha()}")          # False (contains numbers)
print(f".isdigit(): {text.isdigit()}")          # False (contains letters)
print(f".isalnum(): {text.isalnum()}")          # True (only letters and numbers)

text = "hello world"
print(f"\nOriginal: {text}")
print(f".isalpha(): {text.isalpha()}")          # False (contains space)
print(f".isspace(): {'   '.isspace()}")         # True (only spaces)

# ═══════════════════════════════════════════════════════════════════════════════
# PART 2: LISTS - COMPLETE GUIDE
# ═══════════════════════════════════════════════════════════════════════════════

print("\n\n" + "="*70)
print("PART 2: LISTS - COMPLETE GUIDE")
print("="*70)

# ═══════════════════════════════════════════════════════════════════════════════
# 1. LIST CREATION
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 1. LIST CREATION ---")
# Lists use square brackets []
list1 = [1, 2, 3, 4, 5]
list2 = ["apple", "banana", "orange"]
list3 = [1, "hello", 3.14, True]  # Mixed types
empty_list = []

print(f"List 1 (numbers): {list1}")
print(f"List 2 (strings): {list2}")
print(f"List 3 (mixed types): {list3}")
print(f"Empty list: {empty_list}")

# ═══════════════════════════════════════════════════════════════════════════════
# 2. LIST INDEXING
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 2. LIST INDEXING ---")
fruits = ["apple", "banana", "orange", "grape"]
print(f"List: {fruits}")
print(f"First element [0]: {fruits[0]}")        # apple
print(f"Second element [1]: {fruits[1]}")       # banana
print(f"Last element [-1]: {fruits[-1]}")       # grape
print(f"Second last [-2]: {fruits[-2]}")        # orange

# ═══════════════════════════════════════════════════════════════════════════════
# 3. LIST SLICING
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 3. LIST SLICING ---")
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"List: {numbers}")               # [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(f"[0:3]: {numbers[0:3]}")         # [1, 2, 3]
print(f"[2:7]: {numbers[2:7]}")         # [3, 4, 5, 6, 7]
print(f"[5:]: {numbers[5:]}")           # [6, 7, 8, 9, 10]
print(f"[:5]: {numbers[:5]}")           # [1, 2, 3, 4, 5]
print(f"[::2]: {numbers[::2]}")         # [1, 3, 5, 7, 9]
print(f"[::-1]: {numbers[::-1]}")       # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

# ═══════════════════════════════════════════════════════════════════════════════
# 4. LIST LENGTH
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 4. LIST LENGTH ---")
fruits = ["apple", "banana", "orange"]
print(f"List: {fruits}")
print(f"Length: {len(fruits)}")  # 3

# ═══════════════════════════════════════════════════════════════════════════════
# 5. ADD ELEMENTS (APPEND, INSERT, EXTEND)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 5. ADD ELEMENTS TO LIST ---")
# .append() - adds element at the end
fruits = ["apple", "banana"]
print(f"Original: {fruits}")
fruits.append("orange")
print(f"After .append('orange'): {fruits}")

# .insert() - adds element at specific position
fruits = ["apple", "banana", "orange"]
print(f"\nOriginal: {fruits}")
fruits.insert(1, "grape")  # Insert "grape" at index 1
print(f"After .insert(1, 'grape'): {fruits}")

# .extend() - adds multiple elements
fruits = ["apple", "banana"]
print(f"\nOriginal: {fruits}")
fruits.extend(["orange", "grape"])
print(f"After .extend(['orange', 'grape']): {fruits}") # ['apple', 'banana', 'orange', 'grape']

# ═══════════════════════════════════════════════════════════════════════════════
# 6. REMOVE ELEMENTS (REMOVE, POP, CLEAR)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 6. REMOVE ELEMENTS FROM LIST ---")
# .remove() - removes specific value
fruits = ["apple", "banana", "orange"]
print(f"Original: {fruits}")
fruits.remove("banana")
print(f"After .remove('banana'): {fruits}")

# .pop() - removes and returns element at index
fruits = ["apple", "banana", "orange"]
print(f"\nOriginal: {fruits}")
removed = fruits.pop(1)  # Remove at index 1
print(f"After .pop(1): {fruits}") # ['apple', 'orange']
print(f"Removed element: {removed}") # banana

# .pop() without index - removes last element
fruits = ["apple", "banana", "orange"]
print(f"\nOriginal: {fruits}")
fruits.pop()
print(f"After .pop() (no index): {fruits}") # ['apple', 'banana']

# .clear() - removes all elements
fruits = ["apple", "banana", "orange"]
print(f"\nOriginal: {fruits}")
fruits.clear()
print(f"After .clear(): {fruits}")

# ═══════════════════════════════════════════════════════════════════════════════
# 7. LIST METHODS (FIND & SORT)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 7. LENGTH & FIND ELEMENTS ---")
fruits = ["apple", "banana", "orange", "banana"]
print(f"List: {fruits}")
print(f".count('banana'): {fruits.count('banana')}")    # 2
print(f".index('orange'): {fruits.index('orange')}")    # 2

print("\n--- SORT LISTS ---")
numbers = [5, 2, 8, 1, 9]
print(f"Original: {numbers}")
numbers.sort()
print(f"After .sort(): {numbers}")  # [1, 2, 5, 8, 9]

numbers = [5, 2, 8, 1, 9]
print(f"\nOriginal: {numbers}")
numbers.sort(reverse=True)
print(f"After .sort(reverse=True): {numbers}")  # [9, 8, 5, 2, 1]

# Sort strings alphabetically
fruits = ["orange", "apple", "banana"]
print(f"\nOriginal: {fruits}")
fruits.sort()
print(f"After .sort(): {fruits}")

# ═══════════════════════════════════════════════════════════════════════════════
# 8. ITERATION THROUGH LISTS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 8. LOOP THROUGH LISTS ---")
# Method 1: For loop
fruits = ["apple", "banana", "orange"]
print(f"List: {fruits}")
print("Method 1 - Simple loop:")
for fruit in fruits:
    print(f"  - {fruit}")

# Method 2: For loop with index
print("\nMethod 2 - Loop with index:")
for i in range(len(fruits)):
    print(f"  Index {i}: {fruits[i]}")

# Method 3: Using enumerate (BEST)
print("\nMethod 3 - Using enumerate():")
for index, fruit in enumerate(fruits):
    print(f"  Index {index}: {fruit}")

# ═══════════════════════════════════════════════════════════════════════════════
# 9. CHECK IF ELEMENT EXISTS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 9. CHECK IF ELEMENT EXISTS ---")
fruits = ["apple", "banana", "orange"]
print(f"List: {fruits}")
print(f"'apple' in list: {'apple' in fruits}")          # True
print(f"'grape' in list: {'grape' in fruits}")          # False

# ═══════════════════════════════════════════════════════════════════════════════
# 10. LIST COPYING
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 10. LIST COPYING ---")
original = [1, 2, 3]
print(f"Original: {original}")

# WRONG way (creates reference, not copy)
wrong_copy = original
wrong_copy.append(4)
print(f"\nWrong way - wrong_copy = original")
print(f"Original after adding 4: {original}")  # Also changes!

# RIGHT way Method 1: .copy()
original = [1, 2, 3]
correct_copy = original.copy()
correct_copy.append(4)
print(f"\nRight way 1 - .copy()")
print(f"Original: {original}")         # [1, 2, 3]
print(f"Copy: {correct_copy}")         # [1, 2, 3, 4]

# RIGHT way Method 2: list()
original = [1, 2, 3]
correct_copy = list(original)
correct_copy.append(4)
print(f"\nRight way 2 - list()")
print(f"Original: {original}")         # [1, 2, 3]
print(f"Copy: {correct_copy}")         # [1, 2, 3, 4]

# ═══════════════════════════════════════════════════════════════════════════════
# 11. NESTED LISTS (LIST INSIDE LIST)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 11. NESTED LISTS ---")
# 2D List (Matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(f"Matrix:\n{matrix}")
print(f"First row [0]: {matrix[0]}")           # [1, 2, 3]
print(f"First element of first row [0][0]: {matrix[0][0]}")  # 1
print(f"Middle element [1][1]: {matrix[1][1]}")  # 5

# List with mixed data
data = [
    ["Ali", 25, 3.5],
    ["Fatima", 22, 3.8],
    ["Ahmed", 23, 3.6]
]
print(f"\nStudent Data:")
for student in data:
    print(f"  Name: {student[0]}, Age: {student[1]}, GPA: {student[2]}")

# ═══════════════════════════════════════════════════════════════════════════════
# 12. LIST COMPREHENSION (ADVANCED)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 12. LIST COMPREHENSION ---")
# Create list of squares
squares = [x**2 for x in range(1, 6)]
print(f"Squares of 1-5: {squares}")  # [1, 4, 9, 16, 25]

# Create list with conditions
numbers = [x for x in range(1, 11) if x % 2 == 0]
print(f"Even numbers 1-10: {numbers}")  # [2, 4, 6, 8, 10]

# Transform list
words = ["hello", "world", "python"]
uppercase = [word.upper() for word in words]
print(f"Uppercase: {uppercase}")  # ['HELLO', 'WORLD', 'PYTHON']

# ═══════════════════════════════════════════════════════════════════════════════
# 13. COMBINING LISTS (CONCATENATION & REPETITION)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- 13. COMBINE LISTS ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]

# Concatenation using +
combined = list1 + list2
print(f"{list1} + {list2} = {combined}")

# Repetition using *
repeated = [1, 2] * 3
print(f"[1, 2] * 3 = {repeated}")  # [1, 2, 1, 2, 1, 2]

# ═══════════════════════════════════════════════════════════════════════════════
# PART 3: PRACTICAL EXAMPLES (COMBINING STRINGS & LISTS)
# ═══════════════════════════════════════════════════════════════════════════════

print("\n\n" + "="*70)
print("PART 3: PRACTICAL EXAMPLES")
print("="*70)

# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 1: STUDENT MANAGEMENT SYSTEM
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- EXAMPLE 1: STUDENT MANAGEMENT ---")
students = ["Ali", "Fatima", "Ahmed"]
print(f"Students: {students}")

# Add student
students.append("Sara")
print(f"After adding Sara: {students}")

# Remove student
students.remove("Ahmed")
print(f"After removing Ahmed: {students}")

# Print with details
print("Final Student List:")
for i, student in enumerate(students, 1):
    print(f"  {i}. {student}")

# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 2: WORD COUNTER
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- EXAMPLE 2: WORD COUNTER ---")
sentence = "hello world hello python hello"
words = sentence.split()  # Convert string to list
print(f"Sentence: {sentence}")
print(f"Words: {words}")
print(f"Total words: {len(words)}")
print(f"'hello' appears: {words.count('hello')} times")
print(f"Unique words: {len(set(words))}")

# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 3: TEMPERATURE TRACKER
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- EXAMPLE 3: TEMPERATURE TRACKER ---")
temperatures = [25, 28, 26, 30, 29, 27]
print(f"Daily temperatures: {temperatures}")
print(f"Highest: {max(temperatures)}°C")
print(f"Lowest: {min(temperatures)}°C")
print(f"Average: {sum(temperatures) / len(temperatures):.1f}°C")

# Check hot days
hot_days = [temp for temp in temperatures if temp > 28]
print(f"Days above 28°C: {hot_days}")

# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 4: SHOPPING CART
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- EXAMPLE 4: SHOPPING CART ---")
cart = []

# Add items
items = ["Apple", "Banana", "Milk", "Bread"]
for item in items:
    cart.append(item)

print(f"Shopping Cart: {cart}")
print(f"Total items: {len(cart)}")

# Remove item
cart.remove("Banana")
print(f"After removing Banana: {cart}")

# Check if item exists
if "Milk" in cart:
    print("Milk is in cart ✓")

# Print with formatting
print("Cart Contents:")
for index, item in enumerate(cart, 1):
    print(f"  {index}. {item}")

# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 5: TEXT ANALYSIS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- EXAMPLE 5: TEXT ANALYSIS ---")
text = "  Python is awesome! Python is powerful!  "
print(f"Original text: '{text}'")

# Clean text
cleaned = text.strip().lower()
print(f"Cleaned text: '{cleaned}'")

# Split into words
words = cleaned.split()
print(f"Words: {words}")

# Count specific word
word_count = words.count("python")
print(f"'python' appears: {word_count} times")

# Check if contains word
if "awesome" in text.lower():
    print("Text contains 'awesome' ✓")

# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 6: GRADE CALCULATOR WITH LISTS
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- EXAMPLE 6: GRADE CALCULATOR ---")
students_data = [
    ("Ali", [85, 90, 88]),
    ("Fatima", [92, 88, 95]),
    ("Ahmed", [78, 85, 82])
]

print("Student Grades:\n")
for name, grades in students_data:
    average = sum(grades) / len(grades)
    grade = "A" if average >= 90 else "B" if average >= 80 else "C"
    print(f"  {name}: {grades} → Average: {average:.1f} → Grade: {grade}")

# ═══════════════════════════════════════════════════════════════════════════════
# EXAMPLE 7: PASSWORD VALIDATOR
# ═══════════════════════════════════════════════════════════════════════════════

print("\n--- EXAMPLE 7: PASSWORD VALIDATOR ---")
def validate_password(password):
    requirements = []
    
    if len(password) >= 8:
        requirements.append("✓ Length >= 8")
    else:
        requirements.append("✗ Length < 8")
    
    if any(char.isupper() for char in password):
        requirements.append("✓ Contains uppercase")
    else:
        requirements.append("✗ No uppercase")
    
    if any(char.isdigit() for char in password):
        requirements.append("✓ Contains number")
    else:
        requirements.append("✗ No number")
    
    return requirements

password = "Python123"
print(f"Validating password: {password}")
for requirement in validate_password(password):
    print(f"  {requirement}")

print("\n" + "="*70)
print("END OF COMPLETE GUIDE")
print("="*70)
