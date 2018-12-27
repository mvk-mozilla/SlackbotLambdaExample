# SlackbotLambdaExample
A simple Slackbot demonstrating how to use CI and Lambda to deploy to Slack

Links with directions I've followed
https://serverless.com/blog/serverless-python-packaging/
https://dev.to/codevbus/deploy-aws-lambda-functions-with-aws-sam-cli-and-travis-ci-part-2-2goh
https://blog.theodo.fr/2017/08/serverless-applications-aws-travis-make-deployment-great/

Slack-Lambda: https://api.slack.com/tutorials/aws-lambda

EOD 12/14/2018- I've added numpy to test deployment of complex Python setups
I have not yet tried to push this through Travis.
Locally I have updated requirements.txt, created a venv, enabled npm and serverless-python-requirements.
I need to figure out how to tie all that to Travis. Didn't want to go down that rabbit hole at 3 PM.
I also created an IAM Administrator role and group and configured my local aws cli environment to use it.

TO DO MONDAY 12/17:
- Fix Slack- broke the integration
- Fix API Gateway- it's calling slackPy3 but the function isn't updating
-Get complex Python to deploy to Lambda through CI
-Add Slack request processing to Slackbot
-Add Google API integration
-BMO Find Dupes bot?

Simple Lambda Slackbot example: https://chatbotslife.com/write-a-serverless-slack-chat-bot-using-aws-e2d2432c380e

Full details about the architecture that this is part of are described here: https://docs.google.com/document/d/16q97opSUGLLjow0nNxuafpChvXE99kqz68CXInCLpq8/edit?usp=sharing
