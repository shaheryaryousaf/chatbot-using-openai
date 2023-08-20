'''
Code Explanation:

1. Import required libraries: discord for Discord API, os for environment variables, and openai for OpenAI GPT-3 API.

2. Initialize an empty string 'chat' to store the chat history and load OpenAI API key and Discord token from environment variables.

3. Define a custom Discord client class with two main methods:
    - on_ready: Called when the bot is ready.
    - on_message: Called when a message is received.

4. In the on_message method:
    - Update the chat history.
    - Check if the message is not from the bot and if the bot is mentioned.
    - Generate a response using OpenAI's GPT-3 and send it.

5. Initialize Discord Intents to enable message content intent.

6. Create an instance of the custom Discord client and run the bot.
'''

import discord
import os
import openai

chat = ''
openai.api_key = os.getenv("OPENAI_API_KEY")
token = os.environ['SECRET_KEY']

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        global chat
        chat += f"{message.author}: {message.content}\n"
        print(f'Message from {message.author}: {message.content}')
        if self.user != message.author:
            if self.user in message.mentions:
                channel = message.channel
                response = openai.Completion.create(
                    model="text-davinci-003",
                    prompt=f"{chat}\nAlpha GPT: ",
                    temperature=1,
                    max_tokens=256,
                    top_p=1,
                    frequency_penalty=0,
                    presence_penalty=0
                )
                messageToSend = response.choices[0].text
                await channel.send(messageToSend)

intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(token)


