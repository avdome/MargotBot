from typing_extensions import TypeVarTuple
import discord as disc
import os
from Roller import *

# from dotenv import load_dotenv

# finds the .env file in the current working directory
# load_dotenv()

# instance of a client, connects to discord
client = disc.Client()


#TODO "do a little trolling" sound command.

@client.event
async def on_ready():  # printed in terminal when bot is ready to be used
    print('Hello I am {0.user}.'.format(client))


@client.event
async def on_message(msg):  # refactor code for commands

    enable_jenzel_bad_take = False

    # do nothing if bot sends message
    if msg.author == client.user:
        return

    if msg.author.name == "𝒸𝒽𝓊𝓇𝒸𝒽𝑔𝑜𝑒𝓇➀" and enable_jenzel_bad_take:
        await msg.channel.send('https://media.discordapp.net/attachments/'
                               '533513796556161046/873834654271152188/'
                               'TheBadTakeMachine.gif')

    # roll command
    rollnumber = rollcheck(msg.content.lower())
    if rollnumber > 0:
        await msg.channel.send(roll(rollnumber))

    # consider having Margot put a heart after every message
    match msg.content.lower():
        case "help":
            await msg.channel.send(mhelp())
        case "margot":
            match msg.author.name:
                case "alexma22":
                    await msg.channel.send('Margot doesnt love you :(')
                case "KEK":
                    await msg.channel.send('Margot loves you more than everyone else <3')
                case "𝒸𝒽𝓊𝓇𝒸𝒽𝑔𝑜𝑒𝓇➀":
                    # avoid double message for now.
                    # await msg.channel.send('Margot thinks your cringe')
                    a = 'b'  # what is this line?
                    # required to avoid error.
                case _:
                    await msg.channel.send('Margot loves you too <3')
        case "mashallah":
            await msg.channel.send('لا إله إلا الله محمد رسول الله')
        case "enable jenzel bad take":
            enable_jenzel_bad_take = True
            await msg.channel.send('Jenzel bad takes enabled!')
        case "disable jenzel bad take":
            enable_jenzel_bad_take = False
            await msg.channel.send('Jenzel bad takes disabled!')

client.run(os.environ['TOKEN'])  # env var from Heroku server
# client.run(os.getenv('TOKEN'))  # env var from local .env
