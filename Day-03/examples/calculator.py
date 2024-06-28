# Global scope variables
a = 10
b = 5

def addition():
  add = a+b
  print("Addition of two numbers is " + str(add))
def subtraction():
  sub = a-b
 print("Addition of two numbers is " + str(sub))
addition()
subtraction()
#Output: 15 & 5

###########################################

# Local scope variables
def addition():
  a=10
  b=5
  add = a+b
 print("Addition of two numbers is " + str(add))

def subtraction():
  sub = a-b
 print("Addition of two numbers is " + str(sub))

addition()
subtraction()
#Output: Error

################################################

# Global and Local scope variables
a = 10
b = 5
def addition():
  c = 15
  add = a+b+c
  print("Addition of two numbers is " + str(add))

def subtraction():
  sub = a-b
  print("Addition of two numbers is " + str(sub))

addition()
subtraction()
#Output: 30 & 5

