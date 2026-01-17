# Data protection
The AWS [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) applies to data protection in Kiro. As described in this model, AWS is responsible for protecting the global infrastructure that runs all of the AWS Cloud. You are responsible for maintaining control over your content that is hosted on this infrastructure. You are also responsible for the security configuration and management tasks for the AWS services that you use. For more information about data privacy, see the [Data Privacy FAQ](https://aws.amazon.com/compliance/data-privacy-faq/).
## Data storage[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#data-storage)
Kiro stores your questions, its responses, and additional context, such as code, to generate new responses to your requests. For information about how data is encrypted, see [Data encryption](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#data-encryption). For information about how AWS may use some questions that you ask Kiro and its responses to improve our services, see [Kiro service improvement](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#service-improvement).
### AWS regions where content is stored and processed[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#aws-regions-where-content-is-stored-and-processed)
If you are a Kiro Free Tier user or a Kiro individual subscriber, your content, such as prompts and responses, will be stored in the US East (N. Virginia) Region.
If you are a [Kiro enterprise user](https://kiro.dev/docs/cli/enterprise/concepts/#kiro-enterprise-user), your content will be stored in the AWS Region where your Kiro profile was created.
With cross-region inferencing, your content may be processed in a different Region within the geography where your content is stored. For more information, see [Cross-region processing](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#cross-region-processing).
## Cross-region processing[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#cross-region-processing)
The following sections describe how cross-region inference and cross-region calls are used to provide the Kiro service.
### Cross-region inference[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#cross-region-inference)
Kiro is powered by Amazon Bedrock, and uses cross-region inference to distribute traffic across different AWS Regions to enhance large language model (LLM) inference performance and reliability. With cross-region inference, you get increased throughput and resilience during high demand periods, as well as improved performance.
Cross region inference doesn’t affect where your data is stored. For information on where data is stored when you use Kiro, see [AWS Regions where content is stored and processed](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#aws-regions-where-content-is-stored-and-processed).
### Supported regions for Kiro cross-region inference[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#supported-regions-for-kiro-cross-region-inference)
For models or capabilities under the experimental tag, see “[Global cross-region inference for experimental features](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#global-cross-region-inference-for-experimental-features)”.
Supported Kiro geography | Inference regions  
---|---  
United States | 
  * US East (N. Virginia) (`us-east-1`)
  * US West (Oregon) (`us-west-2`)
  * US East (Ohio) (`us-east-2`)

  
Europe | 
  * Europe (Frankfurt) (`eu-central-1`)
  * Europe (Ireland) (`eu-west-1`)
  * Europe (Paris) (`eu-west-3`)
  * Europe (Stockholm) (`eu-north-1`)
  * Europe (Milan) (`eu-south-1`)
  * Europe (Spain) (`eu-south-2`)

  
### Global cross-region inference for experimental features[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#global-cross-region-inference-for-experimental-features)
Kiro may introduce new models and capabilities under an experimental tag, which process data differently than in the table above. When a model is launched as experimental, Kiro may use global cross-region inference to improve performance, increase throughput, and take advantage of available capacity across supported commercial AWS Regions worldwide. Global cross-region inference applies only to models and features explicitly designated as experimental.
For models and capabilities marked as experimental:
  * Inference requests may be processed in multiple AWS Regions globally, including Regions outside the one associated with your Kiro profile.
  * The Region where your data is stored is not affected by global cross-region inference.
  * This global routing is used to optimize resource availability and allow consistent performance for experimental model launches.


## Data encryption[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#data-encryption)
This topic provides information specific to Kiro about encryption in transit and encryption at rest.
### Encryption in transit[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#encryption-in-transit)
All communication between customers and Kiro and between Kiro and its downstream dependencies is protected using TLS 1.2 or higher connections.
### Encryption at rest[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#encryption-at-rest)
Kiro encrypts your data using AWS owned encryption keys from AWS Key Management Service (AWS KMS). You don’t have to take any action to protect the AWS managed keys that encrypt your data. For more information, see [AWS owned keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#aws-owned-cmk) in the _AWS Key Management Service Developer Guide_.
When you subscribe with Kiro enterprise, administrators have the option to create customer managed keys to encrypt your data. Customer managed keys are KMS keys in your AWS account that you create, own, and manage to directly control access to your data by controlling access to the KMS key. Only symmetric keys are supported. For information on creating your own KMS key, see [Creating keys](https://docs.aws.amazon.com/kms/latest/developerguide/create-keys.html) in the _AWS Key Management Service Developer Guide_.
To set up a customer managed key to encrypt data as a Kiro enterprise administrator, you need permissions to use AWS KMS. The required KMS permissions are included in the [example IAM policy](https://kiro.dev/docs/cli/privacy-and-security/data-protection/). After creating a customer managed KMS key, you must provide the key in the Kiro console to use it to encrypt data.
## Service improvement[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#service-improvement)
To help Kiro provide the most relevant information, we may use certain content from Kiro, such as questions that you ask Kiro, other inputs you provide, and the responses and code that Kiro generates, for service improvement. This page explains what content we use and how to opt out.
### Kiro content used for service improvement[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#kiro-content-used-for-service-improvement)
We may use certain content from Kiro Free Tier and Kiro individual subscribers for service improvement. Users that have a paid Kiro subscription and access it through a social login provider (like GitHub or Google) or through AWS Builder ID are considered _individual subscribers_. Content that Kiro may use for service improvement includes, for example, your questions to Kiro, other inputs you provide, and the responses and code that Kiro generates. Kiro may use this content, for example, to provide better responses to common questions, fix Kiro operational issues, for de-bugging, or for model training.
We do not use content from [Kiro enterprise users](https://kiro.dev/docs/cli/enterprise/concepts/#kiro-enterprise-user) for service improvement.
**Info**
If you have an Amazon Q Developer Pro subscription and access Kiro through your AWS account with the Amazon Q Developer Pro subscription, then Kiro will not use your content for service improvement.
## Opt out of data sharing[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#opt-out-of-data-sharing)
By default, Kiro collects usage data, errors, crash reports, and other metrics as well as content for service improvement from Kiro Free Tier users and Kiro individual subscribers. This section explains how to opt out of sharing your data in Kiro for Kiro Free Tier and Kiro individual subscribers. For information on how Kiro uses this data, see [Kiro service improvement](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#service-improvement).
[Kiro enterprise users](https://kiro.dev/docs/cli/enterprise/concepts/#kiro-enterprise-user) are automatically opted out of telemetry and content collection by AWS. Telemetry collection settings for [user activity reports](https://kiro.dev/docs/cli/enterprise/monitor-and-track/user-activity/) are controlled by the administrator in the Kiro console and cannot be configured by Kiro enterprise users. For more information, see [Kiro enterprise settings](https://kiro.dev/docs/cli/enterprise/settings).
### Opting out of sharing data in the IDE[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#opting-out-of-sharing-data-in-the-ide)
To opt out of sharing your client-side telemetry and content in the Kiro IDE, use this procedure:
  1. Open **Settings** in Kiro.
  2. Switch to the **User** sub-tab.
  3. Choose **Application** , and then choose **Telemetry and Content**.
  4. To opt out of telemetry collection, uncheck the box for **Data Sharing and Prompt Logging: Usage Analytics And Performance Metrics**. To opt out of content collection, uncheck the box for **Data Sharing and Prompt Logging: Content Collection for Service Improvement**.


### Opting out of sharing data in the CLI[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#opting-out-of-sharing-data-in-the-cli)
To opt out of sharing your client-side telemetry and content in the Kiro CLI, use this procedure:
  1. Open **Preferences** in the Kiro CLI application.
  2. To opt out of telemetry collection, toggle off the **Telemetry** setting. To opt out of content collection, toggle off the **Share Kiro content with AWS** setting.


## Types of telemetry collected[](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#types-of-telemetry-collected)
  * **Usage data** — Information such as the Kiro version, operating system (Windows, Linux, or macOS), and the anonymous machine ID.
  * **Performance metrics** — The request count, errors, and latency for various features: 
    * Login
    * Tab completion
    * Code generation
    * Steering
    * Hooks
    * Spec generation
    * Tools
    * MCP


Page updated: November 24, 2025
[Privacy and security](https://kiro.dev/docs/cli/privacy-and-security/)
[Compliance validation](https://kiro.dev/docs/cli/privacy-and-security/compliance-validation/)
On this page
  * [Data storage](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#data-storage)
  * [AWS regions where content is stored and processed](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#aws-regions-where-content-is-stored-and-processed)
  * [Cross-region processing](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#cross-region-processing)
  * [Cross-region inference](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#cross-region-inference)
  * [Supported regions for Kiro cross-region inference](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#supported-regions-for-kiro-cross-region-inference)
  * [Global cross-region inference for experimental features](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#global-cross-region-inference-for-experimental-features)
  * [Data encryption](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#data-encryption)
  * [Encryption in transit](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#encryption-in-transit)
  * [Encryption at rest](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#encryption-at-rest)
  * [Service improvement](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#service-improvement)
  * [Kiro content used for service improvement](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#kiro-content-used-for-service-improvement)
  * [Opt out of data sharing](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#opt-out-of-data-sharing)
  * [Opting out of sharing data in the IDE](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#opting-out-of-sharing-data-in-the-ide)
  * [Opting out of sharing data in the CLI](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#opting-out-of-sharing-data-in-the-cli)
  * [Types of telemetry collected](https://kiro.dev/docs/cli/privacy-and-security/data-protection/#types-of-telemetry-collected)