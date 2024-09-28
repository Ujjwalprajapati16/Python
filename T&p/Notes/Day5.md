# Python Data Types

Python has several built-in data types. Here are the most common ones with examples:

## 1. Numeric Types

### Integer (int)
Whole numbers, positive or negative, without decimals.

```python
x = 5
y = -10
print(type(x))  # Output: <class 'int'>
```

### Float
Numbers with decimal points.

```python
a = 3.14
b = -0.5
print(type(a))  # Output: <class 'float'>
```

### Complex
Numbers with a real and imaginary part.

```python
z = 2 + 3j
print(type(z))  # Output: <class 'complex'>
```

## 2. Sequence Types

### List
Ordered, mutable sequences.

```python
fruits = ["apple", "banana", "cherry"]
print(type(fruits))  # Output: <class 'list'>
fruits.append("date")
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']
```

### Tuple
Ordered, immutable sequences.

```python
coordinates = (10, 20)
print(type(coordinates))  # Output: <class 'tuple'>
```

### String
Immutable sequences of Unicode characters.

```python
greeting = "Hello, World!"
print(type(greeting))  # Output: <class 'str'>
```

## 3. Mapping Type

### Dictionary
Key-value pairs, unordered and mutable.

```python
person = {"name": "Alice", "age": 30, "city": "New York"}
print(type(person))  # Output: <class 'dict'>
person["job"] = "Engineer"
print(person)  # Output: {'name': 'Alice', 'age': 30, 'city': 'New York', 'job': 'Engineer'}
```

## 4. Set Types

### Set
Unordered collection of unique elements.

```python
unique_numbers = {1, 2, 3, 3, 4, 5}
print(type(unique_numbers))  # Output: <class 'set'>
print(unique_numbers)  # Output: {1, 2, 3, 4, 5}
```

### Frozenset
Immutable version of a set.

```python
frozen = frozenset([1, 2, 3, 3, 4, 5])
print(type(frozen))  # Output: <class 'frozenset'>
```

## 5. Boolean Type

### Bool
Represents True or False values.

```python
is_python_fun = True
is_java_fun = False
print(type(is_python_fun))  # Output: <class 'bool'>
```

## 6. None Type

### NoneType
Represents the absence of a value.

```python
result = None
print(type(result))  # Output: <class 'NoneType'>
```

## Example Program

Here's a small program that demonstrates the use of various data types:

```python
def demonstrate_data_types():
    # Numeric types
    age = 30
    height = 5.9
    complex_num = 1 + 2j

    # Sequence types
    fruits = ["apple", "banana", "cherry"]
    coordinates = (10, 20)
    name = "Alice"

    # Mapping type
    person = {"name": name, "age": age, "height": height}

    # Set types
    unique_numbers = {1, 2, 3, 4, 5, 5}
    frozen_set = frozenset([1, 2, 3, 3, 4, 5])

    # Boolean type
    is_student = True

    # None type
    result = None

    # Print all variables and their types
    variables = [age, height, complex_num, fruits, coordinates, name, person, 
                 unique_numbers, frozen_set, is_student, result]
    
    for var in variables:
        print(f"Value: {var}, Type: {type(var)}")

# Run the function
demonstrate_data_types()
```

This program creates variables of different data types and then prints each variable along with its type, demonstrating the variety of data types available in Python.