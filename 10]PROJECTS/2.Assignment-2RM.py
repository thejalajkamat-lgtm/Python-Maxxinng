# #Write a Pythin program to input student name and marks of 3 subjects. Print name & percentage in output.
# name = input("Enter your name: ")
# marks1 = input ("Enter your marks for maths: ")
# marks2 = input ("Enter your marks for science: ")
# marks3 = input ("Enter your marks for english: ")
# percentage = (int(marks1) + int(marks2) + int(marks3))/3

# print(f"Your name is {name}. Your marks in maths are {marks1}, marks in science are {marks2}, marks in english are {marks3}". So the percentage is {percentage}%)


#Write a python program that collects multiple types of data (eg., name age, height, and student statu) from user input, stores them in a dictionary and then prints out the collected data.
user_data = {}      #initializing a dictionary

user_data['name'] = input("Enter your name: ")
user_data['age'] = int(input("Enter your age: "))
user_data['height'] = float(input("Enter your height: "))
user_data['student'] = input("Are you a student(yes/no): ")

print(user_data)