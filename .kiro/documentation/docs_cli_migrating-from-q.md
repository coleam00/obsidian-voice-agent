# Upgrading from Amazon Q Developer CLI
## Overview[](https://kiro.dev/docs/cli/migrating-from-q/#overview)
Kiro CLI is the next update of the Q CLI. Your existing Q Developer CLI workflows, subscription, and authentication continue to work without any changes.
Kiro CLI leverages the Auto agent to deliver the best results at the best price, and supports advanced agent functionality and technology similar to what customers are familiar with in the Q Developer CLI (including agent mode, MCP, steering, and custom agents). Existing Q Developer CLI users will find onboarding straightforward, with additional options for logging in via social accounts and GitHub.
**Tip**
Kiro CLI will be available starting **November 17th, 2025**. If you had auto-update enabled, then on **November 24th 2025** Q Developer CLI will be automatically updated to Kiro CLI. If you had disabled auto-update, then you have to manually update Q Developer CLI using `q update` or select "Check for updates" in the Amazon Q application.
If you're familiar with Amazon Q CLI, upgrading to Kiro CLI will feel natural. This guide highlights the key differences and helps you get started quickly.
## Key differences[](https://kiro.dev/docs/cli/migrating-from-q/#key-differences)
Here is the side-by-side comparison of Kiro CLI and Amazon Q Developer
Area | Kiro CLI | Q Developer CLI  
---|---|---  
Installation | native install | dmg and zip based install  
Authentication | GitHub, Gmail, BuilderId, IAM Identity Center | BuilderId, IAM Identity Center  
Entry point | kiro-cli | q / q chat  
Rules | Kiro steering | Amazon Q rules  
Subscriptions | Q Developer and Kiro | Q Developer and Kiro  
Features | MCP, Custom agents, hooks | MCP, Custom agents, hooks  
License | AWS Intellectual Property License | Apache  
See the [Authentication guide](https://kiro.dev/docs/cli/authentication) for details.
## Frequently asked questions[](https://kiro.dev/docs/cli/migrating-from-q/#frequently-asked-questions)
**1. What is Kiro, and how does it relate to Q Developer?**
Kiro is a standalone agentic development experience that helps you go from concept to production with spec-driven development. From simple to complex tasks, Kiro works alongside you to turn prompts into detailed specs, then into working code, docs, and tests—so what you build is exactly what you want and ready to share with your team. Kiro leverages some of the advanced Q Developer functionality and technology (agent mode, MCP, steering, CLI) and adds a streamlined but opinionated developer experience for working with AI which feels familiar because it's based on Q Developer CLI.
**2. How will I upgrade from Q Developer CLI to the Kiro CLI?**
You can simply do `q update` or enable auto-update to switch to Kiro CLI.
**3. What if I don’t want to upgrade to the Kiro CLI? Can I keep my Q Developer CLI access?**
Yes, you can continue to use Amazon Q Developer CLI. However, new features and fixes will only be available for Kiro CLI, which leverages some of the underlying agentic CLI features of Q CLI in a streamlined developer experience. Existing Q Developer CLI users will find the experience familiar, and onboarding straightforward, so we strongly recommend they should consider switching.
**4. What terms will apply to Kiro CLI?**
Just like with Q Developer CLI, your use of the underlying agentic capabilities in Kiro CLI is subject to the AWS Customer Agreement (or other agreement with us governing your use of AWS services) and Service Terms. However, the Kiro CLI software is licensed under the AWS Intellectual Property License, while the Q Developer CLI software was licensed under Apache 2.0.
**5. What is the impact to my current usage of Amazon Q Developer CLI? Do I have to change my automation and configuration files?**
Kiro CLI is backwards compatible with Amazon Q Developer CLI. You can still continue using the `q` and `q chat` entry points. All the functionality in Amazon Q Developer CLI is available in Kiro CLI. You can continue using Amazon Q rules and configuration with Kiro CLI.
**6. What will change when I switch to Kiro CLI?**
We are making it easy for your team to work with Kiro regardless of whether developers prefer Kiro IDE or Kiro CLI. To learn more about the changes, review the [changes in detail](https://kiro.dev/docs/cli/migrating-from-q/#kiro-cli-changes).
**7. Will Kiro CLI work with my Q Developer Pro subscription?**
Yes, you can use Kiro CLI with your Q Developer Pro subscription. Kiro CLI will also support a Kiro subscription.
**8. How does Kiro pricing work?**
Kiro offers flexible pricing tiers designed around how developers use Kiro. For more on pricing, see <https://kiro.dev/pricing/>.
**9. As a current Q Developer Pro subscription user, why should I consider upgrading to a paid Kiro subscription plan?**
Kiro offers 3 different pricing tiers that better map to developer needs, and each pricing tier supports overages. Overages are not supported with the Q Developer Pro subscription plan.
**10: As a current Q Developer Pro user, what is the process for upgrading to a Kiro subscription plan?**
The Kiro dashboard will show the subscriptions for both Kiro and Q Developer separately. For every group or user, an admin can go to their Q subscriptions, select them and upgrade to a Kiro subscription. Changes in subscription will move groups and users from the subscription tab under Q Developer to the subscription tab in Kiro. Customers can migrate users as they see fit, across an entire profile from a member account, or across groups or individual users from the same profile. Upgrades happen at a user level, so customers have fine-grained control over the migration process.
**11. Do you provide an output indemnity for Kiro subscribers? If I’m a Q Developer Pro tier user and I upgrade to a paid Kiro subscription, does the output indemnity apply to me?**
Yes, just like we do for Q Developer Pro users, we provide an output indemnity for paid Kiro subscribers. See Section 50.10 of the Service Terms for more details.
**12. Does Kiro use my content to train any models?**
We do not use content from Kiro Pro, Pro+, or Power users that access Kiro through AWS IAM Identity Center. If you have an Amazon Q Developer Pro subscription and access Kiro through your AWS account with the Amazon Q Developer Pro subscription, then Kiro will not use your content for service improvement. We may use certain content from Kiro Free Tier and Kiro individual subscribers (those that access Kiro through a social login provider or AWS Builder ID) for service improvement.
**13. Can I control telemetry sharing (usage data, performance metrics) for Kiro at the Org level?**
We do not collect telemetry from Kiro Pro, Pro+, or Power users that access Kiro through AWS IAM Identity Center. However, enterprise admins can configure Kiro to collect user activity reports for the users in your org.
**14. Can I go back to Amazon Q Developer CLI?**
To install Amazon Q Developer CLI, download the binary for your platform/OS. Uninstall Kiro CLI using `kiro-cli uninstall` and install the Amazon Q Developer CLI.
You can download Amazon Q Developer CLI v1.19.7 for the specific platform:
  * [MacOS](https://desktop-release.q.us-east-1.amazonaws.com/latest/Amazon%20Q.dmg)
  * [Linux x86-64](https://desktop-release.q.us-east-1.amazonaws.com/latest/q-x86_64-linux.zip)
  * [Linux ARM](https://desktop-release.q.us-east-1.amazonaws.com/latest/q-aarch64-linux.zip)


**Warning**
Any new prompts, agents and steering files you created using Kiro CLI will not be available in Amazon Q Developer CLI. Refer to the configuration file path section to copy files.
## Kiro CLI Changes[](https://kiro.dev/docs/cli/migrating-from-q/#kiro-cli-changes)
### One-time migration during Kiro CLI installation[](https://kiro.dev/docs/cli/migrating-from-q/#one-time-migration-during-kiro-cli-installation)
Here's what happens during the one-time migration when you install Kiro CLI:
  1. Prompts, agents from `~/.aws/amazonq` folder are copied to `~/.kiro` folder with the same names
  2. MCP configuration from `~/.aws/amazonq/mcp.json` is copied to `~/.kiro/settings/mcp.json`. If there are conflicts, skip copying those MCP servers
  3. Files from `rules` folder in ~/.aws/amazonq folder are copied to `~/.kiro/steering` folder with the same names
  4. A `cli.json` file is created with settings from Amazon Q Developer CLI
  5. Kiro CLI will continue to read `.amazonq` folder in your project. So your existing rules, agents, and MCP settings in your project will continue to work as-is 
     * If you save a new prompt or agent configurations, they will be saved to `.kiro` folder in your projeect.
     * If both folders exist in your project, we'll read from `.kiro` folder


**Important**
When you add new project level prompts or agents, they will be saved to the `.kiro` folder in the project and not `.amazonq` folder
  1. q and q chat will continue to work, although we recommend using kiro-cli (both kiro-cli and kiro-cli chat will work)
  2. Tools names have been simplified, but existing tool names will continue to work: 
     * Changes -> `fs_read` to `read`, `fs_write` to `write` , `use_aws` to `aws`, `execute_bash` to `shell`, `report_issue` to `report`


### Configuration file paths[](https://kiro.dev/docs/cli/migrating-from-q/#configuration-file-paths)
Kiro CLI uses different configuration paths than Amazon Q Developer CLI, but maintains backward compatibility:
Configuration | Scope | Kiro CLI | Q Developer CLI  
---|---|---|---  
MCP servers | User | `~/.kiro/settings/mcp.json` | `~/.aws/amazonq/mcp.json`  
| Workspace | `.kiro/settings/mcp.json` | `.amazonq/mcp.json`  
Prompts | User | `~/.kiro/prompts` | `~/.aws/amazonq/prompts`  
| Workspace | `.kiro/prompts` | `.amazonq/prompts`  
Custom agents | User | `~/.kiro/agents` | `~/.aws/amazonq/cli-agents`  
| Workspace | `.kiro/agents` | `.amazonq/cli-agents`  
Rules / Steering | User | `~/.kiro/steering` | `~/.aws/amazonq/rules`  
| Workspace | `.kiro/steering` | `.amazonq/rules`  
Settings | Global | `~/.kiro/settings/cli.json` | -  
### Important changes[](https://kiro.dev/docs/cli/migrating-from-q/#important-changes)
  * Kiro CLI will **not modify** your existing `.amazonq` folders
  * Authentication and subscription management will use Kiro web portal
  * MCP servers, agents, rules, and prompts automatically copied from `~/.aws/amazonq` folder to the appropriate folders (refer above) in `~/.kiro` during installation
  * Logs will be written to `$TMPDIR/kiro-log`
  * Tool names are different, but are backwards compatible so that your existing custom agents will continue to work
  * Default agent name changed to `kiro_default`. Default agent includes paths for both Amazon Q and Kiro. 
    * `/agent list` will list `kiro_default` as an agent with "No path found", because the agent configuration is in memory.
  * UI with updated colors and names
  * Default agent will support both Amazon Q rules and Kiro steering
  * Kiro CLI supports Gmail and GitHub authentication alongside Builder ID and IAM Identity Center


**Important**
If your project has both `.kiro` and `.amazonq` folders, configuration will be loaded from the `.kiro` folder. You will see a warning about this when you start a new session.
### Getting help[](https://kiro.dev/docs/cli/migrating-from-q/#getting-help)
If you encounter issues during migration:
  1. Check the [CLI Commands Reference](https://kiro.dev/docs/cli/reference/cli-commands)
  2. Review [Chat documentation](https://kiro.dev/docs/cli/chat)
  3. Contact support through the Kiro dashboard


### Next steps[](https://kiro.dev/docs/cli/migrating-from-q/#next-steps)
  * Explore [Chat features](https://kiro.dev/docs/cli/chat)
  * Learn about [Custom Agents](https://kiro.dev/docs/cli/custom-agents)
  * Try [MCP integration](https://kiro.dev/docs/cli/mcp)
  * Set up [Agent Hooks](https://kiro.dev/docs/cli/hooks)


Page updated: November 19, 2025
[Settings](https://kiro.dev/docs/cli/reference/settings/)
On this page
  * [Overview](https://kiro.dev/docs/cli/migrating-from-q/#overview)
  * [Key differences](https://kiro.dev/docs/cli/migrating-from-q/#key-differences)
  * [Frequently asked questions](https://kiro.dev/docs/cli/migrating-from-q/#frequently-asked-questions)
  * [Kiro CLI Changes](https://kiro.dev/docs/cli/migrating-from-q/#kiro-cli-changes)
  * [One-time migration during Kiro CLI installation](https://kiro.dev/docs/cli/migrating-from-q/#one-time-migration-during-kiro-cli-installation)
  * [Configuration file paths](https://kiro.dev/docs/cli/migrating-from-q/#configuration-file-paths)
  * [Important changes](https://kiro.dev/docs/cli/migrating-from-q/#important-changes)
  * [Getting help](https://kiro.dev/docs/cli/migrating-from-q/#getting-help)
  * [Next steps](https://kiro.dev/docs/cli/migrating-from-q/#next-steps)