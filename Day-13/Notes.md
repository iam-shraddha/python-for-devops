## Boto3 Module

1. Boto3 is a python module which helps in creating resources like ec2_instances, s3_buckets on the AWS.Only prerequisite to use boto3 is that you should have knowledge to create resources on AWS UI.
2. Boto3 is an bascally anutomation so to master the automation one should know the manual steps. All tools like cft,aws cli,terraform & boto3 are used to create resources on the aws.
3. Terraform & CFT falls under the templating languages because here you don't need to learn any programming whereas AWS CLI and Boto3 are scripting languages so fundamental difference between them is when you want do templating you use Terraform and CFT and when you want to use scriptingyou go with AWS CLI & Boto3.
4. For doing simple tasks like listing s3,ec2 or any quick actions then rather than templating scripting i.e. aws cli is easy option. Again in scripting you have two things aws cli and boto3 for quick actions aws cli is betther then what is the use of boto3.
5. So the fundamental advantage of boto3 is you can use same things with boto3 as aws cli but boto3 can be used in the serverless serverless pogramming as well that means lambda functions in aws as there's no optin to use aws cli for this.

## Steps to use boto3 module
- Go to vscode install aws toolkit and authenticate by using aws configure here provide access key & secret access key from the aws. Now install the boto3 module by using 'pip install boto3'.
- Go to boto3 documentation->Available services->s3 and copy that code. Then search for create s3 bucket and copy that code to your program now keep the parameter as per your requirement.Execute the program and s3 buket will be creted on aws.
- So here client = boto3.client('resource_name') this line is common syntax just add resource name that you want in the bracket so here you creating the client and using it you talk with aws api.
