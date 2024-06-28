***Command Line Arguments***

1. Command line arguments are used to pass the values to your program so that anyone don't have to modify the program but program can take  command line arguments.
2.'Sys' is the module which comes with an python installation and that will help you to read parameters i.e. command line arguments inside the program.

                                       sys.argv[1]
                                       sys.argv[2]
                                       sys.argv[3]

***Environment Variables***
1. When you write a python program lot of time you need to deal with an sensitive information like passwords,API keys or API tokens,certificates etc. So you can pass these things as environment variables.
2. The difference between env_vars and command line argument is that when you want to deal with deal with sensitive information go with env_vars and when you deal with regular information you can use ommand line arguments.

                                     export password="monu"...[terminal]
                                     os.getenv("password")... [in code]
