def calculate():
	a = 1
	b = 2
	return "a + b = " + str(a + b)


def is_valid_password(password):
    if len(password) >= 8:
        print
        return True
    else:
        print("Password must be at least 8 characters long.")
        return False
password("python123")
password("abc123")  

pass1 = is_valid_password("abc123")     # False (too short)
pass2 = is_valid_password("python123")  # True

print(pass1)  # Output: False
print(pass2)  # Output: True