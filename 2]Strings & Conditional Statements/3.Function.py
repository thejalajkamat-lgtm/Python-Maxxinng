str = "i am a coder"

print(str.endswith("er")) #returns true if str ends with substr
print(str.capitalize()) #capitalizes 1st char
print(str.replace("a", "o")) #replaces all occurences of old with new
print(str.replace("coder", "mafia"))
print(str.find("a")) #returns 1st index of 1st occurence
print(str.find("coder"))
print(str.find("Q")) #gives -1 if the str doesn't exist
print(str.count("a")) #counts the occurence of substr in string