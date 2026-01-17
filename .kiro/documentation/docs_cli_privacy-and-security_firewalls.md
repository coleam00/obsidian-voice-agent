# Configuring a firewall, proxy server, or data perimeter for Kiro
If you're using a firewall, proxy server, or [data perimeter](https://aws.amazon.com/identity/data-perimeters-on-aws/), make sure to allowlist traffic to the following URLs and Amazon Resource Names (ARNs) so that Kiro works as expected.
## General urls to allowlist[](https://kiro.dev/docs/cli/privacy-and-security/firewalls/#general-urls-to-allowlist)
In the following URLs, replace:
  * `idc-directory-id-or-alias` with your IAM Identity Center instance's directory ID or alias. For more information about IAM Identity Center, see [What is IAM Identity Center?](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) in the AWS IAM Identity Center User Guide.
  * `sso-region` with the AWS Region where your IAM Identity Center instance is enabled.

URL | Purpose  
---|---  
<idc-directory-id-or-alias>.awsapps.com | Authentication  
oidc.<sso-region>.amazonaws.com | Authentication  
*.sso.<sso-region>.amazonaws.com | Authentication  
*.sso-portal.<sso-region>.amazonaws.com | Authentication  
*.aws.dev | Authentication  
*.awsstatic.com | Authentication  
*.console.aws.a2z.com | Authentication  
*.sso.amazonaws.com | Authentication  
<https://aws-toolkit-language-servers.amazonaws.com/>* | Kiro, language processing  
<https://aws-language-servers.us-east-1.amazonaws.com/>* | Kiro, language processing  
<https://client-telemetry.us-east-1.amazonaws.com> | Kiro, telemetry  
cognito-identity.us-east-1.amazonaws.com | Kiro, telemetry  
Page updated: November 16, 2025
[Infrastructure security](https://kiro.dev/docs/cli/privacy-and-security/infrastructure-security/)
[VPC endpoints (AWS PrivateLink)](https://kiro.dev/docs/cli/privacy-and-security/vpc-endpoints/)
On this page
  * [General urls to allowlist](https://kiro.dev/docs/cli/privacy-and-security/firewalls/#general-urls-to-allowlist)