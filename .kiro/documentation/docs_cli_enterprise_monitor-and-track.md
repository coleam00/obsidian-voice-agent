# Monitoring and tracking
Monitoring is an important part of maintaining the reliability, availability, and performance of Kiro and your other AWS solutions. Kiro includes the following features to help you track and record user activity:
  * _A dashboard_ shows you aggregate user activity metrics of Kiro subscribers. For more information, see [Viewing Kiro usage on the dashboard](https://kiro.dev/docs/cli/enterprise/monitor-and-track/dashboard).
  * _User activity reports_ show you what individual users are up to in Kiro. For more information, see [Viewing per-user activity](https://kiro.dev/docs/cli/enterprise/monitor-and-track/user-activity).
  * _Prompt logs_ provide you with a record of all the prompts that users enter into the Kiro chat in their integrated development environment (IDE). For more information, see [Logging users' prompts](https://kiro.dev/docs/cli/enterprise/monitor-and-track/prompt-logging).


AWS also provides the following tools and features to monitor and record Kiro activity:
  * _AWS CloudTrail_ captures API calls and related events made by or on behalf of your AWS account and delivers the log files to an Amazon Simple Storage Service (Amazon S3) bucket that you specify. You can identify which users and accounts called AWS, the source IP address from which the calls were made, and when the calls occurred.
  * _Amazon CloudWatch_ monitors your AWS resources and the applications you run on AWS in real time. You can collect and track metrics, create customized dashboards, and set alarms that notify you or take actions when a specified metric reaches a threshold that you specify. For example, you can have CloudWatch track the number of times that Kiro has been invoked on your account, or the number of daily active users.


Page updated: November 14, 2025
[Supported regions](https://kiro.dev/docs/cli/enterprise/supported-regions/)
[View usage (dashboard)](https://kiro.dev/docs/cli/enterprise/monitor-and-track/dashboard/)