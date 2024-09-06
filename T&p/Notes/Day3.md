# Day 3

## Operators (remaining in Day 2)
### Shift operator
- Left shift (<<)
```python
x = 10
x<<2 # 40
```
- Right shift (>>)
```python
x = 10
x>>1 # 5
```

### Membership Operator
- in (Partial match)
It find exact match but it also works with partial matches

Exact match = True
Partial match = True
Not found = False

```python
a = "Hello world"
print("Hello" in a) # True

a = "This is a test String for testing"
print("Test" in a) # False
```

- not in
```python
a = "Hello world"
print("Hello" not in a) # False

a = "This is a test String for testing"
print("Test" not in a) # True
```

### Identity Operator
- is 
```python
a = 100
b = 100
print(a is b) # True

a = 100
b = 90
print(a is b) # False

a = 100
b = 90+10
print(a is b) # True

a = 100.0
b = 90.0 + 10.0
print(a is b) # False
```


## Life Cycle of Python Code

- Python Source Code
    - Write code and saved with a .py file extension

- Interpreter 

- Byte Code 
    - Byte code stored in .pyc file
    - inside the __pycache__ directory 
- PVM 
    - Convert the byte code into machine code
    - PVM interpreter bytecode and excecute on the system
- Excecution on Platform

## Literals
Literal means value or data which is assigned to the variable.

- Number
    - Int [10, 15, 56, etc]
    - Float [10.0, 53.0, etc]

## Number system
ALways print in the form of decimal

- Decimal 
- Octal -> 0O
- Binary -> 0B
- Hexadecimal -> 0X

We can't assign prefix to the float value

## Website for learning
- Codingbat.com
- Excersim.com
- Heackerearth.com (Recommanded by tnp)