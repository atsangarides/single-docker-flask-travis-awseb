# docker-flask-travis-awseb
Flask application in single docker container, with redis, CI/CD on travis deploying on AWS Elastic Beanstalk.

# Architecture
* The `Dockerfile` is used for the `build` process in AWS EB.
* The `Dockerfile.dev` is responsible for triggering the `Pytest` tests on travis-ci. The only difference is the startup
command where we are simply calling `pytest` and the pytest module runs all te tests in the `tests` directory.

# Pytest
* A `tests` directory includes all the tests to be run when the master branch on Github receives a pull request.
* An instance of the flask app is created, with `Testing=True`, and this context is then teared down upon 
completion/failure of the tests.
* If all tests pass, this will trigger the newly pushed app to be deployed on AWS EB.

# travis-ci
* To adjust to you needs you would need to edit the `deploy` section.
* We are only deploying the `master` branch.
* For the IAM user, I created a new user, with programmatic access only, and from exiting policies I chose 
`AWSElasticBeanstalkFullAccess`.
* Then I went onto the project setting on travis-ci.org, and added `AWS_ACCESS_KEY` and `AWS_SECRET_KEY` as environment 
variables. This way, the IAM details are securely stored and not exposed during build/deployment.