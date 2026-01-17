# Product Overview

## Product Purpose
Obsidian Voice Agent is a local web application that provides conversational access to an Obsidian knowledge base through both voice and text interfaces. It enables natural language querying, searching, and summarization of Markdown documents stored in Obsidian vaults.

## Target Users
- **Primary**: Knowledge workers and developers who use Obsidian for personal knowledge management
- **Needs**: Quick retrieval of information from large note collections without manual searching, hands-free access while multitasking

## Key Features
- **Voice Interface**: Real-time voice conversations via LiveKit voice agent
- **Text Interface**: Chat-based queries via Pydantic AI agent (also enables automated testing)
- **Unified Tool System**: Shared search tools between voice and text agents
- **Knowledge Base Search**: Fast navigation through Obsidian Markdown documents
- **Document Summarization**: AI-powered summaries of retrieved content

## Current Scope
- **Read-only operations only** - No write/edit/delete capabilities
- Tools limited to: search, read, summarize
- No MCP servers, hooks, or custom agents (keeping it simple)

## Business Objectives
- Reduce time spent manually searching through notes
- Enable hands-free knowledge retrieval
- Provide testable agent architecture for reliable development

## User Journey
1. User opens local web app in browser
2. Chooses voice or text input mode
3. Asks a question about their knowledge base
4. Agent searches Obsidian vault using shared tools
5. Agent returns relevant documents and summaries
6. User continues conversation or asks follow-up questions

## Success Criteria
- Sub-second search response times
- Accurate document retrieval for natural language queries
- Seamless switching between voice and text modes
- All agent tools testable via text interface with Agent Browser
