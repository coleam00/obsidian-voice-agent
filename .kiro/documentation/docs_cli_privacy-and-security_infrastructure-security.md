# Infrastructure security in Kiro
As a managed service, Kiro is protected by AWS global network security. For information about AWS security services and how AWS protects infrastructure, see [AWS Cloud Security](https://aws.amazon.com/security/). To design your AWS environment using the best practices for infrastructure security, see [Infrastructure Protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/infrastructure-protection.html) in _Security Pillar AWS Well‐Architected Framework_. You use AWS published API calls to access Kiro through the network. Clients must support the following:
  * Transport Layer Security (TLS). We require TLS 1.2 and recommend TLS 1.3.
  * Cipher suites with perfect forward secrecy (PFS) such as DHE (Ephemeral Diffie-Hellman) or ECDHE (Elliptic Curve Ephemeral Diffie-Hellman). Most modern systems such as Java 7 and later support these modes.


Additionally, requests must be signed by using an access key ID and a secret access key that is associated with an IAM principal. Or you can use the [AWS Security Token Service](https://docs.aws.amazon.com/STS/latest/APIReference/welcome.html) (AWS STS) to generate temporary security credentials to sign requests.
Page updated: November 12, 2025
[Compliance validation](https://kiro.dev/docs/cli/privacy-and-security/compliance-validation/)
[Firewalls, proxies, and data perimeters](https://kiro.dev/docs/cli/privacy-and-security/firewalls/)