#WAP to check if a list contains a palindrome of elements eg.[1, 2, 3, 2, 1] is palindrome aka reverse is same

#LOGIC here is to copy the list and then reverse the copied list and then compare both the lists if they are same or not 

list1 = [1, 2, 1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else :
    print("not palindrome")



list2 = [1, 2, 3]

copy_list2 = list2.copy()
copy_list2.reverse()

if(copy_list2 == list2):
    print("palindrome")
else :
    print("not palindrome")
