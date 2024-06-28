# Approach_1: Hardcoded Values
num1 = 20
num2 = 10

def addition():
  add = num1 + num2
  print("Addition of two numbers: " + str(add))

def subtraction():
  sub = num1 + num2
  print("Subtraction of two numbers: " + str(sub))

addition()
subtraction()

###########################################################

# Approach_2: Input to the function
def addition(num1,num2):
  add = num1 + num2
  return add

def subtraction(num1,num2):
  sub = num1 - num2
  return sub

add = addition(10,20)
print("Addition of two numbers: " + str(add))
sub = subtraction(15,30)
print("Subtractiontion of two numbers: " + str(sub))


