# class Student:
#     college_name = "KIT CoEK"

#     def __init__(self):
#         pass

#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
    
#     def welcome(self):
#         print("Welcome student, ", self.name)

#     def get_marks(self):
#         return self.marks


# s1 = Student("Karan", 97)
# print(s1.name, s1.marks )
# s2 = Student("Jalaj",100)
# print(s2.name, s2.marks, s1.college_name)
# s1.welcome()
# print(s2.gLKet_marks())


# class Baalak:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks
#     @staticmethod
#     def hello():
#         print("Hello World")
#     def get_avg(self):
#         sum = 0
#         for val in self.marks:
#             sum += val
#         print(f"Hi {self.name} your average marks is {sum/3}")
# s1 = Baalak("Jalaj", [90,91,92])
# s1.get_avg()

# class Account:
#     def __init__(self, bal, acc):
#         self.balance = bal
#         self.account_no = acc
#     #debit method
#     def debit(self, amount):
#         self.balance -= amount
#         print("Rs. ", amount, "was debited") 
#         print("total balance = ", self.balance)
#     #credit method
#     def credit(self, amount):
#         self.balance += amount
#         print("Rs,", amount, "was credited")
#         print("total balance = ", self.balance)
# acc1 =Account(10000, 12345)
# acc1.debit(1000)
# acc1.credit(500)

class A:
    varA = "Welcome to class A"
class B:
    varB = "Welcome to class B"
class C(A, B):
    varC = "Welcome to class C"
c1 = C()
print(c1.varB)