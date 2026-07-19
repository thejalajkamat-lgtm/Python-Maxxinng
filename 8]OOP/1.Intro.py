'''To map with real world scenarios, we started using objects in code. This is called Object Oriented Programming. List, Strings are objects that we have already used. '''

''' CLASS & OBJECT IN PYTHON
  Class is blueprint for creating objects.'''

#Creating Class
class Student:    #generally start with capital letter
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
print(s1.name, s1.marks)   #Jalaj Kamat

s2 = Student("Arjun", 88)
print(s2.name, s2.marks)   #Jalaj Kamat