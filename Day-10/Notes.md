## List the files from the folders provided by users

Input:  User will provide list of foldder names like /abc /xyz

Output: Print all the files in provided folders

***Algorithm:***
1. Read input from the users
2. for loop on folders - list files
3. Identify module in python to execute
4. Print the files
5. Handle any known error

Take list of folders names as a input from user using input() and store it in variable folders. Instead of asking to provide list ask them to provide folder names with some spaces and convert this string into lists using .split() function.
Now write for_loop to execute for each folder one by one to print the files but here we need to use os module and we need to use os.listdir() function from os module.
And we wamt to print files in order not in a list so again write for_loop to print files in order.
