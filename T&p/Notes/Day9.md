# Day 9

## Ques

1. write a program to identify the set of possible words.

   - input1 = "Fi_er"
   - input2 = "Fever:filer:Filter:Fixer:fiber:Fiber:tailor:offer"

   - output = "Filter:Fixer:Fiber"

   - Note : if none of the words in input2 are possible candidates to replace input1. The output string should contain the string "ERROR-009"

```python
input1 = "Fi_er"
input2 = "Fever:filer:Filter:Fixer:Fiber:tailor:offer"

index = input1.find("_")
words = input2.upper().split(":")
res = ""

for word in words:
    temp = input1.upper()
    ch = word[index]
    temp = temp.replace("_", ch)
    if temp == word:
        if res == "":
            res = word
        else :
            res = res + ":" + word

print(res)
```

## Data Type

### List

1. List is a **mutable** object.
2. List work on the basis of **indexing** that is same as string.
3. In python, we can denot list as **square bracktes([])**.
4. we can insert **hetrogenous value**(any type of value) in the list.

```python
a = ["heelo", 10, 10.5, True]
```

5. **Duplicacy** allowed in list data type.

#### list operator

- (+) (merge)

```python
a = [1, 2]
b = [3, 4]
a + b # [1, 2, 3, 4]
```

- (*) (repetation of value)
    - repeat list elements

```python
a = [1, 2]
a * 4 # [1, 2, 1, 2, 1, 2, 1, 2]
```

> [!NOTE]
> if we have 2 two values and try to access 2nd index then pvm generate an error.

- slice operation [start:end:steps]

```python
a = [1, 5, 8, 9, 6, 11, 4]
a[2:0] # []
a[2:] # [8, 9, 6, 11, 4]
a[:5] # [1, 5, 8, 9, 6]
a[::2] # [1, 8, 6, 4]
a[::-1] # [4, 11, 6, 9, 8, 5, 1] (reverse the list)
```

- in operator
```python
a = [1, 5, 8, 9, 6, 11, 4]
5 in a # True
3 not in a # True
```

#### Functions
1. **len(list)** => size of the list.
2. **max(list)** => return maximum value in list.
3. **min(list)** => reutrn minimun value in list.
4. **list(string)** => to convert a string into list.
    - it only make iterable variable into list.
5. **sum(list)** => return the sum of list.
6. **sorted(list)** => it sort the list in ascending order
    - if want to sort in descending order.
    - **sorted(list, reverse=True)**
7. **enumerate(list)** => it returns the list into tuple.
8. **zip(list1, list2)** => it returns object of combined of list in tuple where each index are combined.
    - list1 and list2 should be of same length or it only return the min length.
    - list(zip(list1, list2))
9. **reversed(list)** => it returns list in reverse order.

#### Methods of list
1. **append(value)** => it appends the value in the list.
    - add an element to the end of the list.
    - list.append(value)
2. **extend(list2)** => it extend the list by appending the element of another list.
    - list.extend(list2)
3. **insert(index, value)** => it insert the value at the given index.
    - list.insert(index, value)
4. **remove(value)** => it remove the value from the list.
    - list.remove(value)
    - it removes first occurance of the specific element.
5. **pop(index)** => it remove the element at the given index.
    - list.pop(index)
    - if index is not provided, it removes the last element of the list.
6. **index(value)** => it returns the index of the value.
    - list.index(value)
7. **count(value)** => it returns the count of the value.
    - list.count(value)
    - it return number of occurance of specific element.
8. **clear()** => it empty the list.