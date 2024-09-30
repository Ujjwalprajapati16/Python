# Day 11

# Campus question
## Question 1

    north
east    west
    south

- east => postive x
- west => negative x
- north => negative y
- south => positive y

lrm => left, right, move
left 90 degree and right 90 degree and move forward by one unit

## Inputs

- input1(integer) => x = 3
- input2(integer) => y = 3
- input3(string) => startingPoint = "2-2-e"
- input4(string) => path = "r m l m l m"

## Output

- output(string) => "3-2-n"

## Explanation

1. starting point is 2-2-e
2. the path is r -> 2-2-s
3. the path is m -> 2-1-s
4. the path is l -> 2-1-e
5. the path is m ->

## Case

- x = 3
- y = 4
- startingPoint = "2-2-e"
- path = "r m l m l m r m"

## Output

- "ERROR"

## Code
```python 
for i in path:
    if i == "l":
        start[2] = {"N": "W", "W": "S", "S": "E", "E": "N"}[start[2]]
    elif i == "r":
        start[2] = {"N": "E", "E": "S", "S": "W", "W": "N"}[start[2]]
    elif i == "m":
        dx, dy = directions[start[2]]
        new_x, new_y = int(start[0]) + dx, int(start[1]) + dy
        if new_x in x_range and new_y in y_range:
            start[0], start[1] = str(new_x), str(new_y)
        else:
            print("ERROR")
            break
else:
    print("-".join(start))
```