## Functions in Python
## A function is a resuable block of codes that performs a specific task
##syntax of a function
def function_name(): ##'def' keyword use to define a function
    print('function statement') ##statement that belong to the function
function_name() ##call the function
def greet():
    print('Hola')
greet()
##Create a function that can be called 3 times
def welcome():
    print('welcome to AI Data Engineering')
welcome()
welcome()
welcome()
##Function with one parameters
def welcome(name):
    print(name, 'You are welcome')
welcome('Carl')
welcome('Ann')
welcome('Marcial')
##Functions with mutiple parameters
def student_info(name, age, course):
    print('Name:', name)
    print('Age:', age)
    print('Course:', course)
student_info('Happiness', 25, 'Data Engineering')
#3Function with multiple statements
def introduction():
    print('Welcome to Python')
    print('Today we are learning functions')
    print('Functions makes coding easier')
introduction()
##Functions with two parameters using calculations
def total(num1, num2):
    print(num1 + num2)
total(3, 7)
##Calculate the area of a rectangle using function
def area(length, width):
    return(length * width)
rectangle = area(6, 12)
print(rectangle)
##Calculate annual salary
def annual_salary(monthly_salary):
    return monthly_salary * 12
salary = annual_salary(5000)
print(salary)
##Calculating Employee bonus
def employee_bonus(salary):
    return salary * 0.10
bonus = employee_bonus(5000)
print(bonus)
##Combining loops and function
def greet(name):
    print('welcome', name)
students = ['Ann', 'Carl', 'Mercial', 'Ernest', 'Happiness']
for student in students:
    greet(student)