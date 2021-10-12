import discord as disc
import os
# from dotenv import load_dotenv

# finds the .env file in the current working directory
# load_dotenv()

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
    if msg.content.lower() == 'margot':
        match msg.author.name:
            case "alexma22":
                await msg.channel.send('Margot doesnt love you :(')
            case "KEK":
                await msg.channel.send('Margot loves you more than everyone else <3')
            case "𝒸𝒽𝓊𝓇𝒸𝒽𝑔𝑜𝑒𝓇➀":
                await msg.channel.send('Margot thinks your cringe')
            case _:
                await msg.channel.send('Margot loves you too <3')


client.run(os.environ['TOKEN'])  # env var from Heroku server
# client.run(os.getenv('TOKEN'))  # env var from local .env 