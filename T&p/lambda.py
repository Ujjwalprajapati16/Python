# a = ["hello", "i'm", "Pikachu"]
# res = list(map(lambda x : x.upper(), a))
# print(res)

# # adding two corresponding elements to list
# l1 = [1, 2, 3]
# l2 = [4, 5, 6]

# res = list(map(lambda x,y : x+y, l1, l2))
# print(res)

# output = [5, 7, 9]


# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = list(filter(lambda x : x%2==0, l1))
# print(res)

# l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# res = list(map(lambda x : x%2==0, l1))
# print(res)


# l1 = ["hello", "pikachu", "charizard", "ash"]
# res = list(filter(lambda x : len(x) > 5, l1))
# print(res)

from functools import reduce

l1 = [1, 2, 8, 6, 3, 4, 5, 9, 11, 7]
res = reduce(lambda x, y : max(x, y), l1)
print(res) # 11