collection1 = {1, 2, 2, 2, 3, "hello", "world", "world"}
collection2 = {1, 5, 2, 100, 3, "Jalaj", "world", "world"}

collection1.add(5)   #adds 5 to the set
print(collection1)

collection1.remove(5)    #removes 5 from the set
print(collection1)

collection1.pop()    #removes a random item from the set
print(collection1)

collection1.union()    #removes a random item from the set
print(collection1)

print(collection1.union(collection2))   #combines both set values and returns new set

print(collection1.intersection(collection2))   #combines common values and returns new set
