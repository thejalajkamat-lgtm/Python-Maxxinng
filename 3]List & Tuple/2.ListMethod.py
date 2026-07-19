list = [2, 1, 3]

list.append(4)        #adds one element at the end
print(list)           # [2, 1, 3, 4]

list.sort()           #sorts in ascending order
print(list)           # [1, 2, 3, 4]

list.sort(reverse=True)  #sorts in descending order
print(list)              # [4, 3, 2, 1]

list.reverse()        #reverses list
print(list)           # [1, 2, 3, 4]

list.insert(2,"3L")   #inserts element at index list.insert(idx,el) 
print(list)           # [1, 2, '3L', 3, 4]

list.remove(3)    #removes occurence of the mentioned element
print(list)       # [1, 2, '3L', 4]

list.pop(3)    #removes element at index mentioned
print(list)    # [1, 2, '3L']

''' THESE WILL PRINT NONE
   print(list.append(4)) 
   print(list.sort())  
   print(list.sort(reverse=True)) 
   print(list.reverse()) '''

# Find and display the largest number of a list without using built-in function 
# max(). Your program should ask the user to input values in the list from the 
# keyboard. 
# Get input from the user
user_input = input("Enter numbers separated by spaces: ")

# Convert the string input into a list of actual numbers (floats or ints)
numbers = [float(i) for i in user_input.split()]

# Check if the list is empty to avoid errors
if len(numbers) == 0:
    print("The list is empty.")
else:
    # 1. Assume the first number is the largest
    largest = numbers[0]

    # 2. Iterate through the list to compare
    for num in numbers:
        if num > largest:
            largest = num

    # 3. Display the result
    print("The largest number in the list is:", largest)