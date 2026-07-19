'''Types of files :- 1.Text Files: .txt, .docx, .log etc....
                   2.Binary Files: .mp4, .mov, .png, .jpeg etc....'''

#OPEN, READ & CLOSE FILE --> f = open("file_name", "mode")
f = open("demo.txt", "r")
data = f.read()    #read reads entire file
print(data, type(data)) #My name is Jalaj Kamat.
                        #I am learning Python.

line1 = f.readline()  #readline reads one line at a time
print(line1)  #My name is Jalaj Kamat.

line2 = f.readline()
print(line2)    #I am learning Python.

line3 = f.readline()
print(line3)    #Empty because we don't have 3rd line in demo.txt

'''f = open("demo.txt", "w")  w --> write i.e replace original file
f.write("I want to learn JS tomorrow")   #I want to learn JS tomorrow(inside demo.txt) '''


'''f = open("demo.txt", "a") a --> append i.e add at the end
f.write("Then I will move to ReactJS") My name is Jalaj Kamat.
                                       I am learning Python.
                                       Then I will move to ReactJS
                                       (inside demo.txt) '''


f.close()  #MANNERS but not needed when we use with(will see below)

''' r -- open for reading(default)
    w -- open for writing, truncationg the file first
    x -- create a new file and open it for writing
    a -- open for writing, appending to the end of the file if it exists
    b -- binary mode
    t -- text mode
    + -- open a disk file for updating (reading and writing)
    r+ -- Read & overwrite on the text present in the file(no truncate)
    w+ -- opens in truncated mode(wipes out everything)
    a+ -- Read & Append(no truncate)'''


# W I T H     S Y N T A X
with open("demo.txt", "r") as f:
    data = f.read()
    print(data)