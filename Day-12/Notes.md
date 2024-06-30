## File Operations
- File operations are used when you want to read update or delete a file in such cases you use file concept in python. If you do these things uing shellscript then for windows servers shellscripts will not to work you need to write powershell scripts and you have to continuously maintain both of them.
- So to avoid such things as a devops engineer you can use file operation in python. There are 2 operations wich you mostly use i.e. read and write operation for his you have inbuilt fuction called open.
                                                                         
                                                with open("/path/file","r"):
                                                  -------
                                                  -------

                                                with open("/path/file","w"):
                                                  -------
                                                  -------
## Algorithm
1. OPen the file in read mode
2. Store all the things in variable or list
3. Open the file in write mode
4. Update the maximum connection line(if)


## Explaination of the program
Here we will write function with three arguments i.e. file_path, key , value and this function has to open the file and read everything in the file then assign it to lines variable and use functio file.readlines() which will copy all the things into lines variable.
After that open file in write mode and to read every line using for loop then put if condition if we have perticular key in the lines then update that file with new key else if condtion not met keep the line as it is.
Now call the function and provide file_pat, key and value then execute the file and veriy whether given file uodated or not.
