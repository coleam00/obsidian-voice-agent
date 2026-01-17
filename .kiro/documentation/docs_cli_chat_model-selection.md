# Model selection
Kiro provides multiple powerful AI agent options to handle your development tasks: **Auto** , **Claude Sonnet 4.0** , **Claude Sonnet 4.5** , **Claude Haiku 4.5** , and **Claude Opus 4.5**. Each offers distinct advantages depending on your needs and usage patterns.
## Available models[](https://kiro.dev/docs/cli/chat/model-selection/#available-models)
### Auto (recommended)[](https://kiro.dev/docs/cli/chat/model-selection/#auto-recommended)
Auto is Kiro's default intelligent model router that combines multiple frontier models with advanced optimization techniques.
**Key benefits:**
  * **Cost-effective** – Approximately 23% less expensive than direct Sonnet 4 usage
  * **Smart routing** – Automatically chooses the optimal model for each task
  * **Consistent quality** – Delivers Sonnet 4-level results across different task types
  * **Plan efficiency** – Makes your usage limits go further


#### What model does Auto use?[](https://kiro.dev/docs/cli/chat/model-selection/#what-model-does-auto-use)
Auto uses best in class LLM models (Claude Sonnet 4 and alike) to provide you the best quality for the type of tasks assigned to the agent. We maintain a very high bar to ensure that the quality of what is offered under Auto compares to or exceeds the quality of separate models made available to our users.
### Claude Sonnet 4.0[](https://kiro.dev/docs/cli/chat/model-selection/#claude-sonnet-40)
Direct access to Anthropic's Claude Sonnet 4.0 model for users who prefer consistent model selection or have specific requirements for using this particular model.
**Key benefits:**
  * **Predictable behavior** – Same model for all interactions
  * **Direct access** – No routing or optimization layers
  * **Full control** – Complete transparency in model selection


### Claude Sonnet 4.5[](https://kiro.dev/docs/cli/chat/model-selection/#claude-sonnet-45)
Anthropic's best model for complex agents and coding, with the highest intelligence across most tasks.
**Key benefits:**
  * **Coding excellence** – Advanced state-of-the-art on SWE-bench Verified
  * **Agent capabilities** – Extended autonomous operation for hours with effective tool usage
  * **Enhanced reasoning** – Improved planning, system design, and security engineering


### Claude Opus 4.5[](https://kiro.dev/docs/cli/chat/model-selection/#claude-opus-45)
Anthropic's most intelligent model combining maximum capability with practical performance. Ideal for complex specialized tasks, professional software engineering, and advanced agents.
**Key benefits:**
  * **Maximum intelligence** – Step-change improvements in reasoning, coding, and problem-solving
  * **Practical performance** – More accessible price point than previous Opus models
  * **Complex reasoning** – Better balance of tradeoffs and ambiguity across multiple systems


### Claude Haiku 4.5[](https://kiro.dev/docs/cli/chat/model-selection/#claude-haiku-45)
Anthropic's fastest and most intelligent Haiku model with near-frontier performance. Delivers intelligence matching Sonnet 4 at significantly lower cost and faster speed.
**Key benefits:**
  * **Near-frontier intelligence** – Matches Sonnet 4 performance across reasoning and coding
  * **Blazing speed** – More than twice the speed of Sonnet 4
  * **Cost-effective** – Near-frontier intelligence at one-third the cost
  * **Extended thinking** – First Haiku model with advanced reasoning capabilities


## Cost comparison[](https://kiro.dev/docs/cli/chat/model-selection/#cost-comparison)
Understanding the credit consumption differences:
Model | Credit Usage | Example Task Cost  
---|---|---  
**Claude Haiku 4.5** | 0.4x | 4 credits  
**Auto** | 1.0x | 10 credits  
**Claude Sonnet 4.0** | 1.3x | 13 credits  
**Claude Sonnet 4.5** | 1.3x | 13 credits  
**Claude Opus 4.5** | 2.2x | 22 credits  
## Choosing the right model[](https://kiro.dev/docs/cli/chat/model-selection/#choosing-the-right-model)
### Claude Haiku 4.5[](https://kiro.dev/docs/cli/chat/model-selection/#claude-haiku-45-1)
Consider using Haiku 4.5 when:
  * **Speed is critical** – You need fast responses for interactive experiences
  * **Cost efficiency matters** – Near-frontier intelligence at one-third the cost
  * **High-volume processing** – Cost-effective intelligence for large-scale deployments
  * **Real-time applications** – Fast turnaround for user-facing features


### Auto[](https://kiro.dev/docs/cli/chat/model-selection/#auto)
Consider using Auto when:
  * **Cost efficiency matters** – You want to maximize your plan's value
  * **General development work** – Most coding, debugging, and planning tasks
  * **Variable task types** – Working on diverse projects with different requirements
  * **Plan optimization** – You want your limits to stretch further


### Sonnet 4.0 & Sonnet 4.5[](https://kiro.dev/docs/cli/chat/model-selection/#sonnet-40--sonnet-45)
Consider using Sonnet 4.0 or Sonnet 4.5 when:
  * **Consistency is critical** – You need predictable model behavior
  * **Specific requirements** – Your workflow depends on Sonnet 4's particular capabilities
  * **Model transparency** – You prefer knowing exactly which model handles each request
  * **Budget flexibility** – Higher costs aren't a primary concern


### Claude Opus 4.5[](https://kiro.dev/docs/cli/chat/model-selection/#claude-opus-45-1)
Consider using Opus 4.5 when:
  * **Maximum intelligence needed** – Most complex specialized tasks requiring top-tier reasoning
  * **Professional software engineering** – Sophisticated production development challenges
  * **Advanced agents** – Long-running autonomous tasks with complex decision-making
  * **Critical implementations** – High-stakes features where quality is paramount


## How to switch models[](https://kiro.dev/docs/cli/chat/model-selection/#how-to-switch-models)
### In the chat interface[](https://kiro.dev/docs/cli/chat/model-selection/#in-the-chat-interface)
![/model command usage](https://kiro.dev/images/cli-model-selection.png?h=fa2bf44f)
### Kiro CLI setting[](https://kiro.dev/docs/cli/chat/model-selection/#kiro-cli-setting)
bash
```

kiro-cli settings chat.defaultModel claude-sonnet4


```

### Persisting your model selection[](https://kiro.dev/docs/cli/chat/model-selection/#persisting-your-model-selection)
To save your current model as the default for all future sessions:
bash
```

> /model set-current-as-default


```

This stores your preference in `~/.kiro/settings/cli.json`. New sessions will automatically use this model.
## Best practices[](https://kiro.dev/docs/cli/chat/model-selection/#best-practices)
### Maximizing efficiency[](https://kiro.dev/docs/cli/chat/model-selection/#maximizing-efficiency)
  * **Start with Auto** – Use it as your default for most tasks
  * **Use Haiku for speed** – Near-frontier intelligence with fast responses and lower cost
  * **Use Sonnet for agents** – Best for complex coding and autonomous workflows
  * **Reserve Opus for maximum intelligence** – Use for the most complex specialized tasks
  * **Monitor usage** – Track how different models affect your plan consumption
  * **Experiment** – Try different models for similar tasks to compare results


### Cost management[](https://kiro.dev/docs/cli/chat/model-selection/#cost-management)
  * **Plan accordingly** – Factor model choice into your tier selection
  * **Track patterns** – Understand which tasks benefit most from each model
  * **Optimize workflows** – Adjust development practices based on model strengths
  * **Consider overages** – Enable if you need flexibility beyond plan limits


Page updated: December 19, 2025
[Chat](https://kiro.dev/docs/cli/chat/)
[Subagents](https://kiro.dev/docs/cli/chat/subagents/)
On this page
  * [Available models](https://kiro.dev/docs/cli/chat/model-selection/#available-models)
  * [Auto (recommended)](https://kiro.dev/docs/cli/chat/model-selection/#auto-recommended)
  * [What model does Auto use?](https://kiro.dev/docs/cli/chat/model-selection/#what-model-does-auto-use)
  * [Claude Sonnet 4.0](https://kiro.dev/docs/cli/chat/model-selection/#claude-sonnet-40)
  * [Claude Sonnet 4.5](https://kiro.dev/docs/cli/chat/model-selection/#claude-sonnet-45)
  * [Claude Opus 4.5](https://kiro.dev/docs/cli/chat/model-selection/#claude-opus-45)
  * [Claude Haiku 4.5](https://kiro.dev/docs/cli/chat/model-selection/#claude-haiku-45)
  * [Cost comparison](https://kiro.dev/docs/cli/chat/model-selection/#cost-comparison)
  * [Choosing the right model](https://kiro.dev/docs/cli/chat/model-selection/#choosing-the-right-model)
  * [Claude Haiku 4.5](https://kiro.dev/docs/cli/chat/model-selection/#claude-haiku-45-1)
  * [Auto](https://kiro.dev/docs/cli/chat/model-selection/#auto)
  * [Sonnet 4.0 & Sonnet 4.5](https://kiro.dev/docs/cli/chat/model-selection/#sonnet-40--sonnet-45)
  * [Claude Opus 4.5](https://kiro.dev/docs/cli/chat/model-selection/#claude-opus-45-1)
  * [How to switch models](https://kiro.dev/docs/cli/chat/model-selection/#how-to-switch-models)
  * [In the chat interface](https://kiro.dev/docs/cli/chat/model-selection/#in-the-chat-interface)
  * [Kiro CLI setting](https://kiro.dev/docs/cli/chat/model-selection/#kiro-cli-setting)
  * [Persisting your model selection](https://kiro.dev/docs/cli/chat/model-selection/#persisting-your-model-selection)
  * [Best practices](https://kiro.dev/docs/cli/chat/model-selection/#best-practices)
  * [Maximizing efficiency](https://kiro.dev/docs/cli/chat/model-selection/#maximizing-efficiency)
  * [Cost management](https://kiro.dev/docs/cli/chat/model-selection/#cost-management)