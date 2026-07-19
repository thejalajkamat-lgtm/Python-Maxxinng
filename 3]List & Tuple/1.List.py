'''marks1 = 94.3
marks2 = 87.5
marks3 = 95.2
marks4 = 66.4
marks5 = 45.1
 #IS EQUIVALENT TO WRITING
marks = [94.3, 87.5, 95.2, 66.4, 45.1]
print(marks, "  ", type(marks))
print(marks[0], marks[1], len(marks))'''

student = ["Karan", 95.4, 17, "Delhi"]
print(student[0], type(student), len(student))
student[0] = "Arjun"  #for lists we can change the value
print(student)
#list is mutable and string is immutable 

marks =  [87, 64, 33, 95, 76]
print(marks[1:4])
print(marks[1: ])   #Slicing of lists
print(marks[:4])
print(marks[-3:-1])


'''# Accept elements from the user
lst = input("Enter elements separated by space: ").split()

# Print alternate elements
print("Alternate elements in the list are:")
for i in range(0, len(lst), 2):
    print(lst[i], end=" ")'''
