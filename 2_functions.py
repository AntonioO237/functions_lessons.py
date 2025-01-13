# Create Functions Practice #1
# Declare a function called greet, which every time it is called prints "Hello world!"
def greet():
    print("Hello world!")

greet()

# You should only define the function, you should not call it later.

# Create Functions Practice #2
# Declare a Function: Create a function called welcome that takes a person's name as an argument. This function should print "Welcome {name}!" whenever it is called.

# Create a Variable: Define a variable named name and store any name of your choice in it.

# Note: Only define the function and create the variable. Do not call the function afterwards.

def count_even(numbers):
    numbers = []
    even_numbers = 0
    for n in numbers:
        if n % 2 == 0:
            even_numbers += 1
            return even_numbers
        else:
            pass
        
code = count_even([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(code)




# Create Functions Practice #3
# Declare a function called square, that takes any number as an argument, and each time it is called, it prints the square of that number on the screen (that is, the value to the second power).

# The name of the argument that this function must take is number. Create this variable and assign it any number.

# You should only define the function and create the variable, you should not call the function afterwards.