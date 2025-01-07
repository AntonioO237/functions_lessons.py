# # Functions are ways to wrap your code
# # Into resuable units

# # How you define a function:
# # I only define the function ONCE!!!
# # Whatever I pass inside the parentheses is called a parameter
# # A parameter is a placeholder for future information
# def sayHello(name,age,address):
#     print(f"say hello {name}")
#     print(f"Hello Governer, your address is {address}")
#     print(f"welcome back {name}")
#     print(f"your age is {age}")

# # Once you define a function yuou must call of invoke the function
# # When I pass in information into the called funtion, it's called an arguement
# sayHello("Tony", 17, "345 North Lawndale")
# sayHello("Olvera", 34, "345 North Lawndale")


# # EXAMPLE: 
# def determineEligibility(age):
#     # If your age is over 18, you can vote
#     # Otherwise you can't
#     if age >= 18:
#         print("You can vote")
#     else: 
#         print("You have to wait")

# determineEligibility(12)
# determineEligibility(15)
# determineEligibility(19)

# def willYouGraduate(GPA,credits,SAT):
#     # GPA: number variable
#     # credits: number variable
#     # Passed SAT: Boolean
#     if (GPA == 3.0) and (credits>=28) and (SAT == True):
#         print("You passed. Good luck in college")
#     elif (GPA < 3.0) or (credits < 28) or (SAT != True):
#         print("You suck! You'll never make it")
#     else:
#         print("Talk to your counselor")
    
# willYouGraduate(2.8, 15, True)
# willYouGraduate(3.8, 27, True)
# willYouGraduate(3.1, 28, True)

# Return = statement uysed to end a function and send a result back to the caller
def add(x, y):
    z = x + y
    return z

def subtract(x, y):
    z = x - y
    return z

def multiply(x, y):
    z = x * y
    return z

def divide(x, y):
    z = x / y
    return z

print(add(1, 2))
print(subtract(1, 2))
print(multiply(1, 2))
print(divide(1, 2))

def create_name(first, last):
    first = first.capitalize()
    last = last.capitalize()
    return first + " " + last

full_name = create_name("Spongebob", "Squarepants")
print(full_name)

# MORE EDITS
