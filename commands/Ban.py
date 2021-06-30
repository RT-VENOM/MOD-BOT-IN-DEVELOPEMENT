import discord
import asyncio
from discord.ext import commands
from discord import utils
from discord.ext.commands import bot



class Commands(commands.Cog, name="Commands"):
    """
    **MOD BOT is a moderation bot made by RT_VENOM**
    """
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        pass
    
    @commands.command(aliases = ['b'], brief = '[Used to ban a member]', description = 'This command can be only executed when the bots role is above than the role of the members you want to ban, this bot cannot ban any bot as well as cannot ban any administrator, this bot requires send, add reaction, embed, attachment permission etc. When the command will be successful executed it will send a message in the channel where the command was executed but if the command is inappropriate like trying to ban a bot it will send a message telling you that you cannot ban a bot and it will delete both the command and the error message given by bot after 10 seconds of the execution of command.')
    @commands.has_permissions(ban_members= True )
    async def ban(self, ctx, member: discord.Member, *, reason = None):
    
        if member == None or member == ctx.message.author:
            await ctx.message.add_reaction('❌')
            embed = discord.Embed(
                title = "**BAN COMMAND EXECUTION FAILED**",
                description = f"""**BAN COMMAND EXECUTION WAS CANCELLED BECAUSE THE USER YOU MENTIONED IS EITHER A USER WHO IS NOT A MEMBER OF THIS SERVER OR THIS IS YOUR ID.
    Executed by { ctx.author.mention }**""",
            color=0xff0000
            )
            embed.set_footer(text= f"The command was used by {ctx.author.mention}")
       
            embed_variable = await ctx.send(embed = embed)
            await asyncio.sleep(10)
            await ctx.message.delete()
            await embed_variable.delete()
            return
        if reason == None:
            reason = "no reason applied"
        if member.bot:
            await ctx.message.add_reaction('❌')
            embed = discord.Embed(
                title = "**BAN COMMAND EXECUTION FAILED**",
                description = f"""**BAN COMMAND WAS CANCELLED BECAUSE THE MEMBER YOU MENTION IS A BOT.
    Executed by { ctx.author.mention }**""",
                color=0xff0000
            )
            embed.set_footer(text= f"The command was used by {ctx.author.mention}")

            embed_variabl = await ctx.send(embed = embed)
            await asyncio.sleep(10)
            await ctx.message.delete()
            await embed_variabl.delete()
            return
    
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
            color=ctx.author.color)
        embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
        embed.set_author(name = "BAN COMMAND EXECUTED", icon_url= "https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif")
        await ctx.send(embed = embed)
    
    
    @ban.error
    async def on_command_error(self, ctx, error):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.message.add_reaction('❌')
            embed = discord.Embed(
                title = "**BAN COMMAND EXECUTION FAILED**",
                description = f"""**BAN COMMAND CANNOT BE USED IN A DM CONVERSATION.
    Executed by { ctx.author.mention }**""",
                color=0xd89522
            )
            embed.set_footer(text= f"The command was used by {ctx.author.mention}")
       
            await ctx.send(embed = embed)
            return
        if isinstance(member, discord.Member):
            if member.top_role >= ctx.author.top_role:
                role = await ctx.send("`You cannot ban a member with higher role or permissions than you.`")
                await ctx.message.delete()
                await asyncio.sleep(4)
                await role.delete()
                return
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.add_reaction('❌')    
            embed=discord.Embed(
            title="**MODERATION COMMAND EXECUTION CANCELLED**",
            description=f"""You don't have permission to use the ban command.
    Executed by { ctx.author.mention }""",
            color=ctx.author.color)
            embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
            error = await ctx.send(embed = embed)
            await ctx.author.send(f'{ ctx.author.mention } you dont have permission to ban anyone in { ctx.guild.name }')
            await asyncio.sleep(10)
            await ctx.message.delete()
            await error.delete()
            return


def setup(bot):
    bot.add_cog(Commands(bot))
