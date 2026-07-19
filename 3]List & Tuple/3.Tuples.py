'''TUPLES are a built in data type thta let's us create immutable sequence of values. Here we use () instead of [] to create a tuple.'''

tup = (2, 1, 3, 1)
print(tup[0], tup[1], type(tup))

''' tup[0] = 5
   print(tup)
This will give an error as tuples are immutable unlike lists '''

#And if we want one element tuple then we need a comma after the element otherwise the type of the variable will not be tuple.

#It will be integer or float or string whatever we have assigned in the brackets but if we have many elements then comma at the end is purely optional

#Slicing of tuples is same as slicing of string or lists