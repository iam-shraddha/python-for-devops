import sys

type = sys.argv[1]

if type == "t2.micro":
   print("Ok, we will create instance for you with 2 cpu")
elif type == "t2.medium":
   print("Ok, we will create instance for you with 4 cpu")
elif type == "t2.xlarge":
   print("Ok, we will create instance for you with 8 cpu")
else:
   print("Please, provide valid instance type")
