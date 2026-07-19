#BREAK is used to terminate the loop when encountered
i = 1
while i <= 5 :
    print (i)
    if(i == 3) :
        break
    i += 1


#CONTINUE terminates execution in the current iteration & continues execution of the loop with the next iteration
print ("\n")
i = 1
while i <= 5 :
    if(i == 3) :
        i+=1
        continue #acts as skip
    print (i)
    i += 1

#Printing odd numbers from 1 to 10
print ("\n")
i = 1
while i <= 10 :
    if(i%2 == 0 ) :
        i+=1
        continue #acts as skip
    print (i)
    i += 1

#Printing even numbers from 1 to 10
print ("\n")
i = 1
while i <= 10 :
    if(i%2 != 0 ) :
        i+=1
        continue #acts as skip
    print (i)
    i += 1    #37:00