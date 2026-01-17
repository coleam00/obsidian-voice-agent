# How Kiro works with identity and access management (IAM)
To access the Kiro console and perform tasks related to your Kiro subscription, you need permissions provisioned through AWS Identity and Access Management (IAM). AWS IAM is an AWS service that helps an administrator securely control access to AWS resources and is available at no additional charge.
To enable access, you can create an identity-based policy with the necessary permissions and attach it to the IAM identity that is configuring Kiro subscriptions. For more information, see [Identity-based policies for Kiro](https://kiro.dev/docs/cli/enterprise/iam/#identity-based-policies-for-kiro).
In addition, Kiro uses AWS IAM service-linked roles. A service-linked role is a unique type of IAM role that is linked directly to Kiro, rather than to an identity, and they are automatically created for you when you subscribe. For more information, see [Service-linked roles for Kiro](https://kiro.dev/docs/cli/enterprise/iam/#service-linked-roles-for-kiro).
## Identity-based policies for Kiro[](https://kiro.dev/docs/cli/enterprise/iam/#identity-based-policies-for-kiro)
Identity-based policies are JSON permissions policy documents that you can attach to an identity, such as an IAM user, group of users, or role. These policies control what actions users and roles can perform, on which resources, and under what conditions.
To subscribe users and configure your subscription, you need the permissions defined in Allow administrators to configure and subscribe to Kiro in the console.
To learn how to create an identity-based policy, see [Define custom IAM permissions with customer managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_create.html) in the _AWS IAM User Guide_.
### Policy: allow administrators to configure Kiro and subscribe users[](https://kiro.dev/docs/cli/enterprise/iam/#policy-allow-administrators-to-configure-kiro-and-subscribe-users)
The following example policy grants permissions to perform actions in the Kiro console. The Kiro console is where you subscribe users to Kiro, configure Kiro’s integration with AWS IAM Identity Center and AWS Organizations, and manage subscription settings. This policy also includes permissions to create and configure customer managed KMS keys.
Show policy
json
```

{
  "Version":"2012-10-17",                   
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "sso:ListInstances",
        "sso:CreateInstance",
        "sso:CreateApplication",
        "sso:PutApplicationAuthenticationMethod",
        "sso:PutApplicationGrant",
        "sso:PutApplicationAssignmentConfiguration",
        "sso:ListApplications",
        "sso:GetSharedSsoConfiguration",
        "sso:DescribeInstance",
        "sso:PutApplicationAccessScope",
        "sso:DescribeApplication",
        "sso:DeleteApplication",
        "sso:CreateApplicationAssignment",
        "sso:DeleteApplicationAssignment",
        "sso:UpdateApplication",
        "sso:DescribeRegisteredRegions",
        "sso:GetSSOStatus"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:ListRoles"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "identitystore:DescribeUser"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "sso-directory:GetUserPoolInfo",
        "sso-directory:DescribeUser",
        "sso-directory:DescribeUsers",
        "sso-directory:DescribeGroups",
        "sso-directory:SearchGroups",
        "sso-directory:SearchUsers",
        "sso-directory:DescribeDirectory"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "signin:ListTrustedIdentityPropagationApplicationsForConsole",
        "signin:CreateTrustedIdentityPropagationApplicationForConsole"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "user-subscriptions:ListClaims",
        "user-subscriptions:ListApplicationClaims",
        "user-subscriptions:ListUserSubscriptions",
        "user-subscriptions:CreateClaim",
        "user-subscriptions:DeleteClaim",
        "user-subscriptions:UpdateClaim",
        "user-subscriptions:SetOverageConfig"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "organizations:DescribeAccount",
        "organizations:DescribeOrganization",
        "organizations:ListAWSServiceAccessForOrganization",
        "organizations:DisableAWSServiceAccess",
        "organizations:EnableAWSServiceAccess"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "kms:ListAliases",
        "kms:CreateGrant",
        "kms:Encrypt",
        "kms:Decrypt",
        "kms:GenerateDataKey*",
        "kms:RetireGrant",
        "kms:DescribeKey"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "codeguru-security:UpdateAccountConfiguration"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "iam:CreateServiceLinkedRole"
      ],
      "Resource": [
        "arn:aws:iam::*:role/aws-service-role/q.amazonaws.com/AWSServiceRoleForAmazonQDeveloper"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "codewhisperer:UpdateProfile",
        "codewhisperer:ListProfiles",
        "codewhisperer:TagResource",
        "codewhisperer:UnTagResource",
        "codewhisperer:ListTagsForResource",
        "codewhisperer:CreateProfile"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "q:ListDashboardMetrics", 
        "q:CreateAssignment", 
        "q:DeleteAssignment",
        "q:UpdateAssignment"
      ],
      "Resource": [
        "*"
      ]
    },
    {
      "Effect": "Allow",
      "Action": [
        "cloudwatch:GetMetricData", 
        "cloudwatch:ListMetrics"
      ],
      "Resource": [
        "*"
      ]
    }
  ]
}


```

## Service-linked roles for Kiro[](https://kiro.dev/docs/cli/enterprise/iam/#service-linked-roles-for-kiro)
A service-linked role is a unique type of IAM role that is linked directly to Kiro. Service-linked roles are predefined by AWS and include all the permissions that Kiro requires to call other AWS services on your behalf.
A service-linked role makes setting up Kiro easier because you don’t have to manually add the necessary permissions. Kiro defines the permissions of its service-linked roles, and unless defined otherwise, only Kiro can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.
You can delete a service-linked role only after first deleting their related resources. This protects your Kiro resources because you can't inadvertently remove permission to access the resources. For more information about service-linked roles, see the [AWS IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html#id_roles_terms-and-concepts).
There are two service-linked roles that will be created for you when you subscribe with Kiro enterprise:
  * [AWSServiceRoleForUserSubscriptions](https://kiro.dev/docs/cli/enterprise/iam/#service-linked-role-awsserviceroleforusersubscriptions)
  * [AWSServiceRoleForAmazonQDeveloper](https://kiro.dev/docs/cli/enterprise/iam/#service-linked-role-awsserviceroleforamazonqdeveloper)


### Service-linked role: AWSServiceRoleForUserSubscriptions[](https://kiro.dev/docs/cli/enterprise/iam/#service-linked-role-awsserviceroleforusersubscriptions)
Kiro uses the service-linked role named **AWSServiceRoleForUserSubscriptions**. This role grants permissions for Kiro to access your IAM Identity Center resources in order to automatically update your subscriptions.
The AWSServiceRoleForUserSubscriptions service-linked role trusts the following services to assume the role:
  * `user-subscriptions.amazonaws.com`


The role permissions policy named AWSServiceRoleForUserSubscriptions allows Kiro to complete the following actions on the specified resources:
  * Action: `identitystore:DescribeGroup` on `*`
  * Action: `identitystore:DescribeUser` on `*`
  * Action: `identitystore:IsMemberInGroups` on `*`
  * Action: `identitystore:ListGroupMemberships` on `*`
  * Action: `organizations:DescribeOrganization` on `*`
  * Action: `sso:DescribeApplication` on `*`
  * Action: `sso:DescribeInstance` on `*`
  * Action: `sso:ListInstances` on `*`
  * Action: `sso-directory:DescribeUser` on `*`


You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#service-linked-role-permissions) in the _AWS IAM User Guide_.
### Service-linked role: AWSServiceRoleForAmazonQDeveloper[](https://kiro.dev/docs/cli/enterprise/iam/#service-linked-role-awsserviceroleforamazonqdeveloper)
Kiro uses the service-linked role named **AWSServiceRoleForAmazonQDeveloper**. This role grants permissions for Kiro to access data in your account to calculate billing, provides access to create and access security reports in Amazon CodeGuru, and emit data to CloudWatch.
The AWSServiceRoleForAmazonQDeveloper service-linked role trusts the following services to assume the role:
  * `q.amazonaws.com`


The role permissions policy named AWSServiceRoleForAmazonQDeveloper allows Kiro to complete the following actions on the specified resources:
  * Action: `cloudwatch:PutMetricData` on `AWS/Q CloudWatch namespace`


You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html#service-linked-role-permissions) in the _AWS IAM User Guide_.
### Managing service-linked roles[](https://kiro.dev/docs/cli/enterprise/iam/#managing-service-linked-roles)
You don't need to manually create a service-linked role. When you create a profile for Kiro in the AWS Management Console, Kiro creates the service-linked role for you. If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account.
You can also use the IAM console or AWS CLI to create a service-linked role with the `q.amazonaws.com` service name. For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the _AWS IAM User Guide_. If you delete this service-linked role, you can use the same process to create the role again.
Kiro does not allow you to edit the AWSServiceRoleForUserSubscriptions or AWSServiceRoleForAmazonQDeveloper service-linked roles. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the _AWS IAM User Guide_.
If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it. Use the IAM console, the AWS CLI, or the AWS API to delete the service-linked roles. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the _AWS IAM User Guide_.
**Info**
Note: If Kiro is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.
### Supported regions for Kiro service-linked roles[](https://kiro.dev/docs/cli/enterprise/iam/#supported-regions-for-kiro-service-linked-roles)
You can use the AWSServiceRoleForUserSubscriptions and AWSServiceRoleForAmazonQDeveloper roles in the following AWS Regions. For more information on Regions, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html) in the _AWS General Reference_.
Region name | Region identity  
---|---  
US East (N. Virginia) | us-east-1  
Europe (Frankfurt) | eu-central-1  
Page updated: December 11, 2025
[Billing](https://kiro.dev/docs/cli/enterprise/billing/)
[Concepts](https://kiro.dev/docs/cli/enterprise/concepts/)
On this page
  * [Identity-based policies for Kiro](https://kiro.dev/docs/cli/enterprise/iam/#identity-based-policies-for-kiro)
  * [Policy: allow administrators to configure Kiro and subscribe users](https://kiro.dev/docs/cli/enterprise/iam/#policy-allow-administrators-to-configure-kiro-and-subscribe-users)
  * [Service-linked roles for Kiro](https://kiro.dev/docs/cli/enterprise/iam/#service-linked-roles-for-kiro)
  * [Service-linked role: AWSServiceRoleForUserSubscriptions](https://kiro.dev/docs/cli/enterprise/iam/#service-linked-role-awsserviceroleforusersubscriptions)
  * [Service-linked role: AWSServiceRoleForAmazonQDeveloper](https://kiro.dev/docs/cli/enterprise/iam/#service-linked-role-awsserviceroleforamazonqdeveloper)
  * [Managing service-linked roles](https://kiro.dev/docs/cli/enterprise/iam/#managing-service-linked-roles)
  * [Supported regions for Kiro service-linked roles](https://kiro.dev/docs/cli/enterprise/iam/#supported-regions-for-kiro-service-linked-roles)