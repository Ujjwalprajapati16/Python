num = 512
first = 0
last = num % 10

while num>0:
    first = num % 10
    num = num // 10

print(first + last)
    
