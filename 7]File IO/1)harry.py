f = open("myfile.txt", "a")
f.write("Hello Jalaj")
# text = f.read()
# print(text)
f.close()

with open("myfile.txt", "a") as f:
    f.write("heyy I am inside with")