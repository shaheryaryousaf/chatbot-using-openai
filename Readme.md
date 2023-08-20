# Discord Bot with OpenAI GPT-3 Integration

## Overview
This Discord bot is integrated with OpenAI's GPT-3 API to generate conversational responses. The bot listens for mentions and responds to messages where it is mentioned.

## Code Explanation
1. **Import required libraries**: `discord` for Discord API, `os` for environment variables, and `openai` for OpenAI GPT-3 API.
2. **Initialize Variables**: An empty string 'chat' is initialized to store the chat history. OpenAI API key and Discord token are loaded from environment variables.
3. **Custom Discord Client**: A custom Discord client class is defined with two main methods:
    - `on_ready`: Called when the bot is ready.
    - `on_message`: Called when a message is received.
4. **Message Handling**: In the `on_message` method, the chat history is updated, and a check is performed to see if the message is not from the bot and if the bot is mentioned.
5. **GPT-3 Response**: A response is generated using OpenAI's GPT-3 and sent back in the Discord chat.
6. **Initialize Discord Intents**: Discord Intents are initialized to enable message content intent.

## Requirements
- Python 3.x
- `discord.py` library
- `openai` library
- OpenAI API key
- Discord Bot Token

## Testing Environment
This code has been tested on repl.com as of the latest update.

## Contributing
Feel free to fork this repository and submit pull requests. For major changes, please open an issue first to discuss the change.

## License
This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.
