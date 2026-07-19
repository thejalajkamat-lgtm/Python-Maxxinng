#Block of statements that perform a specific task
def calc_sum(a, b):    #a & b are parameters
    sum = a + b
    print(sum)
    return sum
calc_sum(10,3)          #10 & 3 are arguments


#Function with no parameter or return value
def print_hello():
    print("Hello")

output=print_hello()
print(output)


#Print average of 3 numbers using function
def calc_sum(a, b, c):    #a & b are parameters
    sum = a + b + c
    avg = sum/3
    print(avg)
    return avg
calc_sum(10,3,2)          #10 & 3 are arguments


#Function to convert Celcius to Fahrenheit
def celcius_to_Fahrenheit(celcius):
    fahrenheit = (celcius * 9/5) + 32
    return fahrenheit
#call function
temp_f = celcius_to_Fahrenheit(25)
print(temp_f,"°F")


#ODD EVEN
def num(n):
    return "EVEN" if n/2==0 else "ODD" 
num1 = num(4)
print(num1)


#GREET HELLO
def greet():
    return f"Hello World"
greeting = greet()
print(greeting)


#FACTORIAL USING FUNCTION
def cal_fact(n):
    result = 1
    for i in range (1, n+1):
        result *= i
    return result
num = cal_fact(5)
print(num)



''' Write a program with a function that accepts a string from the keyboard and creates a new string after converting the character of each word capitalized. For instance, if the sentence is "stop and smell the roses." the output should be "Stop and Smell The Roses''' 
def transform_to_title_case(sentence):
    # 1. Split the sentence into a list of words
    words = sentence.split()
    
    # 2. Capitalize the first letter of each word using list comprehension
    capitalized_words = [word.capitalize() for word in words]
    
    # 3. Join the words back into a single string with spaces
    result = " ".join(capitalized_words)
    
    # 4. Return the new string
    return result

# --- Main Program ---
user_input = input("Enter a sentence: ")
transformed_sentence = transform_to_title_case(user_input)

print(f"Original: {user_input}")
print(f"Modified: {transformed_sentence}")