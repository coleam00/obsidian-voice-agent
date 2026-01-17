# Privacy and security
Kiro is an AWS application that works as a standalone agentic IDE. Kiro's security framework is built around AWS's security infrastructure and follows practices to protect your development environment and data. Cloud security at AWS is the highest priority. As an AWS customer, you benefit from a data center and network architecture that is built to meet the requirements of the most security-sensitive organizations.
Security is a shared responsibility between AWS and you. The [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) describes this as security of the cloud and security in the cloud:
  * Security of the cloud – AWS is responsible for protecting the infrastructure that runs AWS services in the AWS Cloud. AWS also provides you with services that you can use securely. Third-party auditors regularly test and verify the effectiveness of our security as part of the [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/). To learn about the compliance programs that apply to Kiro, see [AWS Services in Scope by Compliance Program](https://aws.amazon.com/compliance/services-in-scope/).
  * Security in the cloud – Your responsibility is determined by the AWS service that you use. You are also responsible for other factors including the sensitivity of your data, your company’s requirements, and applicable laws and regulations


This documentation helps you understand how to apply the shared responsibility model when using Kiro. It shows you how to configure Kiro to meet your security and compliance objectives. You also learn how to use other AWS services that help you to monitor and secure your Kiro resources.
## URL fetching[](https://kiro.dev/docs/cli/privacy-and-security/#url-fetching)
In the Kiro chat module, you can paste a specific URL for your device to fetch and use it as context to help Kiro answer your query or solve your task. You are responsible for the URL content that you fetch and ensuring that your use complies with any applicable third-party terms and laws.
## Autopilot versus supervised mode[](https://kiro.dev/docs/cli/privacy-and-security/#autopilot-versus-supervised-mode)
In Kiro, Autopilot is enabled by default. You can toggle between Autopilot and Supervised mode at any time. Autopilot mode enables the agent to execute code changes, such as creating, modifying, searching, and deleting files in your codebase and run commands that impact the filesystem.
### Autopilot mode[](https://kiro.dev/docs/cli/privacy-and-security/#autopilot-mode)
In Autopilot mode, Kiro works autonomously:
  * Kiro executes multiple steps without requiring approval for each one
  * Kiro makes decisions based on its understanding of your requirements
  * You can toggle autopilot on/off in the chat interface
  * You can interrupt autopilot at any time to regain manual control


### Supervised mode[](https://kiro.dev/docs/cli/privacy-and-security/#supervised-mode)
In supervised mode, Kiro works interactively with the user, requiring their approval and guidance at each step:
  * Kiro suggests actions such as file creation, modification and deletion, but waits for user confirmation before proceeding
  * Kiro asks clarifying questions when needed
  * You can review and approve each generated document or code change, thus maintaining full control over the development process


When operating in either of these modes, you can view individual or all file changes made by the agent by selecting **View all changes** in the **Chat** module. Additionally, you can also select **Revert all changes** or revert to a [checkpoint](https://kiro.dev/docs/chat/checkpoints) to restore your files to their previous state in the filesystem locally.
## Trusted commands[](https://kiro.dev/docs/cli/privacy-and-security/#trusted-commands)
By default, Kiro requires approval before running any command. You can create your own trusted commands list by searching for **Kiro Agent: Trusted Commands** in your settings.
Kiro uses simple string prefix matching to determine if a command should be automatically trusted:
  * **Exact matching** : Commands must match exactly (e.g., `npm install`)
  * **Wildcard matching** : Use `*` to trust command variations (e.g., `npm *` trusts all npm commands)
  * **Universal trust** : Use `*` alone to trust all commands (use with extreme caution)


The system treats entire commands as single strings and only checks if they start with trusted patterns. It does not analyze command structure, chains, or special characters, putting full responsibility on you to carefully configure trusted patterns.
## Best practices[](https://kiro.dev/docs/cli/privacy-and-security/#best-practices)
Kiro provides a number of security features to consider as you develop and implement your own security policies. The following best practices are general guidelines and don’t represent a complete security solution. Because these best practices might not be appropriate or sufficient for your environment, treat them as helpful considerations rather than prescriptions.
### Protecting your resources[](https://kiro.dev/docs/cli/privacy-and-security/#protecting-your-resources)
When using GitHub or Google authentication with Kiro, be aware that the Kiro agent operates within your local environment and may access:
  * Local files and repositories
  * Environment variables
  * AWS credentials stored in your environment
  * Other configuration files with sensitive information


### Recommendations[](https://kiro.dev/docs/cli/privacy-and-security/#recommendations)
  1. **Workspace Isolation**
     * Keep sensitive projects in separate workspaces
     * Use .gitignore to prevent access to sensitive files
     * Consider using workspace trust features in your IDE
  2. **Use a Clean Environment**
     * Consider creating a dedicated user account or container environment for Kiro
     * Limit access to only the repositories and resources needed for your current project
  3. **Manage AWS Credentials Carefully**
     * Use temporary credentials with appropriate permissions
     * Consider using AWS named profiles to isolate Kiro's access
     * For sensitive work, remove AWS credentials from your environment when not needed
  4. **Repository Access Control**
     * When using GitHub authentication, review which repositories Kiro can access
     * Use repository-specific access tokens when possible
     * Regularly audit access permissions


## Remote extensions security[](https://kiro.dev/docs/cli/privacy-and-security/#remote-extensions-security)
**Warning**
**Security Note** : Using remote extensions opens a connection between your local machine and the remote machine. Only connect to secure remote machines that you trust and that are owned by a party whom you trust. A compromised remote could use the connection to execute code on your local machine. Third-party extensions including remote extensions are not developed, maintained, or managed by Kiro. We are not responsible for third-party extensions and cannot guarantee their stability, compatibility, or ongoing support.
Kiro supports Open VSX extensions, including remote SSH extensions (the community-maintained [Open Remote - SSH](https://open-vsx.org/extension/jeanp413/open-remote-ssh) extension on Open VSX is a popular choice), to provide a familiar development experience. For comprehensive information about extension compatibility and support in Kiro, see our [extension compatibility guide](https://kiro.dev/docs/guides/migrating-from-vscode/#extension-compatibility).
By following these practices, you can enjoy Kiro's capabilities while maintaining appropriate security boundaries for your development environment.
Page updated: December 12, 2025
[Concepts](https://kiro.dev/docs/cli/enterprise/concepts/)
[Data protection](https://kiro.dev/docs/cli/privacy-and-security/data-protection/)
On this page
  * [URL fetching](https://kiro.dev/docs/cli/privacy-and-security/#url-fetching)
  * [Autopilot versus supervised mode](https://kiro.dev/docs/cli/privacy-and-security/#autopilot-versus-supervised-mode)
  * [Autopilot mode](https://kiro.dev/docs/cli/privacy-and-security/#autopilot-mode)
  * [Supervised mode](https://kiro.dev/docs/cli/privacy-and-security/#supervised-mode)
  * [Trusted commands](https://kiro.dev/docs/cli/privacy-and-security/#trusted-commands)
  * [Best practices](https://kiro.dev/docs/cli/privacy-and-security/#best-practices)
  * [Protecting your resources](https://kiro.dev/docs/cli/privacy-and-security/#protecting-your-resources)
  * [Recommendations](https://kiro.dev/docs/cli/privacy-and-security/#recommendations)
  * [Remote extensions security](https://kiro.dev/docs/cli/privacy-and-security/#remote-extensions-security)