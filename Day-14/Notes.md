## Automate JIRA Creation On Github Event Using Python:

***Problem Statement*** :
- There are lot of QE/DEV engineers so when they notice the bug in the application then tey will create issue/ticket on the github repoitory. And once in a week development team goes to the repository and understands if tere are genuine issues or not.
- So everytime when theychecks the issue and if it is not valid so they can simplly close the issue and if the issue is valid then will work on that perticular issue. To work on that they have to track the amount of work that is reuired,for that they need to create ticket on the JIRA dashboard.
- This is so much of work for the development team, hence they ask devops enginer to automate this perticular process. There are two parties iyhub and Jira wheneer someone comments on the github on jira issue tickets have to automaticaly created on the jira.
- Firstly we ask github whenever someone writes comment called /jira then we will tell github through the webhook to sent entire information of that perticular issue. This entire UI information will converts into JSON automatically only you need to provide url on webhook configuration where you want to get this json informantion, Now we will take required fields from this json information and will make API call to jira.
- There are two parts to it Part1(Github) and Part2(Jira) here first of all you'll create an ec2 instance and write your python application. So in Part1 you'll configure a webhook which tells github to keep watching for this perticular comment /jira whenever you find that comment just provide a json for that python application and in Part2 we are sending json or making call with jira and we are creating a jira ticket.

***Algorithm*** :
1. Jira setup(account)
2. Understand jira api calls
3. Write the python script
4. Execution

***1.Steps to get list of projects*** : 
- Go to Atlassian link then signin by using your Email: Create account-->Jira Software-->Email & jir_site name-->Scrum Project-->Project_name & key-->Done.
- Once you have your dashboard firstcreate your API_Token: Go to profile-->Manage your account-->Security tab-->Create & manage api tokens. Now you need to understand how to talk to the jira api like which module you have to use, on which url you should accessthis jira etc for this you can refer jira api documentation.
- To Get list of the projects search for: Projects-->Get all projects-->Copy code for python-->Paste it on vscode. Now in that code replace the atlassian url with your own then in auth provide your email also provide api token that you have created.
- Now just run the this python file you'll get the list of projects that you have on your jira dashboard. For each project it will give all the details whichare available in the UI.
- So you can copy that entire output go to online json formatter and beautify it and you'll find you have two elements. Now want to just print the project name of perticular element by using index of the elements [index]["key"]. If you want to print all the project names that you have use a simple for loop.

***2.Steps to create jira request*** : 
- Go to jira dcumentation search for issue then goto create issue and copy the code and paste this to your file. When you create issue manuaaly on jira some of fields are mandatory & some are not.
- So just remove the non-mandatory fields and only keep the mandatory fields like Project,Issue type,Summary,Reporter(jira know as we use Api token). Issue type we used is story to get it's id click on this (...) icon-->configure board-->issue type-->story-->id(in url).
- Now execute this scripts and if you check on your jira dasboard you will notice a new ticket has been created.

***Explaination of the code*** :
- Here we are trying to use request module which is used to make an api calls. When we try to do automation ike aws instead of requests we use boto3 module but jira is not as stable as aws that's why here we are using standard module i.e. request module.
- Now from imported package we are using only perticular module i.e. HTTPBasicAuth so you want to authenticate with jira also here we also used json module. And we took url, api token and we performed the request as shown in the documentation.
