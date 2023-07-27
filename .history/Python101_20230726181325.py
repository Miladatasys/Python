print("Hello, world!")

#python is case sensitive
#Types of data in python: str, int, bool
#Conversion to type: float(),int(), bool(), str()

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
print(course)
print(course.find('for'))
print(course.replace('for',))

