# SlackbotLambdaExample
A simple Slackbot demonstrating how to use CI and Lambda to deploy to Slack

Links with directions I've followed
https://serverless.com/blog/serverless-python-packaging/
https://dev.to/codevbus/deploy-aws-lambda-functions-with-aws-sam-cli-and-travis-ci-part-2-2goh
https://blog.theodo.fr/2017/08/serverless-applications-aws-travis-make-deployment-great/

EOD 12/14/2018- I've added numpy to test deployment of complex Python setups
I have not yet tried to push this through Travis.
Locally I have updated requirements.txt, created a venv, enabled npm and serverless-python-requirements.
I need to figure out how to tie all that to Travis. Didn't want to go down that rabbit hole at 3 PM.
I also created an IAM Administrator role and group and configured my local aws cli environment to use it.

TO DO MONDAY 12/17:
-Get complex Python to deploy to Lambda through CI
-Add Slack request processing to Slackbot
-Add Google API integration