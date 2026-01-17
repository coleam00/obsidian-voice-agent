# Thinking tool
The thinking tool enables Kiro to show its reasoning process when working through complex problems, providing transparency into how conclusions are reached.
## Overview[](https://kiro.dev/docs/cli/experimental/thinking/#overview)
When enabled, the thinking tool allows Kiro to break down complex reasoning into visible steps, helping you understand the decision-making process and learn from the AI's approach to problem-solving.
## Enabling thinking tool[](https://kiro.dev/docs/cli/experimental/thinking/#enabling-thinking-tool)
bash
```

kiro-cli settings chat.enableThinking true


```

Or use the experiment command:
bash
```

/experiment
# Select "Thinking" from the list


```

## How it works[](https://kiro.dev/docs/cli/experimental/thinking/#how-it-works)
When Kiro encounters a complex problem that requires multi-step reasoning, it will:
  1. **Show its thought process** as it works through the problem
  2. **Break down the reasoning** into logical steps
  3. **Explain intermediate conclusions** before reaching the final answer
  4. **Make the decision-making transparent** so you can follow along


## When thinking appears[](https://kiro.dev/docs/cli/experimental/thinking/#when-thinking-appears)
The thinking tool is automatically invoked by Kiro when:
  * **Complex problem-solving** requires multiple logical steps
  * **Analyzing trade-offs** between different approaches
  * **Planning multi-step implementations** with dependencies
  * **Debugging complex issues** that need systematic analysis
  * **Making architectural decisions** with multiple considerations


## Example usage[](https://kiro.dev/docs/cli/experimental/thinking/#example-usage)
### Without thinking tool[](https://kiro.dev/docs/cli/experimental/thinking/#without-thinking-tool)
```

> What's the best way to implement caching for our API?

I recommend using Redis for caching your API responses...


```

### With thinking tool[](https://kiro.dev/docs/cli/experimental/thinking/#with-thinking-tool)
```

> What's the best way to implement caching for our API?

🧠 Thinking...

Let me think through the caching requirements:

1. First, I need to consider the type of data being cached
   - API responses suggest read-heavy workload
   - Need to handle cache invalidation

2. Evaluating caching solutions:
   - In-memory (fast but limited by RAM)
   - Redis (distributed, persistent, feature-rich)
   - Memcached (simple, fast, but less features)

3. Considering your use case:
   - API responses benefit from distributed cache
   - Need TTL support for automatic expiration
   - May need cache invalidation on updates

4. Redis appears best because:
   - Supports complex data structures
   - Built-in TTL and eviction policies
   - Can be distributed across nodes
   - Persistent if needed

Based on this analysis, I recommend using Redis for caching your API responses...


```

## Benefits[](https://kiro.dev/docs/cli/experimental/thinking/#benefits)
### For learning[](https://kiro.dev/docs/cli/experimental/thinking/#for-learning)
  * **Understand reasoning patterns** : See how complex problems are broken down
  * **Learn problem-solving approaches** : Observe systematic analysis
  * **Identify gaps in logic** : Spot where reasoning might be flawed


### For debugging[](https://kiro.dev/docs/cli/experimental/thinking/#for-debugging)
  * **Trace decision paths** : Understand why certain recommendations were made
  * **Verify assumptions** : Check if the AI's assumptions match your context
  * **Catch errors early** : Spot logical errors before implementation


### For complex tasks[](https://kiro.dev/docs/cli/experimental/thinking/#for-complex-tasks)
  * **Follow multi-step plans** : See how complex tasks are decomposed
  * **Understand dependencies** : Identify relationships between steps
  * **Validate approach** : Confirm the reasoning aligns with your goals


## Use cases[](https://kiro.dev/docs/cli/experimental/thinking/#use-cases)
### Architectural decisions[](https://kiro.dev/docs/cli/experimental/thinking/#architectural-decisions)
```

> Should we use microservices or a monolith for our new project?

🧠 Thinking...

Let me analyze this architectural decision:

1. Project characteristics to consider:
   - Team size and structure
   - Expected scale and growth
   - Deployment requirements
   - Development velocity needs

2. Microservices advantages:
   - Independent scaling
   - Technology flexibility
   - Isolated failures
   - But: increased complexity, operational overhead

3. Monolith advantages:
   - Simpler deployment
   - Easier debugging
   - Lower operational cost
   - But: scaling limitations, tight coupling

4. Decision factors:
   - Small team → Monolith likely better
   - Unclear requirements → Start with monolith
   - Need rapid iteration → Monolith faster initially
   - Can refactor to microservices later if needed

Based on this analysis...


```

### Algorithm selection[](https://kiro.dev/docs/cli/experimental/thinking/#algorithm-selection)
```

> What sorting algorithm should I use for this data?

🧠 Thinking...

Let me think through the sorting requirements:

1. Data characteristics:
   - Size of dataset
   - Is data partially sorted?
   - Memory constraints
   - Stability requirements

2. Algorithm options:
   - Quick Sort: O(n log n) average, O(n²) worst
   - Merge Sort: O(n log n) guaranteed, stable
   - Heap Sort: O(n log n), in-place
   - Tim Sort: Optimized for real-world data

3. Trade-offs:
   - If data is partially sorted → Tim Sort excels
   - If memory is limited → Heap Sort (in-place)
   - If stability matters → Merge Sort or Tim Sort
   - For general case → Quick Sort often fastest

4. Recommendation depends on...


```

### Debugging complex issues[](https://kiro.dev/docs/cli/experimental/thinking/#debugging-complex-issues)
```

> My application is slow but I don't know why

🧠 Thinking...

Let me systematically analyze potential performance issues:

1. Common performance bottlenecks:
   - Database queries (N+1 problem, missing indexes)
   - Network latency (API calls, external services)
   - Memory issues (leaks, excessive allocation)
   - CPU-bound operations (complex calculations)

2. Diagnostic approach:
   - First, profile to identify hotspots
   - Check database query patterns
   - Monitor network requests
   - Analyze memory usage patterns

3. Most likely culprits based on typical patterns:
   - Database queries often account for 60-80% of slowness
   - Should start there before optimizing code

4. Recommended investigation order...


```

## Configuration[](https://kiro.dev/docs/cli/experimental/thinking/#configuration)
### Enable/disable[](https://kiro.dev/docs/cli/experimental/thinking/#enabledisable)
bash
```

# Enable
kiro-cli settings chat.enableThinking true

# Disable
kiro-cli settings chat.enableThinking false

# Check status
kiro-cli settings chat.enableThinking


```

## Limitations[](https://kiro.dev/docs/cli/experimental/thinking/#limitations)
### Performance impact[](https://kiro.dev/docs/cli/experimental/thinking/#performance-impact)
  * **Slower responses** : Thinking adds time to generate responses
  * **More tokens used** : Thinking process consumes additional tokens
  * **Longer output** : Responses are more verbose


### When not to use[](https://kiro.dev/docs/cli/experimental/thinking/#when-not-to-use)
  * **Simple questions** : Thinking overhead not needed for straightforward queries
  * **Quick iterations** : May slow down rapid back-and-forth
  * **Well-defined tasks** : When you just need the answer, not the reasoning


## Best practices[](https://kiro.dev/docs/cli/experimental/thinking/#best-practices)
### When to enable[](https://kiro.dev/docs/cli/experimental/thinking/#when-to-enable)
  * **Learning new concepts** : Understand the reasoning behind recommendations
  * **Complex decisions** : Need to validate the decision-making process
  * **Debugging** : Want to see systematic problem analysis
  * **Code reviews** : Understand why certain approaches are suggested


### When to disable[](https://kiro.dev/docs/cli/experimental/thinking/#when-to-disable)
  * **Simple tasks** : Straightforward questions don't need reasoning
  * **Speed priority** : Need quick responses without explanation
  * **Familiar territory** : Already understand the reasoning patterns


### Workflow integration[](https://kiro.dev/docs/cli/experimental/thinking/#workflow-integration)
  1. **Enable for complex tasks** : Turn on when starting difficult problems
  2. **Learn from reasoning** : Observe how problems are broken down
  3. **Disable for execution** : Turn off when implementing known solutions
  4. **Re-enable for review** : Turn back on when validating approaches


## Troubleshooting[](https://kiro.dev/docs/cli/experimental/thinking/#troubleshooting)
### Thinking not appearing[](https://kiro.dev/docs/cli/experimental/thinking/#thinking-not-appearing)
  1. **Verify it's enabled** :
bash
```

kiro-cli settings chat.enableThinking


```

  2. **Try a complex question** : Simple questions may not trigger thinking
  3. **Restart chat session** : Changes may require new session


### Too much thinking[](https://kiro.dev/docs/cli/experimental/thinking/#too-much-thinking)
If thinking output is overwhelming:
  1. **Disable for simpler tasks** :
bash
```

kiro-cli settings chat.enableThinking false


```

  2. **Ask for concise answers** : Request brief responses explicitly
  3. **Use for specific questions** : Enable only when needed


## Related features[](https://kiro.dev/docs/cli/experimental/thinking/#related-features)
  * [Experimental Features](https://kiro.dev/docs/cli/experimental)
  * [Tangent Mode](https://kiro.dev/docs/cli/experimental/tangent-mode) - Explore reasoning without affecting main conversation
  * [TODO Lists](https://kiro.dev/docs/cli/experimental/todo-lists) - Break down complex tasks


## Next steps[](https://kiro.dev/docs/cli/experimental/thinking/#next-steps)
  * [Enable other experimental features](https://kiro.dev/docs/cli/experimental)
  * [Configure settings](https://kiro.dev/docs/cli/settings)
  * [Learn about custom agents](https://kiro.dev/docs/cli/custom-agents)


Page updated: November 16, 2025
[TODO lists](https://kiro.dev/docs/cli/experimental/todo-lists/)
[Checkpointing](https://kiro.dev/docs/cli/experimental/checkpointing/)
On this page
  * [Overview](https://kiro.dev/docs/cli/experimental/thinking/#overview)
  * [Enabling thinking tool](https://kiro.dev/docs/cli/experimental/thinking/#enabling-thinking-tool)
  * [How it works](https://kiro.dev/docs/cli/experimental/thinking/#how-it-works)
  * [When thinking appears](https://kiro.dev/docs/cli/experimental/thinking/#when-thinking-appears)
  * [Example usage](https://kiro.dev/docs/cli/experimental/thinking/#example-usage)
  * [Without thinking tool](https://kiro.dev/docs/cli/experimental/thinking/#without-thinking-tool)
  * [With thinking tool](https://kiro.dev/docs/cli/experimental/thinking/#with-thinking-tool)
  * [Benefits](https://kiro.dev/docs/cli/experimental/thinking/#benefits)
  * [For learning](https://kiro.dev/docs/cli/experimental/thinking/#for-learning)
  * [For debugging](https://kiro.dev/docs/cli/experimental/thinking/#for-debugging)
  * [For complex tasks](https://kiro.dev/docs/cli/experimental/thinking/#for-complex-tasks)
  * [Use cases](https://kiro.dev/docs/cli/experimental/thinking/#use-cases)
  * [Architectural decisions](https://kiro.dev/docs/cli/experimental/thinking/#architectural-decisions)
  * [Algorithm selection](https://kiro.dev/docs/cli/experimental/thinking/#algorithm-selection)
  * [Debugging complex issues](https://kiro.dev/docs/cli/experimental/thinking/#debugging-complex-issues)
  * [Configuration](https://kiro.dev/docs/cli/experimental/thinking/#configuration)
  * [Enable/disable](https://kiro.dev/docs/cli/experimental/thinking/#enabledisable)
  * [Limitations](https://kiro.dev/docs/cli/experimental/thinking/#limitations)
  * [Performance impact](https://kiro.dev/docs/cli/experimental/thinking/#performance-impact)
  * [When not to use](https://kiro.dev/docs/cli/experimental/thinking/#when-not-to-use)
  * [Best practices](https://kiro.dev/docs/cli/experimental/thinking/#best-practices)
  * [When to enable](https://kiro.dev/docs/cli/experimental/thinking/#when-to-enable)
  * [When to disable](https://kiro.dev/docs/cli/experimental/thinking/#when-to-disable)
  * [Workflow integration](https://kiro.dev/docs/cli/experimental/thinking/#workflow-integration)
  * [Troubleshooting](https://kiro.dev/docs/cli/experimental/thinking/#troubleshooting)
  * [Thinking not appearing](https://kiro.dev/docs/cli/experimental/thinking/#thinking-not-appearing)
  * [Too much thinking](https://kiro.dev/docs/cli/experimental/thinking/#too-much-thinking)
  * [Related features](https://kiro.dev/docs/cli/experimental/thinking/#related-features)
  * [Next steps](https://kiro.dev/docs/cli/experimental/thinking/#next-steps)