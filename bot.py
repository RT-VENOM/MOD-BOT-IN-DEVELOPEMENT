import discord
from discord.ext.commands.bot import Bot
import config
from config import token
from discord import client 
from discord.ext import commands
from discord import utils
client = commands.Bot(command_prefix='?')





@client.event
async def on_ready():
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name='?help'))
    print("bot is online")


@client.event
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
    embed.set_image(url= 'https://media.discordapp.net/attachments/854545082634862622/854932493047955517/download_5_Fotor.jpg')
    await channel.send(embed=embed)
    
@client.command()
async def invite(ctx):
    await ctx.message.add_reaction('✅')
    embed=discord.Embed(
        title="**======== *WANNA ADD ME IN YOUR SERVER!* ========**",
        description=f"""Do you liked using { client.user.mention } and wanna add `MOD BOT` in your server
        


         Then click on **[Invite me!](https://discord.com/api/oauth2/authorize?client_id=853890206570119188&permissions=4294967287&scope=bot)** to add `MOD BOT` in your server.
        """,
        color=0xd89522)
    embed.set_footer(text = "ENJOY USING ME IN YOUR SERVER")
    embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
    embed.set_author(name = "𝕯𝖊𝖆𝖉 ℵᛨℵJᏘ#1412", url='https://www.youtube.com/channel/UCt0g05Q4JTm1a5mxGj7JPQQ', icon_url= 'https://cdn.discordapp.com/attachments/845324641521107004/845391299196747796/3dgifmaker81594_1.gif')
    embed.set_image(url= 'https://media.discordapp.net/attachments/854545082634862622/854931871291670528/download_6_Fotor.jpg')
    await ctx.author.send(embed=embed)
    
@client.event
async def on_command_error(ctx, error):
    pass
    
@client.command()
@commands.has_permissions(ban_members= True )
async def ban(ctx, member: discord.Member, *, reason = None):
    if member == None or member == ctx.message.author:
        await ctx.channel.send("`You cannot ban yourself`")
        return
    if reason == None:
        reason = "no reason applied"
    
    await ctx.message.add_reaction('✅')
    embedfordm=discord.Embed(
        title="**BAN NOTICE**",
        description=f"""{ member.mention } you are banned from { ctx.guild.name } by { ctx.author.mention } due to some unavoidable reasons which were created due to your activity in the server which are breaking the rules of { ctx.guild.name }.""",
        color=0xd89522)
    await member.send(embed = embedfordm)
    await member.ban(reason= reason)
    embed=discord.Embed(
        title="**MODERATION COMMAND**",
        description=f"""{member.mention}  is banned from the server by  { ctx.author.mention }""",
        color=0xd89522)
    embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
    embed.set_author(name = "BAN COMMAND EXECUTED", icon_url= "https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif")
    await ctx.send(embed = embed)
    
    
@ban.error
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
        await ctx.author.send(f'{ ctx.author.mention } you dont have permission to ban anyone in { ctx.guild.name }')    



    
    

client.run(token)
