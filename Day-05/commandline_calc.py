# Calculator program using command line argument
import sys

def addition(num1,num2):
   add = num1 + num2
   return add

def subtraction(num1,num2):
   sub = num1 - num2
   return sub

def multiplication(num1,num2):
   mul = num * num2
   return mul

num1 = float(sys.argv[1])
operation = sys.argv[2]
num2 = float(sys.argv[3])

if operation == "addition":
  output = addition(num1,num2)
  print("Addition of two numbers: " + str(output))

elif operation == "subtraction":
  output  = subtraction(num1,num2)
  print("Subtractiontion of two numbers: " + str(otput))

elif operation == "multiplication":
  output = multiplication(num1,num2)
  print("Multiplication of two numbers: " + str(output))

else:
  print("Please provide valid operation")
# execution: python commandline_calc.py 10 addition 40
#output: Addition of two numbers: 50
