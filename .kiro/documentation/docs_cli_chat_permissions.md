# Managing tool permissions
You can use the `/tools` command to manage permissions for tools that Kiro uses to perform actions on your system. This provides granular control over what actions Kiro can perform.
Tools commands
Command | Description  
---|---  
`help` | Shows help related to tools.  
`trust` | Trusts a specific tool for the session.  
`untrust` | Reverts a tool to per-request confirmation.  
`trust-all` | Trusts all tools (equivalent to deprecated /acceptall).  
`reset` | Resets all tools to default permission levels.  
To view the current permission settings for all tools:
```

$ kiro-cli chat
Kiro> /tools


```

This displays a list of all available tools and their current permission status (trusted or per-request).
Tool permissions have two possible states:
  * _Trusted_ : Kiro can use the tool without asking for confirmation each time.
  * _Per-request_ : Kiro must ask for your confirmation each time before using the tool.


To trust or untrust a specific tool for the current session:
```

Kiro> /tools trust read
Kiro> /tools untrust shell


```

You can also trust all tools at once with `/tools trust-all`(equivalent to the deprecated `/acceptall` command):
```

Kiro> /tools trust-all


```

###### Warning[](https://kiro.dev/docs/cli/chat/permissions/#warning)
Using `/tools trust-all` carries risks. For more information, see [Understanding security risks](https://kiro.dev/docs/cli/chat/permissions/command-line-chat-security.html#command-line-chat-security-risks "./command-line-chat-security.html#command-line-chat-security-risks") .
The following image shows the status of the CLI tools when they are all in their default trust status.
The following tools are natively available for Kiro to use:
Available tools
Tool | Description  
---|---  
`read` | Reads files and directories on your system.  
`write` | Creates and modifies files on your system.  
`shell` | Executes bash commands on your system.  
`aws` | Makes AWS CLI calls to interact with AWS services.  
`report` | Opens a browser to report an issue with the chat to AWS.  
When Kiro attempts to use a tool that doesn't have explicit permission, it will ask for your approval before proceeding. You can choose to allow or deny the action, or trust the tool for the remainder of your session.
Each tool has a default trust behavior. `read` is the only tool that is trusted by default.
Here are some examples of when to use different permission levels:
  * _Trust fs_read_ : When you want Kiro to read files without confirmation, such as when exploring a codebase.
  * _Trust fs_write_ : When you're actively working on a project and want Kiro to help you create or modify files.
  * _Untrust execute_bash_ : When working in sensitive environments where you want to review all commands before execution.
  * _Untrust use_aws_ : When working with production AWS resources to prevent unintended changes.


When Kiro uses a tool, it shows you the trust permission being used.
You can also specify trust permissions as part of starting a `kiro-cli chat` session.
Page updated: November 18, 2025
[Responding to messages](https://kiro.dev/docs/cli/chat/responding/)
[Working with Git](https://kiro.dev/docs/cli/chat/git-aware-selection/)