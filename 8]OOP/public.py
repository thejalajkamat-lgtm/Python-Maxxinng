# class Account:
#     def __init__(self, acc_no, acc_pass):
#         self.acc_no = acc_no
#         self.__acc_pass = acc_pass
#     def reset_pass(self):
#         print(self.__acc_pass)  #private __

# acc1 = Account("12345", "abcde")
# print(acc1.acc_no)
# # print(acc1.__acc_pass)  gives error
# print(acc1.reset_pass())



# class A:
#     varA = "Welcome to class A"
# class B:
#     varB = "Welcome to class B"
# class C(A, B):              #C has inherited properties of A and B class
#     varC = "Welcome to class C"
# c1 = C()
# print(c1.varB)    


class Car():
    def __init__(self, type):
        self.type = type
    @staticmethod
    def start():
        print("car started")
    @staticmethod
    def stop():
        print("car stopped")
class ToyotaCar(Car):
    def __init__(self, brand, type):
        self.brand = brand
        super().__init__(type)
class Fortuner(ToyotaCar):
    def __init__(self, type):
        self.type = type
c1 = Fortuner("Legender")
c1.start()
c2 = ToyotaCar("Camry", "hybrid")
print(c2.type, c2.brand)