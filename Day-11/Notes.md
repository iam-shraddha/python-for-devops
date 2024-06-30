# Get pull request information on a repository using python

## Algorithm
1. Use the request module
2. Make API calls(url)
3. convert json to dictionary
4. Print the required things

## Explaination of the program
- To get api url go to github api documentation and search for pulls here you will find a url. Now execute command 'pip install requests' and import the requests module in the program.
- Paste the url and replce the owner and repo with your data(api.github.com/repos/kubernetes/kubernetes/pulls) if you put this url on brwser you'll get list of pull requests and complete information of user who created this pull request.(list of dictionary)
- To access it by using python program you have syntax request.get, if you use response.json() it will convert json to dictionary> Now if you want to print only names of the user who created the pull request.
- Then print it using ---- detail[0]["user"]["login"] and for printing all the users you can write the for loop ---- for i in range(len(detail))
