# Chat
The Kiro CLI provides an interactive chat mode that lets you have natural conversations with AI directly in your terminal. This feature brings the power of conversational AI to your command-line workflow.
## Starting a session[](https://kiro.dev/docs/cli/chat/#starting-a-session)
To start a chat session
bash
```

kiro-cli


```

Or start a chat with a specific context:
bash
```

kiro-cli --agent myagent


```

## Entering multi-line statements[](https://kiro.dev/docs/cli/chat/#entering-multi-line-statements)
To enter multi-line statements, use the `/editor` command or type `Ctrl(^) + J` to insert new-line for multi-line prompt
bash
```

/editor


```

This opens your default editor (defaults to vi) where you can compose longer, multi-line prompts. After you save and close the editor, the content will be sent as your message to Kiro.
You can also:
  * Use the [`/reply`](https://kiro.dev/docs/cli/chat/responding) command to open your editor with the most recent assistant message quoted for reply, which is useful for multi-line responses to previous messages.


## Conversation persistence[](https://kiro.dev/docs/cli/chat/#conversation-persistence)
Kiro can remember your conversations based on the folder where you started them. When you start a session where you previously chatted with Kiro, you can tell Kiro to automatically load that conversation history, allowing you to seamlessly continue your discussion.
### Directory-based persistence[](https://kiro.dev/docs/cli/chat/#directory-based-persistence)
If it's your first time chatting in that directory, Kiro will start a new conversation (taking into consideration any designated context).
To explicitly resume a conversation in the current directory, use:
bash
```

$ kiro-cli chat --resume


```

### Manually saving and loading conversations[](https://kiro.dev/docs/cli/chat/#manually-saving-and-loading-conversations)
You can also manually save and load conversations using the following commands while in a chat session:
bash
```

    /save [path] – Saves your current conversation to a JSON file.

        Add -f or --force to overwrite an existing file

        Examples:

        /save ./my-project-conversation -f

        /save /home/user/project/my-project-conversation.json

        You cannot use ~ to denote your home directory.

    /load [path] – Loads a conversation from a previously saved JSON file

        Example: /load ./my-project-conversation.json


```

**Info**
The `/save` and `/load` commands operate independently of the directory where the conversation was originally created. When loading a conversation, be mindful that it will replace your current conversation regardless of which directory it was saved from.
Page updated: November 16, 2025
[Authentication](https://kiro.dev/docs/cli/authentication/)
[Model selection](https://kiro.dev/docs/cli/chat/model-selection/)
On this page
  * [Starting a session](https://kiro.dev/docs/cli/chat/#starting-a-session)
  * [Entering multi-line statements](https://kiro.dev/docs/cli/chat/#entering-multi-line-statements)
  * [Conversation persistence](https://kiro.dev/docs/cli/chat/#conversation-persistence)
  * [Directory-based persistence](https://kiro.dev/docs/cli/chat/#directory-based-persistence)
  * [Manually saving and loading conversations](https://kiro.dev/docs/cli/chat/#manually-saving-and-loading-conversations)