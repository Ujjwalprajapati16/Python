# Day 4

is operator provide false in float beacuse floating point value is stored in different memory locations.
```python
a = 10.5
b = 10.5
a is b # False
```

## Control flow statements / Flow control statements

- Selective statements : Filteration / select
    - if-else statement
- Iterative statements : Repeat
    - while loop
    - for loop
- Jump statements : Stop / skip
    - break 
    - continue

### if-else statement
syntax:
```python
if condition:
    pass
```
- Condition should be <bool> type (True / False)
- python assumes all none zeros and all none values are true otherwise false
```python
if 10:
    print("Hello") 
else :
    print("HI")
print("Bye")
# Hello
# Bye
```
```python
if 0:
    print("Hello") 
else :
    print("Hi")
print("Bye")
# Hi
# Bye
```
- Python uses None instead of Null
```python
if None:
    print("Hello") 
else :
    print("Hi")
# Hi
```
```python
if not None:
    print("Hello") 
else :
    print("Hi")
# Hello
```

```python
if 10 < 20:
    print("Hello")
else :
    print("Hi")
```

```python
if 10 > 20:
    print("Hello")
else :
    print("HI")
print("Bye")
```

- Else without if is not exceptable
```python
else :
    print("Hi") # Invalid statement
```
- print function always returns None
```python
if print("hello"):
    print("Hi")
else :
    print("Bye") 
# Hello
# Bye
```
```python
if int(input("Enter a number : ")):
    print("Hi")
else:
    print("Bye")
# Enter a number : 0
# Bye
```

- If we want to check multiple conditions between if-else we use elif statement.

[!QUESTION]
Check the greater number in 3 numbers
```python
a = 10
b = 20
c = 30

if a>b and a>c:
    print("a is greater")
elif b>c:
    print("b is greater")
else:
    print("c is greater")
# c is greater
```

### Nested if-else
if-else condition inside the another if-else statement is called nested if-else.
```python
a = 1000
b = 120
c = 30

if a>b:
    if a>c:
        print("a is greater")
    else:
        print("c is greater")
else:
    if b>c:
        print("b is greater")
    else:
        print("c is greater")
# a is greater
```

### While loop
syntax
```python
while condition:
    # statement
```
- jab tak condition true hai tab tak while loop run hoga
- 
- if condition is false it will not run
```python
while 10 < 20:
    print("Hello")
```
- We can use else also with while loop
```python
while 10 > 20:
    print("Hello")
else:
    print("Hi")
# Hi
```

```python
a = 1
while a < 10:
    print(a)
    a += 1
else:
    print("Bye")

1
2
3
4
5
6
7
8
9
Bye
```

> [!IMPORTANT]
Sum of digits of number.
num = 512
o/p = 5 + 1+ 2 = 8

```python
num = 512
sum = 0

while num>0:
    rem = num % 10
    sum = sum + rem
    num = num // 10

print(sum) # 8
```

> [!IMPORTANT]
find the product of digit of the number.
```python
num = 512
pro = 1

while num>0:
    rem = num % 10
    pro = pro * rem
    num = num // 10

print(pro) # 10
```

> [!IMPORTANT]
Find first and last digit of the number and then sum
```python
num = 512
first = 0
last = num % 10

while num>0:
    first = num % 10
    num = num // 10

print(first + last) # 7
```

> [!IMPORTANT]
find the smallest digit for each digit position and then the largest digit from the all numbers at thousands place

hundreds tens ones
a = 5   4   2
b = 3   5   9
c = 6   1   3
output = 9312

constraints:
100 >= inputs <= 999 


### Interview quetion
> [!NOTE]
> Difference between while loop and for loop
We already know number of steps we use for loop , when we don't know number of steps we use while loop

