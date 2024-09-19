# Day 8

## Methods of string data type

### functions

1. len() => its a function return length of string.

```python
a = "djfhbvh"
len(a)
7
```

1. str() => convert a value into string

```python
b = str(a)
print(a) # 'hello'
```

### methods

2. islower() => its a method returns if all characters are lower case in bool.

```python
a = "djfhbvh"
a.islower() # True
```

3. isupper() =>

```python
a = "Hello"
a.isupper() # False
```

4. upper() => make string in upper case
5. lower() => make string in lower case
6. title() => capitalize first character of each word.
7. istitle() => retuns true if first character is capital
8. capitalize() => capitalize first letter of string or sentence.
9. strip() => it remove the leading and trailing space.

```python
a = "       hello          "
a.strip() # 'hello'
```

10. replace(oldValue, newValue) => replace old with new
    And works as a replace all.

```python
a = "this is a test string"
a.replace("test", "best") # 'this is a best string'
```

11. split() =>

```python
a = 'this is a test string'
a.split(" ") # ['this', 'is', 'a', 'test', 'string']
```

- Ques

```python
a = 'this is a test string'
len(a.split("i")) # 4
```

12. join()

```python
a = ["Hello", "world"]
b = "-"
b.join(a)
'Hello-world'
```

13. find() => to find the index of a string

```python
a = "Its a test string"
a.find("is")
-1
a.find("s")
2
```

14. startswith()

```python
a.startswith("Its") # True
a.startswith("th") # False
```

15. endswith()

```python
a.endswith("ing")
True
a.endswith("l")
False
```

16. isdigit() => to check the digit or number in string

17. isalpha() => to check the alphabet in the string

```python
a = "hello"
a.isalpha() # True
```

18. isalnum() => to check the alphabet and number in string

```python
a = "hello123"
a.isalnum() # True
```

19. splitlines()

```python
a = "hello\nworld"
a.splitlines()
['hello', 'world']
```

20. zfill() => to add 0 in front of string

```python
a = "hello"
a.zfill(10)
'000000hello'
```

21. ljust() => left justify

```python
a = "hello"
a.ljust(10 , " ")
'hello     '
```

22. rjust() => right justify

```python
a = "hello"
a.rjust(10) # '     hello'
a.rjust(10, "-") # '-----hello'
```

## Ques

1. Count number of characters of a string
```python
a = "Hello World"
count = 0
for i in a:
    if i.isalnum():
        count += 1

print(count) # 10
```

2. Replace the all space with hypen.
```python
a = "Hello World"
b = a.replace(" ", "-")
print(b) # 'Hello-World'
```

3. Count the number of vowels in a string.
```python
a = "Hello World"
count = 0
for i in a:
    if i in "aeiouAEIOU":
        count += 1
print(count) # 3
```

4. Check if two string are anagram.
```python
a = "silent"
b = "listen"
print(a == b) # True
```

5. Calculate the length of string without using function.
```python
a =  "Hello World"
count = 0
for i in a:
    count += 1
print(count) # 11
```

6. Calculate the number of words and the number of characters present in a string.
```python
a = "Hello World"
word = len(a.split(" "))
count = 0
for i in a:
    if i.isalnum():
        count += 1

print(count) # 10
print(word) # 2
```

7. Count the number of lowercase character of a string.

8. Create the new string made of first two and last two characters from a given string.