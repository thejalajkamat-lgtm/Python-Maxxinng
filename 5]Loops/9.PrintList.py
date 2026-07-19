#Q1] Print the elements of the following list using a loop  [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
for val in list:
    print(val)
    
    
#Q1]Search for a number x in this tuple using loop: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("\n")
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 49)
x = 49

idx = 0
for el in tup:
    if(el == 49):
        print("number found at idx", idx)
        idx += 1


