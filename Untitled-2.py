first_name = "Muhammad"
last_name = "Ali"

full_name = first_name + " " + last_name
print(full_name)  # Output: Muhammad Ali

text = "Hello bro how are you?"
print(len(text))         
text = "Python"

print(text[0])   # Output: P
print(text[1])   # Output: y
print(text[2])   # Output: t
print(text[-1])  # Output: n (last character)
print(text[-2])  # Output: o (second last)
text = "Python"

print(text[0:2])   # Output: Py (characters 0 and 1)
print(text[1:4])   # Output: yth
print(text[2:])    # Output: thon (from position 2 to end)
print(text[:3])    # Output: Pyt (from start to position 2)
text = "hello"
print(text.upper())  # Output: HELLO
print(text.lower())  # Output: hello
print(text.capitalize())  # Output: Hello
text = "I like cats"
new_text = text.replace("cats", "dogs")
print(new_text)  # Output: I like dogs
text = "apple,banana,orange"
fruits = text.split(",") 
print(fruits)  # Output: ['apple', 'banana', 'orange']