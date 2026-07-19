student = {
    "name" : "Jalaj Kamat",
    "subjects" : {
       "physics" : 98,
       "chemistry" : 76,    #Nested Dictionary is dictionary under another
       "maths" : 89,
    }
}

print(student.keys()) #returns all keys in the dictionary(not nested)
print(student.values()) #returns all values in the dictionary
print(student.items()) #returns all (key,val) pairs as tuples
print(len(student)) #returns length of dictionary(not nested)
print(student.get("name")) #returns the key according to value(gives none if key is not found)
print(student["name"])  #same as above but it gives error if key not found and the entire code stops to function, so din't use this method
student.update({"city" : "Kolhapur"})
print(student) #returns the specified items to the dictionary