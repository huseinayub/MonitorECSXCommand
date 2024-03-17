# MonitorECSXCommand

[![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

## Description

MonitorECSXCommand is an AWS SAM template that helps you monitor the IAM entities accessing your AWS Services & Cluster via ECS [execute-command](https://docs.aws.amazon.com/cli/latest/reference/ecs/execute-command.html) and notify your team via Slack.

## Deployment

- ```sam validate && sam deploy```

## Deployment Artifacts

- The SAM template will provision an **AWS Lambda function** and an **EventBridge Rule**. Make sure you have the necessary IAM permissions to deploy to these services.

## Contact

- [Linkedin](https://www.linkedin.com/in/hussein-ayoub-207a49135/)
- [Twitter/X](https://twitter.com/h__ayub)
