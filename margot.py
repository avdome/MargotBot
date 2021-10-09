import discord as disc
import os
from dotenv import load_dotenv

# finds the .env file in the current working directory
load_dotenv()

# instance of a client, connects to discord
client = disc.Client()


@client.event
async def on_ready():  # printed in terminal when bot is ready to be used
    print('Hello I am {0.user}.'.format(client))


@client.event
async def on_message(msg):
    # do nothing if bot sends message
    if msg.author == client.user:
        return

    # user messages
    # consider having Margot put a heart after every message
    if msg.content.lower() == 'margot' and msg.author.name != 'KEK':
        await msg.channel.send('Margot loves you too <3')


client.run(os.getenv('TOKEN'))  # environment variable
