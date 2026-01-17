# Enterprise billing
When you subscribe your team to Kiro, you can choose from the following service tiers: **Kiro Pro** , **Kiro Pro+** , and **Kiro Power**. Depending on usage patterns, higher level tiers will give users more credits to use with Kiro.
Credits are consumed fractionally based on each request. Simple edits and shorter prompts will use fewer credits than complex, lengthy tasks. This means that fractional credits will give you more value from your credit allocation.
## Tier comparison[](https://kiro.dev/docs/cli/enterprise/billing/#tier-comparison)
Tier | Credits | Overage  
---|---|---  
Pro | 1,000 | Opt-in  
Pro+ | 2,000 | Opt-in  
Power | 10,000 | Opt-in  
You are billed monthly for each user that you subscribe to Kiro. For more information, see [Kiro pricing](https://kiro.dev/pricing/).
## I've subscribed a user twice. Will I be double-billed?[](https://kiro.dev/docs/cli/enterprise/billing/#ive-subscribed-a-user-twice-will-i-be-double-billed)
It depends.
If a user is subscribed twice _under the same Kiro profile_ (for example, in two different groups), then you will _not_ be charged twice. Instead, you will pay the subscription price of the highest tier assigned to the user. Example: If Alice is subscribed at the Pro tier in group A, and the Pro+ tier in group B, then you will pay the Pro+ tier price for Alice.
If a user is subscribed twice under _different Kiro profiles_ (for example, in two different AWS Regions), then you will be charged twice. Example: If Bob is subscribed in Profile A in Europe (Frankfurt) and Profile B in US East (N. Virginia), then you will be charged twice for Bob.
## Proration considerations[](https://kiro.dev/docs/cli/enterprise/billing/#proration-considerations)
  * If you **unsubscribe** a user mid-month, you will pay for the last month in full. The cancellation takes effect at the beginning of the following month.
  * If you **upgrade** a subscription mid-month, you will be refunded for the lower-tier subscription, and you will be charged in full for the higher-tier subscription.
  * If you **downgrade** a subscription mid-month, you will pay in full for the higher-tier subscription, and you will be charged for the lower-tier subscription starting the following month.


## Viewing your bill[](https://kiro.dev/docs/cli/enterprise/billing/#viewing-your-bill)
  * You can view your bill in the AWS console's Billing and Cost Management service. The Kiro expenses are listed on the **Charges by service** tab, under **Kiro**. For more information about the Billing and Cost Management service, see [What is AWS Billing and Cost Management?](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/billing-what-is.html) in the _AWS Billing User Guide_.
  * You can identify the cost of Kiro subscriptions for specific users with resource IDs through AWS Billing and Cost Management. To do so, in the Billing and Cost Management console, under [Data Exports](https://console.aws.amazon.com/costmanagement/home#/bcm-data-exports), create either a standard data export or a legacy CUR export with the **Include resource IDs** option selected. To learn more, refer to [Creating data exports](https://docs.aws.amazon.com/cur/latest/userguide/dataexports-create.html?icmpid=docs_costmanagement_hp-dataexports-export-type) in the _AWS Data Exports User Guide_.


Page updated: November 16, 2025
[Settings](https://kiro.dev/docs/cli/enterprise/settings/)
[IAM](https://kiro.dev/docs/cli/enterprise/iam/)
On this page
  * [Tier comparison](https://kiro.dev/docs/cli/enterprise/billing/#tier-comparison)
  * [I've subscribed a user twice. Will I be double-billed?](https://kiro.dev/docs/cli/enterprise/billing/#ive-subscribed-a-user-twice-will-i-be-double-billed)
  * [Proration considerations](https://kiro.dev/docs/cli/enterprise/billing/#proration-considerations)
  * [Viewing your bill](https://kiro.dev/docs/cli/enterprise/billing/#viewing-your-bill)