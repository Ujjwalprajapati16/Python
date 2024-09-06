# python (Major Topics)

- Tokens
- Data  types
- Flow control Statements
- Functions
- Modules
- Time, datetime, calender
- File handling
- SQL
- Database connectivity
- OOPS (Very important)
- REGEX
- Multithreading and concurrency (Not to tell in interview)
- Exception handling
- Tkinter

## Project
- Frontend 
- Backend
- Database
- Data Analysis
- Deployment


```python
a = 100
print(a)
a = 100/10
```
```python
type(a)
<class 'float'>
```
```python
id(a)
2327110625616
b = 100/10
id(b)
2327110622768
```

if calculated value id will be different.

## Token

- Keywords
- Litreals/constants
- Identifiers
- Operators

### Identifiers
Name in python is known as identifier.
Used for identification purpose only.
Such as 
- variable name
- class name
- function name
- object name
- class name
- etc.

#### Rules to define identifiers

- We can use A-Z, a-z, 0-9
```python
temp = 100
```
- We can't start identifiers with numbers
```python
9temp = 100
```
- Identifiers are case sensitive
```python
temp = 100
Temp = 200
tEMP = 300
TEMP = 400
```
- No limit in length of identifiers
```python
temptemptemptemp = 100
```
- We cannot use keywords as identifier
```python
while = 100
SyntaxError: invalid syntax
```
### Keywords
The reserved words may not be used as identifiers or variable or any other identifiers names.
All the Python keywords contain lowercase letters only.

- and
- or

(Many more......)

### Operators
Operators which perform some operation

Types of operators:- 
- Arithmetic Operators
- Comparison Operators
-
-
#### Arithmetic operators
- Addition (+)
```python
a = 10
b = 20
print(a+b) # 30
```
- Subtraction (-)
```python
a = 10
b = 20
print(b-a) #10 
```
- Multiplication (*)
```python
a = 9
b = 2
print(a*b) # 18
```
- Division (/)
```python
a = 9
b = 2
print(a/b) # 4.5
```
- Modulus (%)
```python
a = 9
b = 2
c = a%b
print(c) # 1
print(type(c)) # <class 'int'>
```
- Exponent (**)
```python
a = 9
b = 2
c = a**b
print(c) # 81
print(type(c)) # <class 'int'>
```
- Floor division (//)
```python
a = 9
b = 2
c = a//b
print(c) # 4
print(type(c)) # <class 'int'>
```

#### Comparison Operators
- Equal to (==)
```python
a = 9
b = 2
c = a == b
print(c) # False
print(type(c)) # <class 'bool'>
```
- Doesn't equal to (!=)
```python
a = 9
b = 2
c = a != b
print(c) # True
print(type(c)) # <class 'bool'>
```
- less than (<)
```python
a = 9
b = 2
c = a < b
print(c) # False
print(type(c)) # <class 'bool'>
```
- greater than (>)
```python
a = 9
b = 2
c = a > b
print(c) # True
print(type(c)) # <class 'bool'>
```
- greater than or equal (<=)
```python
a = 9
b = 2
c = a <>= b
print(c) # False
print(type(c)) # <class 'bool'>
```
- less than or equal to (>=)
```python
a = 9
b = 2
c = a >= b
print(c) # True
print(type(c)) # <class 'bool'>
```

#### Assignment operator
- simple assignment (=)
- add and assign (+=)
```python
a = 9
a += 2 # a = a +2
print(a) # 11
```
- subtract and assign (-=)
- multiply and assign (*=)
- divide and assign (/=)
- floor division and assign (//=)

#### Logical operator
- and
    - Both conditons are true then return true otherwise return false
    - If one conditon is false then it will not check second conditon
- or
    - Both conditons are false then return false otherwise return true
    - if one conditon is true then it will not check second conditon
- not
    - if conditon is true then return false
    - if conditon is false then return true


#### Bitwise operator
- compliment (~)
```python
a = 9
print(~a) # -10
```
- and (&)
```python
a = 60
b = 13
print(a&b) # 12
```
- or (|)
```python
a = 60
b = 13
print(a|b) # 61
```
- xor (^)
```python
a = 60
b = 13
print(a^b) # 49
```
