password = "Secure@123"

if len(password) < 6:
    strength = "weak"
elif len(password) <= 10:
    strength = "Medium"
else:
    strength = "Strong"

print("Password strength is :", strength)