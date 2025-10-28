# Irrigation Educator Agent

The **Irrigation Educator Agent** is a terminal-based AI assistant designed to support irrigation education and decision-making in Nebraska and beyond. It provides plain-language explanations, practical recommendations, and guided support for students, educators, and agricultural producers.

## Features

- Conversational AI agent powered by OpenAI
- Tailors responses based on user type (e.g., student, farmer)
- Pulls information from primary and secondary irrigation documents
- Provides example calculations and explains irrigation management concepts
- Supports file search and web search tools

## Getting Started

For installation instructions, please see the guide for your operating system:

- [Windows Setup Guide](./docs/setup_windows.md)
- [macOS & Linux Setup Guide](./docs/setup_macos_linux.md)

## Running the Educator Agent

For an interactive chat experience, see the [Educator Agent Instructions](./docs/educator_agent.md).

## Translating Captions

For translating .vtt caption files to other languages, see the [Translate Captions Instructions](./docs/translate_captions.md).

## Configuration

For configuration instructions, see the [Configuration Guide](./docs/config.md).

## Notes

- This agent uses the OpenAI Agents API and requires an API key.
- **Markdown formatting** is supported in responses.  
- This project is a test for the openai agent sdk, not a real product. This is also why we have other features like the translator script included that use the already made architecture  
- The real benefit of this agent is the file database that has high quality information  
- I tried to make the docs as user friendly as possible for non-techinal people

## Links

[SDK Documentation](https://openai.github.io/openai-agents-python/)  
[SDK Github](https://github.com/openai/openai-agents-python)
