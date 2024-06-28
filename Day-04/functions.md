***Functions***
1. If you are writting code in linear approach it'll be fine for simple codes but if code goes to some 10000 lines then it is very difficult to troubleshoot or debug this file and understand where exactly the error is coming from.
2. Whereas if you are writting the code in a perticular way i.e. using concepts of functions and if there is a flaw in a addition() logic you know that this is the function that you have to look at.
3. And this code is much more redable than linear code, so the using functions you'll get advantages like redeability, reusability/modularity and debugging of the code.
4. Redeability:-Let say you wrote a python program of 1000 lines and you modified something in the line after that you sent it for the code review with your teammate if here function is not used it becomes very difficult for them to read the file.
5. Reusability:-If other person from your team needs to write addition() so instead of writting it they can just use your function by simply copying that part or they can invoke your function in their code as well.
6. Debugging:-If you got error in addition functionality but in linear program you need to start to read from line1 itself but in if function is used you already know which part of the code has an error so you can resolve it.
7. To start writting a function you should use keyword def so that python interpreter will understand this is the definition or function in the python.
                             def function_name():
                                function logic
