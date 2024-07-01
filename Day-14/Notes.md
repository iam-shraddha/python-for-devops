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
