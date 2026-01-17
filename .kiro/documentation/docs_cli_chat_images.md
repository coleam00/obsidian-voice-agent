# Working with images
Kiro can analyze and discuss images directly in your chat session. You can share images with Kiro by dragging and dropping them into your terminal window or by using the `read` tool with the Image mode.
## Drag and drop images[](https://kiro.dev/docs/cli/chat/images/#drag-and-drop-images)
The simplest way to share images with Kiro is to drag and drop them directly into your terminal window. When you drag an image into the terminal:
  1. The image path is automatically inserted into your prompt
  2. You can then add text to provide context about what you want Kiro to do with the image
  3. Kiro will process the image and respond based on its content


Example:
```

Kiro> /path/to/architecture-diagram.png Can you explain this architecture and generate sample code for implementing it?


```

## Using fs_read with images[](https://kiro.dev/docs/cli/chat/images/#using-fs_read-with-images)
You can also explicitly use the `read` tool to share images:
```

Kiro> Can you analyze this screenshot at /path/to/screenshot.png?


```

Kiro will automatically suggest using fs_read with Image mode when you mention image files.
## Image use cases[](https://kiro.dev/docs/cli/chat/images/#image-use-cases)
Common use cases for sharing images with Kiro include:
  * Analyzing screenshots of error messages for troubleshooting
  * Converting architecture diagrams into code implementations
  * Discussing UI/UX designs and generating corresponding HTML/CSS
  * Understanding flowcharts and translating them into algorithms
  * Reviewing code snippets shared as images
  * Interpreting technical diagrams for documentation


## Supported formats and limitations[](https://kiro.dev/docs/cli/chat/images/#supported-formats-and-limitations)
Supported image formats include JPEG/JPG, PNG, GIF, and WebP. Images must be under 10MB in size, and you can share up to 10 images in a single request.
For best results:
  * Use high-resolution images with clear text
  * Provide specific instructions about what you want Kiro to do with the image
  * For complex diagrams, consider providing additional context


Page updated: November 25, 2025
[Working with Git](https://kiro.dev/docs/cli/chat/git-aware-selection/)
[Security considerations](https://kiro.dev/docs/cli/chat/security/)
On this page
  * [Drag and drop images](https://kiro.dev/docs/cli/chat/images/#drag-and-drop-images)
  * [Using fs_read with images](https://kiro.dev/docs/cli/chat/images/#using-fs_read-with-images)
  * [Image use cases](https://kiro.dev/docs/cli/chat/images/#image-use-cases)
  * [Supported formats and limitations](https://kiro.dev/docs/cli/chat/images/#supported-formats-and-limitations)