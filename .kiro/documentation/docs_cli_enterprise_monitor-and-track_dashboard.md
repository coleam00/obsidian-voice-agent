# Viewing Kiro usage on the dashboard
Available only for Kiro admins, the Kiro dashboard summarizes useful data about how your subscribers use the Kiro IDE and Kiro CLI.
Kiro generates and displays new metrics on an hourly basis for the most part. The only section that is not updated hourly is the **Active users** widget, which is updated daily according to the coordinated universal time (UTC) clock.
## View the dashboard[](https://kiro.dev/docs/cli/enterprise/monitor-and-track/dashboard/#view-the-dashboard)
  1. Sign in to the AWS Management Console.
  2. Switch to the Kiro console.
  3. From the navigation pane, choose **Dashboard**.
  4. (Optional) Filter the information by date range or programming language.


**Info**
  * If the **Dashboard** link is not available in the navigation pane, see [Troubleshoot the dashboard](https://kiro.dev/docs/cli/enterprise/monitor-and-track/dashboard/#troubleshoot-the-dashboard).
  * If you'd like to send user metrics to a daily report with a per-user breakdown of their Kiro usage, see [View per-user activity in Kiro](https://kiro.dev/docs/cli/enterprise/monitor-and-track/user-activity).
  * For information about specific metrics, see [Dashboard metrics](https://kiro.dev/docs/cli/enterprise/monitor-and-track/dashboard/#dashboard-metrics) or choose the help link at the top-right of the dashboard page.


## Disable the dashboard[](https://kiro.dev/docs/cli/enterprise/monitor-and-track/dashboard/#disable-the-dashboard)
You might want to disable the Kiro dashboard if you have concerns about data privacy, page load times, or other potential issues. When you disable the dashboard, the dashboard page (and any links to it) will no longer be available in the Kiro console.
For more information about the dashboard, see [viewing usage metrics (dashboard)](https://kiro.dev/docs/enterprise/monitor-and-track/dashboard/#dashboard-metrics).
#### To disable the dashboard[](https://kiro.dev/docs/cli/enterprise/monitor-and-track/dashboard/#to-disable-the-dashboard)
  1. Sign in to the AWS Management Console.
  2. Switch to the Kiro console.
  3. Choose **Settings** , and in the **Kiro Settings** section, disable **Kiro usage dashboard**.


## Troubleshoot the dashboard[](https://kiro.dev/docs/cli/enterprise/monitor-and-track/dashboard/#troubleshoot-the-dashboard)
If the Kiro dashboard page is not available, do the following:
  * **Verify your permissions**. To view the dashboard, you need the following permissions:
    * `q:ListDashboardMetrics`
    * `codewhisperer:ListProfiles`
    * `sso:ListInstances`
    * `user-subscriptions:ListUserSubscriptions`
For more information about permissions, see [Policy: Allow administrators to configure Kiro and subscribe users](https://kiro.dev/docs/cli/enterprise/iam/#policy-allow-administrators-to-configure-kiro-and-subscribe-users).
  * **Verify your settings**. In the Kiro console, choose **Settings** and make sure that the **Kiro usage dashboard** toggle is enabled.


## Dashboard metrics[](https://kiro.dev/docs/cli/enterprise/monitor-and-track/dashboard/#dashboard-metrics)
The following table describes the metrics shown in the Kiro dashboard.
Metric name | Description  
---|---  
**Total subscriptions per tier** | Shows the total subscriptions broken down by subscription tier (Pro, Pro+, Power). Displays both per-group breakdown and total counts across all groups in the current AWS account, as well as subscriptions in member accounts if you're signed in to a management account for which organization-wide visibility of subscriptions has been enabled.  
**Active subscriptions per tier** | Shows the total active subscriptions broken down by subscription tier (Pro, Pro+, Power).  
  
_Active subscriptions_ are those belonging to users who have started using Kiro in their integrated development environment (IDE) or CLI. You are being charged for these subscriptions. For more information about active subscriptions, see [Subscription statuses](https://kiro.dev/docs/cli/enterprise/subscription-management#subscription-statuses).  
**Pending subscriptions per tier** | Shows the total pending subscriptions broken down by subscription tier (Pro, Pro+, Power).  
  
_Pending subscriptions_ are those belonging to users who have not yet started using Kiro. You are not being charged for these subscriptions. For more information about pending subscriptions, see [Subscription statuses](https://kiro.dev/docs/cli/enterprise/subscription-management#subscription-statuses).  
**Active users** | Shows the number of unique users actively utilizing Kiro on a daily, weekly, and monthly basis. Includes breakdowns by:  
- **Client type** (IDE vs. CLI)  
- **Subscription tier** (Pro, Pro+, Power)  
**Credits consumed** | Shows total Kiro credits consumed with time-based views (daily, weekly, monthly). Includes breakdowns by:  
- **Subscription tier** (Pro, Pro+, Power)  
- **Client type** (IDE vs. CLI)  
Page updated: November 26, 2025
[Monitor and track](https://kiro.dev/docs/cli/enterprise/monitor-and-track/)
[View per-user activity](https://kiro.dev/docs/cli/enterprise/monitor-and-track/user-activity/)
On this page
  * [View the dashboard](https://kiro.dev/docs/cli/enterprise/monitor-and-track/dashboard/#view-the-dashboard)
  * [Disable the dashboard](https://kiro.dev/docs/cli/enterprise/monitor-and-track/dashboard/#disable-the-dashboard)
  * [To disable the dashboard](https://kiro.dev/docs/cli/enterprise/monitor-and-track/dashboard/#to-disable-the-dashboard)
  * [Troubleshoot the dashboard](https://kiro.dev/docs/cli/enterprise/monitor-and-track/dashboard/#troubleshoot-the-dashboard)
  * [Dashboard metrics](https://kiro.dev/docs/cli/enterprise/monitor-and-track/dashboard/#dashboard-metrics)