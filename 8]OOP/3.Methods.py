'''class Student:    
    college_name="KIT CoEK" 
  
    def __init__(self):
        pass

    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
        print("Adding new student in Database..")

    def welcome(self):             # M E T H O D S
        print("welcome student,", self.name)

    def get_marks(self):           # M E T H O D S
        return self.marks

s1 = Student("Jalaj Kamat", 34)
print(s1.name, s1.marks, s1.college_name, s1.welcome())   

s2 = Student("Arjun", 88)
print(s2.name, s2.marks, s2.college_name)''' 

#Create a student class that takes name & marks of 3 subjects as arguments in constructor. The create a method to print the average
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def get_avg(self):
        sum = 0
        for val in self.marks:
            sum += val
        print(f"{self.name} your avg score is : {sum/3}")

s1 = Student("Jalaj Kamat", [99, 98, 97])
s1.get_avg()

s1.name = "Niraj Kamat"
s1.get_avg()

''' I M P O R T A N T '''
#Abstraction - Hiding the implmentation details of a class and only showing the essential features to the user
#Encapulation - Wrapping data and functions into a single unit(object)