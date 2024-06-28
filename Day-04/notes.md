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


***Modules***
1. Module means if you are writting a piece of code for project_1 and the same code can be used by project-2,project_3..etc just by modifying some variables.
2. Then instead of writting it again and again you'll write module called python.py file which has lot of functions then you can use this file as a module.
3. If someone needs all of the functions inside this module they can use all of them and if they need only some functions then they can use part of the module.
4. So the advantage module is same as functions i.e. reusability.Because module is equals to a group of functions.


***Packages***
1. Packages are collection of modules which means in your organization if your code is written in multiple python files then you can bundle it into a package.
2. We use both modules and packageslot of times beacause the task that we want to do there are people who already written entire code for that.
3. You can find and use these packages for python on PYPI(Python Package Index). And for installing those packages from pypl you can use the command called pip.

                                 pip install boto3
                                 pip install github
***Virtualenv***
1. Sometimes as a devops engineer we all use acommon machine for multiple projects and project_1(v1.2.3), project_2(v1.2.5) so if you install version for project_1 then it will not work for Project_2.
2. To solve this problem there is a concept in python called virtualenv and this is only useful if you are using same machine for different projects.
3. Virtualenv will do a logical seperation on your virtual machine for python packages that means if you create virtualenv for project_1 then will create virtual space where all the packages that you install will be available.
4. When you login inside the virtual machine using a perticular command you can switch to this virtualenv. So for each project you can create virtualenv ssh to the machine switch to the virtualenv and install the required packages.
                                pip install virtualenv
                                python -m venv project-abc
                                python -m venv project-xyz
                                source project-abc/bin/activate

