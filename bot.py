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
    embed=discord.Embed(
            title="**======== *THANK YOU!* ========**",
            description=f"""Thanks for adding `MOD BOT` in your server
                
        Click on **[Support server!](https://discord.gg/4DSZ4skNgp)** to join the official `MOD BOT` support server.
                """,
            color= 0xd89522)
        embed.set_footer(text = "ENJOY USING ME IN YOUR SERVER")
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/845324641521107004/845391299196747796/3dgifmaker81594_1.gif')
        embed.set_author(name = "MOD BOT", url='https://www.youtube.com/channel/UCt0g05Q4JTm1a5mxGj7JPQQ', icon_url= 'https://cdn.discordapp.com/attachments/845324641521107004/845391299196747796/3dgifmaker81594_1.gif')
        
        await ctx.author.send(embed=embed)

@client.event
async def on_guild_remove(guild):
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f'{len(client.guilds)} servers | ?help'))




client.run(token)
