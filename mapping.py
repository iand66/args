x = [1,2,3,4,5]

mp = map(lambda i: i + 2, x) # Adds 2 to each element of x
print(list(mp))

fl = filter(lambda i: i % 2 == 0, x) # Is divisible by 2?
print(list(fl))