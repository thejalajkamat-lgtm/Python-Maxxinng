print("\n")
str = "apnacollegejalaj"
for ch in str:
    if(ch == 'o'):
        print("o found")
        break
    print(ch)
else:  #else is needed in cases where we need to use break
    print("END")