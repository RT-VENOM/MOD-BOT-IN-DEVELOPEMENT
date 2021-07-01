import discord
from discord import client
from discord.ext import commands
import config 
from config import token
import asyncio
import os

client = commands.Bot(command_prefix= '?')


if __name__ == "__main__":
    for file in os.listdir("./commands"):
        if file.endswith(".py"):
            extension = file[:-3]
            try:
                client.load_extension(f"commands.{extension}")
                print(f"Loaded extension '{extension}'")
            except Exception as e:
                exception = f"{type(e).__name__}: {e}"
                print(f"Failed to load extension {extension}\n{exception}")







@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{len(client.guilds)} servers | ?help'))
    print("bot is online")



@client.event
async def on_guild_join(guild):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{len(client.guilds)} servers | ?help'))
@client.event
async def on_guild_remove(guild):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{len(client.guilds)} servers | ?help'))

@client.event
async def on_message(message):
    if client.user.mentioned_in(message):

        embed=discord.Embed(title=f"""Hello! my prefix is `?`""",
        color = 0x80c904)
   
        var2 = await message.channel.send(embed=embed)

        await client.process_commands(message)



client.run(token)
