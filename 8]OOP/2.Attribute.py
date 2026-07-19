'''CLASS & INSTANCE ATTRIBUTES'''
#Creating Class
class Student:    #generally start with capital letter
    college_name="KIT CoEK" #class attribute(common for all objects)
    #Default constructor
    def __init__(self):
        pass

    #parameterized constuctor
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database..")

#Creating object
s1 = Student("Jalaj Kamat", 34)
print(s1.name, s1.marks, s1.college_name)   #Jalaj Kamat

s2 = Student("Arjun", 88)
print(s2.name, s2.marks, s2.college_name)   #Jalaj Kamat