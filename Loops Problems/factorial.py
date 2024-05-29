number = 5
factorial = 1

while True:
    if number == 0:
        break
    factorial = factorial * number
    number = number - 1

print(factorial)