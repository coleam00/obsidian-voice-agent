# Concepts
## AWS IAM Identity Center[](https://kiro.dev/docs/cli/enterprise/concepts/#aws-iam-identity-center)
An AWS service that provides a central place to manage user identities of Kiro subscribers.
## AWS region[](https://kiro.dev/docs/cli/enterprise/concepts/#aws-region)
A physical location around the world where AWS clusters its data centers. There are two AWS Regions relevant to Kiro administrators:
  * The Region where your IAM Identity Center instance is enabled. This is where user identities are managed, and where subscriptions are stored.
  * The Region where your Kiro profile is created. This is where data is stored, and might be different from your IAM Identity Center instance's Region.


For more information about Regions, see [Supported Regions](https://kiro.dev/docs/cli/enterprise/supported-regions).
## Group[](https://kiro.dev/docs/cli/enterprise/concepts/#group)
A collection of users within IAM Identity Center. When you subscribe a group to Kiro, the users within it are individually subscribed. (There is no concept of a group subscription.)
## Kiro console[](https://kiro.dev/docs/cli/enterprise/concepts/#kiro-console)
A console within the AWS console where you create and manage Kiro subscriptions and control settings. The Kiro console appears as **Kiro** in the drop-down list of AWS services.
## Kiro credits[](https://kiro.dev/docs/cli/enterprise/concepts/#kiro-credits)
A unit of consumption that measures usage of Kiro's AI-powered features. Credits are spent when you interact with AI capabilities and are replenished based on your subscription tier.
## Kiro enterprise user[](https://kiro.dev/docs/cli/enterprise/concepts/#kiro-enterprise-user)
A user that you have added and subscribed to a Kiro subscription tier through the AWS console, capable of accessing Kiro through IAM Identity Center.
## Kiro profile[](https://kiro.dev/docs/cli/enterprise/concepts/#kiro-profile)
The management abstraction that defines and enforces administrative settings and subscriptions to enterprise users in a given AWS account and Region. A Kiro profile corresponds to a combination of an AWS account (management or member) and the Region for that account. This implies that you can only have one profile for each AWS account in a given Region. You set up Kiro profiles through the Kiro console.
## Kiro subscription tier[](https://kiro.dev/docs/cli/enterprise/concepts/#kiro-subscription-tier)
A distinctive pricing plan with a predetermined number of Kiro credits.
Page updated: November 16, 2025
[IAM](https://kiro.dev/docs/cli/enterprise/iam/)
[Privacy and security](https://kiro.dev/docs/cli/privacy-and-security/)
On this page
  * [AWS IAM Identity Center](https://kiro.dev/docs/cli/enterprise/concepts/#aws-iam-identity-center)
  * [AWS region](https://kiro.dev/docs/cli/enterprise/concepts/#aws-region)
  * [Group](https://kiro.dev/docs/cli/enterprise/concepts/#group)
  * [Kiro console](https://kiro.dev/docs/cli/enterprise/concepts/#kiro-console)
  * [Kiro credits](https://kiro.dev/docs/cli/enterprise/concepts/#kiro-credits)
  * [Kiro enterprise user](https://kiro.dev/docs/cli/enterprise/concepts/#kiro-enterprise-user)
  * [Kiro profile](https://kiro.dev/docs/cli/enterprise/concepts/#kiro-profile)
  * [Kiro subscription tier](https://kiro.dev/docs/cli/enterprise/concepts/#kiro-subscription-tier)