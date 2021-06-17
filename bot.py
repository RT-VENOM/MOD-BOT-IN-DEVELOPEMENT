import discord
from discord.ext.commands.bot import Bot
import config
from config import token
from discord import client 
from discord.ext import commands
from discord import utils
Bot = commands.Bot(command_prefix='/')





@Bot.event
async def on_ready():
    print("bot is online")


@Bot.event
async def on_guild_join(guild):
    channel = discord.utils.get(guild.channels, name= 'general',)
    embed=discord.Embed(
        title="**======== *Thanks For Adding Me!* ========**",
        description=f"""Thanks for adding me to {guild.name}! You can use the `/help` command to get started! if you face any issues using """  + client.user.mention + """ you can submit it in our support server so that we can fix it as soon as possible
        


         Click on **[Support Server!](https://discord.gg/EJR9XFyg8f)** to join our support server.
        """,
        color=0xd89522)
    embed.set_footer(text = "ENJOY USING ME IN THIS SERVER")
    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/845324641521107004/845391299196747796/3dgifmaker81594_1.gif')
    embed.set_author(name = "𝕯𝖊𝖆𝖉 ℵᛨℵJᏘ#1412", url='https://www.youtube.com/channel/UCt0g05Q4JTm1a5mxGj7JPQQ', icon_url= 'https://cdn.discordapp.com/attachments/845324641521107004/845391299196747796/3dgifmaker81594_1.gif')
    embed.set_image(url= 'https://discord.com/channels/841947091205881887/841947091659653162/854923489593262090')
    await channel.send(embed=embed)
    
@Bot.command()
async def invite(ctx):
    embed=discord.Embed(
        title="**======== *WANNA ADD ME IN YOUR SERVER!* ========**",
        description=f"""Do you liked using { Bot.user.mention } and wanna add `MOD BOT` in your server
        


         Then click on **[Invite me!](https://discord.com/api/oauth2/authorize?client_id=853890206570119188&permissions=4294967287&scope=bot)** to add `MOD BOT` in your server.
        """,
        color=0xd89522)
    embed.set_footer(text = "ENJOY USING ME IN YOUR SERVER")
    embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/845324641521107004/845391299196747796/3dgifmaker81594_1.gif')
    embed.set_author(name = "𝕯𝖊𝖆𝖉 ℵᛨℵJᏘ#1412", url='https://www.youtube.com/channel/UCt0g05Q4JTm1a5mxGj7JPQQ', icon_url= 'https://cdn.discordapp.com/attachments/845324641521107004/845391299196747796/3dgifmaker81594_1.gif')
    embed.set_image(url= 'https://www.google.com/imgres?imgurl=https%3A%2F%2Fswall.teahub.io%2Fphotos%2Fsmall%2F19-197090_best-gaming-wallpapers-x-pc-and-ipad-desktop.jpg&imgrefurl=https%3A%2F%2Fwww.teahub.io%2Fviewwp%2FiTiwii_pc-game%2F&tbnid=p4IbvkA89fUI9M&vet=12ahUKEwiEvtnd353xAhU_DrcAHT7-BlAQMygBegQIARBC..i&docid=rq65Aop0-XlloM&w=711&h=400&q=thank%20you%20gaming%20image%201024%20*%20500%20px&hl=en-GB&ved=2ahUKEwiEvtnd353xAhU_DrcAHT7-BlAQMygBegQIARBC')
    await ctx.author.send(embed=embed)

Bot.run(token)
