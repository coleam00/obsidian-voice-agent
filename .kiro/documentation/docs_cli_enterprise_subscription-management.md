# Managing Kiro subscriptions
## Change Kiro subscription plans[](https://kiro.dev/docs/cli/enterprise/subscription-management/#change-kiro-subscription-plans)
  1. Sign in to the AWS Management Console.
  2. Switch to the Kiro console. If you don't see it, you might be in the wrong AWS Region.
  3. In the **Users & Groups** page, choose the **Users** or **Groups** tab.
  4. Choose the user or group whose subscriptions you want to upgrade or downgrade.
  5. Choose **Change plan** then choose the new plan. Select **Continue** to finish.
  6. If it is a higher tier plan, changes will happen immediately. If it is a lower tier plan, changes happen at the beginning of the following month.


**Info**
To learn about what's offered at each subscription tier, see [Enterprise billing](https://kiro.dev/docs/cli/enterprise/billing).
## Unsubscribe Kiro users[](https://kiro.dev/docs/cli/enterprise/subscription-management/#unsubscribe-kiro-users)
  1. Sign in to the AWS Management Console.
  2. Switch to the Kiro console. If you don't see it, you might be in the wrong AWS Region.
  3. In the **Users & Groups** page, choose the **Users** or **Groups** tab.
  4. Choose the user or group whose subscriptions you want to cancel.
  5. Choose **Deactivate plan**. Review the contents of the **Unsubscribee** dialog box then choose **Unsubscribe**.


**Info**
After unsubscribing users, their subscriptions are marked as **Canceled**. They will have until the end of the month to use credits from the current plan. Starting the following month, they can no longer access paid Kiro features.
## Enable overages for Kiro users[](https://kiro.dev/docs/cli/enterprise/subscription-management/#enable-overages-for-kiro-users)
You might want to enable overages to give users the ability to continue working when they exceed their plan limits. Enabling overages has the following advantages:
  * **Uninterrupted productivity** – When a user exceeds their plan's quota, they can continue working without disruption. The productivity benefits of continued access might outweigh the additional costs.
  * **Better usage pattern insights** – Users get more accurate data about their actual usage, which helps in right-sizing future subscription needs.


By default, overages are _disabled_. Once enabled, overages become available to all users and groups in the profile. To enable overages:
  1. Sign in to the AWS Management Console.
  2. Switch to the Kiro console. If you don't see it, you might be in the wrong AWS Region.
  3. Choose **Settings**.
  4. Find the **Kiro settings** section.
  5. Turn on **Overages**.


**Info**
Setting custom caps for overages is not yet supported (coming soon).
## Subscription statuses[](https://kiro.dev/docs/cli/enterprise/subscription-management/#subscription-statuses)
You can view the status of your users' subscriptions on the **Subscriptions** page of the Kiro console. The statuses on the **User** tab are:
  * **Active** – The user is subscribed to Kiro. You will be charged for active user subscriptions in the group.
  * **Canceled** – The user subscription was canceled by an administrator. Unsubscribed users in the group can no longer access paid Kiro features. For more information, see [Unsubscribe Kiro users](https://kiro.dev/docs/cli/enterprise/subscription-management/#unsubscribe-kiro-users).
  * **Pending** – The user is subscribed but has not activated their subscription. You are not being charged for this subscription and there will be no data under _Last active_ column.


**Info**
There are no statuses on the **Groups** tab since subscriptions are assigned to users, not groups.
Page updated: November 16, 2025
[Subscribe your team](https://kiro.dev/docs/cli/enterprise/subscribe/)
[Supported regions](https://kiro.dev/docs/cli/enterprise/supported-regions/)
On this page
  * [Change Kiro subscription plans](https://kiro.dev/docs/cli/enterprise/subscription-management/#change-kiro-subscription-plans)
  * [Unsubscribe Kiro users](https://kiro.dev/docs/cli/enterprise/subscription-management/#unsubscribe-kiro-users)
  * [Enable overages for Kiro users](https://kiro.dev/docs/cli/enterprise/subscription-management/#enable-overages-for-kiro-users)
  * [Subscription statuses](https://kiro.dev/docs/cli/enterprise/subscription-management/#subscription-statuses)