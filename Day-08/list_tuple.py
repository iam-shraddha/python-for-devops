student_names = ["sonu","monu","tonu","shubu","pillu","chhotu","pajji"] # Lists
teachers_names = ("patil","joshi") #Tuples
print(student_names)
student_names.append("banku")     # To add elements
student_names.remove("tonu")      # To remove elements
numbers = [5,7,91,5,3,9]          # Sorting in ascending order
numbers.sort()

print(student_names)
print(student_names[0:3])        # Slicing of elements
print(teachers_names)
print(len(teachers_names))       # Length function
print(len(student_names))
print(student_names[1] + "_" + student_names[2] )  # Concantenation
print(numbers)
for name in student_names:
    print(name)
