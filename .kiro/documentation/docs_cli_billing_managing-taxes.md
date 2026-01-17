# Managing your taxes
This section provides answers to tax collection, VAT, and billing address questions for Kiro.
## Why do I see information for Amazon web services, inc. For my Kiro purchase?[](https://kiro.dev/docs/cli/billing/managing-taxes/#why-do-i-see-information-for-amazon-web-services-inc-for-my-kiro-purchase)
Amazon Web Services, Inc. is the service provider for Kiro. Amazon Web Services, Inc. ("AWSI") is established and operates in the United States. AWSI is registered for Sales Tax in the states shown [here](https://aws.amazon.com/tax-help/united-states/). AWSI is also registered for VAT in countries where indirect tax laws require foreign providers of Electronically Supplied Services ("ESS") to register and collect local VAT. AWSI treats Kiro as Downloaded Software in the USA and as ESS outside of the USA. If required by your country's Indirect Tax laws, AWS will collect Indirect Taxes from you, issue a tax invoice, and remit it to the tax authority in AWS's name. In some countries, AWS is not required to collect Indirect Taxes from you and remit it to the tax authority in AWS's name if you have a valid tax registration number ("TRN") in that country. You need to add your TRN to your Stripe Account Customer Profile, and you may be required to self-assess VAT depending on local regulations.
Please see below jurisdictions where tax will be charged on Kiro purchases:
Country Name | Tax Collected From | Tax Rate  
---|---|---  
AUSTRALIA | B2C | 10%  
AUSTRIA | B2B/B2C | 20%  
BANGLADESH | B2B | 15%  
BELGIUM | B2B/B2C | 21%  
BULGARIA | B2C | 20%  
CANADA | B2B/B2C | Varies by Province  
CHILE | B2C | 19%  
CZECH REPUBLIC | B2B/B2C | 21%  
FRANCE | B2C | 20%  
GERMANY | B2C | 19%  
INDIA | B2C | 18%  
INDONESIA | B2B/B2C | 11%  
ISRAEL | N/A | 18%  
ITALY | B2C | 22%  
JAPAN | B2B/B2C | 10%  
KOREA (REPUBLIC OF KOREA) | B2C | 10%  
MALAYSIA | B2B/B2C | 8%  
NEPAL | B2B | 13%  
NETHERLANDS | B2C | 21%  
NEW ZEALAND | B2C | 15%  
NORWAY | B2B/B2C | 25%  
POLAND | B2C | 23%  
PORTUGAL | B2B/B2C | 23%  
ROMANIA | B2C | 19%  
SINGAPORE | B2C | 9%  
SOUTH AFRICA | B2B/B2C | 15%  
SPAIN | B2C | 21%  
SWEDEN | B2B/B2C | 25%  
SWITZERLAND | B2B/B2C | 8.1%  
TAIWAN | B2C | 5%  
THAILAND | B2C | 7%  
UK | B2C | 20%  
UNITED ARAB EMIRATES | B2B/B2C | 5%  
UNITED STATES (US) | B2B/B2C | Varies by state  
## How does AWS determine my location to determine the applicable taxes for my account(s)?[](https://kiro.dev/docs/cli/billing/managing-taxes/#how-does-aws-determine-my-location-to-determine-the-applicable-taxes-for-my-accounts)
AWS will use your customer billing address you provide when purchasing Kiro. If the billing address entered is invalid, you will get a customer_tax_location_invalid error.
## I am a B2B (business) customer, my company's tax registration number (TRN) is on our stripe/AWS accounts, so why are we being charged VAT rather than using reverse charge and self-assessing VAT?[](https://kiro.dev/docs/cli/billing/managing-taxes/#i-am-a-b2b-business-customer-my-companys-tax-registration-number-trn-is-on-our-stripeaws-accounts-so-why-are-we-being-charged-vat-rather-than-using-reverse-charge-and-self-assessing-vat)
Kiro is billed using a different platform (not the AWS Console). If you are a B2B customer who has provided its TRN in your AWS Account, you will need to also include for your Kiro account through your customer portal. In addition, certain jurisdictions require AWS to charge and collect tax on both B2B and B2C purchases, in these jurisdictions AWS is responsible, and you will not be able to Self-Assess.
## If I update my tax, account, or billing address mid-month, how is VAT calculated?[](https://kiro.dev/docs/cli/billing/managing-taxes/#if-i-update-my-tax-account-or-billing-address-mid-month-how-is-vat-calculated)
AWS will use your billing address at the time of your purchase, or changes to your subscription such as upgrades or renewals.
## I receive special status/relief from paying VAT. How do I check that I am not charged VAT?[](https://kiro.dev/docs/cli/billing/managing-taxes/#i-receive-special-statusrelief-from-paying-vat-how-do-i-check-that-i-am-not-charged-vat)
Special status/relief status from paying VAT is coming soon.
## What payment currencies and payment methods are supported by AWS inc. For Kiro purchases?[](https://kiro.dev/docs/cli/billing/managing-taxes/#what-payment-currencies-and-payment-methods-are-supported-by-aws-inc-for-kiro-purchases)
We accept all major credit cards. Kiro usage is invoiced in USD.
## My VAT invoice, and/or AWS seller appears incorrectly.[](https://kiro.dev/docs/cli/billing/managing-taxes/#my-vat-invoice-andor-aws-seller-appears-incorrectly)
Please contact [Kiro billing support](https://support.aws.amazon.com/#/contacts/kiro).
## What tax registration numbers (trns) and formats are accepted?[](https://kiro.dev/docs/cli/billing/managing-taxes/#what-tax-registration-numbers-trns-and-formats-are-accepted)
Kiro will accept TRNs based on the requirements set forth by the country in which the customer is located. When a customer adds a TRN, Kiro will check that the formatting is correct.
Page updated: November 16, 2025
[Managing your Kiro CLI subscription](https://kiro.dev/docs/cli/billing/subscription-portal/)
[Related questions](https://kiro.dev/docs/cli/billing/related-questions/)
On this page
  * [Why do I see information for Amazon web services, inc. For my Kiro purchase?](https://kiro.dev/docs/cli/billing/managing-taxes/#why-do-i-see-information-for-amazon-web-services-inc-for-my-kiro-purchase)
  * [How does AWS determine my location to determine the applicable taxes for my account(s)?](https://kiro.dev/docs/cli/billing/managing-taxes/#how-does-aws-determine-my-location-to-determine-the-applicable-taxes-for-my-accounts)
  * [I am a B2B (business) customer, my company's tax registration number (TRN) is on our stripe/AWS accounts, so why are we being charged VAT rather than using reverse charge and self-assessing VAT?](https://kiro.dev/docs/cli/billing/managing-taxes/#i-am-a-b2b-business-customer-my-companys-tax-registration-number-trn-is-on-our-stripeaws-accounts-so-why-are-we-being-charged-vat-rather-than-using-reverse-charge-and-self-assessing-vat)
  * [If I update my tax, account, or billing address mid-month, how is VAT calculated?](https://kiro.dev/docs/cli/billing/managing-taxes/#if-i-update-my-tax-account-or-billing-address-mid-month-how-is-vat-calculated)
  * [I receive special status/relief from paying VAT. How do I check that I am not charged VAT?](https://kiro.dev/docs/cli/billing/managing-taxes/#i-receive-special-statusrelief-from-paying-vat-how-do-i-check-that-i-am-not-charged-vat)
  * [What payment currencies and payment methods are supported by AWS inc. For Kiro purchases?](https://kiro.dev/docs/cli/billing/managing-taxes/#what-payment-currencies-and-payment-methods-are-supported-by-aws-inc-for-kiro-purchases)
  * [My VAT invoice, and/or AWS seller appears incorrectly.](https://kiro.dev/docs/cli/billing/managing-taxes/#my-vat-invoice-andor-aws-seller-appears-incorrectly)
  * [What tax registration numbers (trns) and formats are accepted?](https://kiro.dev/docs/cli/billing/managing-taxes/#what-tax-registration-numbers-trns-and-formats-are-accepted)