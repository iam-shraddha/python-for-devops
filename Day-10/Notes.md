## List the files from the folders provided by users

Input:  User will provide list of foldder names like /abc /xyz

Output: Print all the files in provided folders

***Algorithm:***
1. Read input from the users
2. for loop on folders list files
3. Identify module in python to execute
4. Print the files
5. Handle any known error

***Steps to follow***
- Take list of folders names as a input from user using input() and sto-re it in variable folders. Instead of asking to provide list ask them to provide folder names with some spaces and convert this string into lists using .split() function.
- Now write for_loop to execute for each folder one by one to print the files but here we need to use os module and we need to use os.listdir() function from os module and we want to print files in order not in a list so again write for_loop to print files in order.
- If user gives 2 input as /xyz /opt here xyz is a folder which does not exists whereas opt is exists but after executing we got error that [file not found]. But this is not expected behavior as /opt is right input so we need to write logic for exceptional handing.
- Exception handling means instead of terminating the program for a known error we want to give proper error messege and then proceed the program for this we need to write that block of code inside keyword called try and another keyword except by using it we can write what kind of errors to except.
