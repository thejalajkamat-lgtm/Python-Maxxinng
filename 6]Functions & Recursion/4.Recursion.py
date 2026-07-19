#RECURSION is when a function calls itself repeatedly
def show(n):
    if(n == 0):   #BASE CASE
        return
    print(n)
    show(n-1)
show(5) #5, 4, 3, 2, 1 in one call only without loop



#return n!    3! =   2!   * 3
#             n! = (n-1)! * n 
print("\n")
def fact(n):
    if(n == 0 or n == 1):
        return 1
    return fact(n-1)*n
print(fact(5))
    
# #FACTORIAL USING FUNCTION
# def cal_fact(n):
#     result = 1
#     for i in range (1, n+1):
#         result *= i
#     return result
# num = cal_fact(5)
# print(num)