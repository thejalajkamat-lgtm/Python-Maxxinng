#Range functions returns a sequence of numbers, starting from 0 by default, and increments by 1 (by default), and stops before a specified number  eg.range(5) = 0, 1, 2, 3, 4

seq = range(5)
# '''print(seq[0])
#    print(seq[1])
#    print(seq[2])
#    print(seq[3])'''
for i in seq:
     print(i)

'''for i in range(10):  #range(stop)
         print(i) '''
print("\n")
for i in range(2,10):  #range(start,stop)
         print(i)

print("\n")
for i in range(2,10,2):  #range(start,stop,step size)
         print(i)