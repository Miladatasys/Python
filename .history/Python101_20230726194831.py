print("Hello, world!")

#python is case sensitive
#Types of data in python: str, int, bool
#Conversion to type: float(),int(), bool(), str()
#Operators: >,<, <=,>=, ==, !=
#Logical operators: and(both expressions return true), or (at least one expression return true), not (inverses any value that we give it)
#Instead of using curly braces {} to represent a block of code, python uses only indentation

#Variables#
age = 20
age = 30
price = 19.95
first_name = "Milan"
is_online = False
print(age)

#exercise
patient_first_name = "John"
patient_last_name = " Smith"
age = 20
is_new_patient = True
print (patient_first_name + patient_last_name)

#Receiving input and store it in a variable
name = input("What is your name? ")
print("Hello " + name)

#Type conversion
birth_year = input("Enter your birth year: ")
age = 2023 - int (birth_year)
print(age)

#exercise
First = 10.1
Second = 20
sum = 20 + float (First)
print(sum)

first = input("First number: ")
second = input("Second number: ")
sum = int (first) + int (second)
print(sum)

first = input("First number: ")
second = input("Second number: ")
sum = float (first) + float (second)
print("Sum: " + str(sum))

first = float(input("First: "))
second = float(input("Second: "))
sum = first + second
print("Sum: " + str(sum))

#Strings and their methods
course = "Python for Beginners"
print(course.upper())
print(course) #it will not change
print(course.find('for'))
print(course.replace('for', '4'))

#Operator 'in' and arithmetic operators
course = 'Python for beginners'
print('Python' in course) # search for the word

print(10 + 3)
print(10 - 3)
print(10 / 3) #Float
print(10 // 3)#n int
print(10 % 3)#remainder
print(10 ** 3)#raised to the power of 3

x = 10
x = x + 3 #incrementing the value of x by 3 (13x)

#Augmented assignment operator
x = 10
x += 3

x = 10
x -= 3

x = 10
x *= 3

#Operator precedence
x = 10 + 3 * 2 #16
x = (10 + 3) * 2 #60
print(x)

#Comparison operators 
x = 3 > 2#bool
print(x)

x = 3 >= 2
print(x)

x = 3 <= 2
print(x)

x = 3 == 2 #equality operator
print(x)

x = 3 != 2 
print(x)

#Logical operators
price = 25
print(price > 10 and price < 30)

price = 5
print(price > 10 or price < 30)#True

price = 5
print( not price > 10) #true because the not operator

#If statements
temperature = 35

if temperature > 30:
    print("It's a hot day")
    print("Drink plenty of water")

if temperature > 25:
    print("It's a hot day")
    print("Drink plenty of water")
elif temperature > 20
print("Done")#Always execute "Done" after the if block

