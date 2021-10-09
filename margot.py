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
    if msg.content == 'margot':   
        await msg.channel.send('Margot loves you too <3')
    #else:
#       await msg.channel.send('I am sorry I only speak Australian, I do not understand you. Margot still loves you <3')

# print(os.getenv('TOKEN'))

# client.run('ODk2MjEyMzE0NTM2MTQ4OTkz.YWD0wg.1hTt5RHi8-qmXRquBeF196rhuHU')
client.run(os.getenv('TOKEN'))  # environment vairable
