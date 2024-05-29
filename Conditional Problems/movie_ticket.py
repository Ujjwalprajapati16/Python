age = int(input("Enter age : "))
day = "Wednesday"
price = 12 if age >= 18 else 8
# price is 12 if age is greater than 18 else 8

if day == "Wednesday":
    price = price - 2

print("Ticket price for you is $", price)
