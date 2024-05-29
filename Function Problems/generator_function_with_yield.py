def even_generator(limits):
    for i in range(2, limits+1):
        if i % 2 == 0:
            yield i
            
for num in even_generator(10):
    print(num)