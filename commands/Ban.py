import discord
import asyncio
from discord.ext import commands
from discord import utils
from discord.ext.commands import bot
from discord.ext.commands.errors import BadArgument



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
    @commands.cooldown(rate=1, per=30, type=<BucketType.guild: 0>)
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        print("ban command")
        
        if member == ctx.message.author:
            try:
                await ctx.message.add_reaction('❌')
                embed = discord.Embed(
                    title = "**BAN COMMAND EXECUTION FAILED**",
                    description = f"""**BAN COMMAND EXECUTION WAS CANCELLED BECAUSE THE USER YOU MENTIONED IS YOUR ID.\nExecuted by { ctx.author.mention }**""",
                color=discord.Color.red()
                )
                embed.set_footer(text= f"The command was used by {ctx.author.mention}")

                embed_variable = await ctx.send(embed = embed)
                await asyncio.sleep(10)
                await ctx.message.delete()
                await embed_variable.delete()
                return
            except:
                embed = discord.Embed(
                    title = "**BAN COMMAND EXECUTION FAILED**",
                    description = f"""**BAN COMMAND EXECUTION WAS CANCELLED BECAUSE THE USER YOU MENTIONED IS YOUR ID.\nExecuted by { ctx.author.mention }**""",
                color=discord.Color.red()
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
            print("bot ban")
            embed20072007 = discord.Embed(
                title = "**BAN COMMAND EXECUTION FAILED**",
                description = f"""**BAN COMMAND WAS CANCELLED BECAUSE THE MEMBER YOU MENTION IS A BOT.\nExecuted by { ctx.author.mention }**""",
                color= discord.Color.red()
                )
            embed20072007.set_footer(text= f"The command was used by {ctx.author.mention}")
            embed_variabl = await ctx.send(embed = embed20072007)
            await asyncio.sleep(10)
            await ctx.message.delete()
            await embed_variabl.delete()
            return
        
        
        if ctx.author.top_role.position < member.top_role.position:
            dgh4 = discord.Embed(
                description = f"""The user you menitoned has a higher role than you\n**Executed by** {ctx.author.mention}\n Tried to ban: {member.mention}""",
                color = discord.Color.green()
            )
            await ctx.send(embed = dgh4, delete_after = 5)
            return
        if ctx.me.top_role.position < member.top_role.position:
            dgh3 = discord.Embed(
                description = f"""The user you menitoned has a higher role than me\n**Executed by** {ctx.author.mention}""",
                color = discord.Color.green()
            )
            await ctx.send(embed = dgh3, delete_after = 5)
            return
 
        if ctx.me.top_role.position == member.top_role.position:
            dgh2 = discord.Embed(
                description = f"""The user you menitoned has the same role or same position as me.\nNote to fix this: MOD BOTs role or any other role given to MOD BOT must be in higher position than the top role of the member you want to ban\n**Executed by** {ctx.author.mention}\nTried to ban: {member.mention}""",
                color = discord.Color.green()
            )
            await ctx.send(embed = dgh2, delete_after = 30)
            return
        elif ctx.author.top_role.position == member.top_role.position:
            dgh5 = discord.Embed(
                description = f"""The member you mentioned has the same role or position as yours\nReason of cancellation: Your top role and the top role of the member you want to ban is the same\n**Executed by** {ctx.author.mention}\n**Tried to ban:** {member.mention}""",
                color = discord.Color.green()
            )
            await ctx.send(embed = dgh5, delete_after = 30)
            return
        
           
        try:
            print("ban try")
            await ctx.message.add_reaction('✅')
            embedfordm=discord.Embed(
                title="**BAN NOTICE**",
                description=f"""{ member.mention } you are banned from { ctx.guild.name } by { ctx.author.mention } due to some unavoidable reasons which were created due to your activity in the server which are breaking the rules of { ctx.guild.name }.""",
                color=0xd89522)
            await member.send(embed = embedfordm)
            await member.ban(reason= reason)
            embed=discord.Embed(
                title="**MODERATION COMMAND**",
                description=f"""{member.mention}  is banned from the server by  { ctx.author.mention }\n**Reason : {reason}**\n**Executed by: {ctx.author.mention}**\nBanned user: {member.mention}""",
                color= discord.Color.green())
            embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
            embed.set_author(name = "BAN COMMAND EXECUTED", icon_url= "https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif")
            await ctx.send(embed = embed)
        except:
            print("ban except")
            embedfordm=discord.Embed(
                title="**BAN NOTICE**",
                description=f"""{ member.mention } you are banned from { ctx.guild.name } by { ctx.author.mention } due to some unavoidable reasons which were created due to your activity in the server which are breaking the rules of { ctx.guild.name }.""",
                color=0xd89522)
            await member.send(embed = embedfordm)
            await member.ban(reason= reason)
            embed=discord.Embed(
                title="**MODERATION COMMAND**",
                description=f"""{member.mention}  is banned from the server by  { ctx.author.mention }\n**Reason : {reason}**\n**Executed by: {ctx.author.mention}**\n**Banned user: {member.mention}**""",
                color= discord.Color.green())
            embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
            embed.set_author(name = "BAN COMMAND EXECUTED", icon_url= "https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif")
            await ctx.send(embed = embed)
    
    
    @ban.error
    async def on_command_error(self, ctx, error):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            try:
                await ctx.message.add_reaction('❌')
                embed = discord.Embed(
                    title = "**BAN COMMAND EXECUTION FAILED**",
                    description = f"""**BAN COMMAND CANNOT BE USED IN A DM CONVERSATION.\nExecuted by { ctx.author.mention }**""",
                    color=0xd89522
                )
                embed.set_footer(text= f"The command was used by {ctx.author.mention}")
        
                await ctx.send(embed = embed)
                return
            except:
                embed = discord.Embed(
                    title = "**BAN COMMAND EXECUTION FAILED**",
                    description = f"""**BAN COMMAND CANNOT BE USED IN A DM CONVERSATION.\nExecuted by { ctx.author.mention }**""",
                    color=0xd89522
                )
                embed.set_footer(text= f"The command was used by {ctx.author.mention}")
        
                await ctx.send(embed = embed)
                return
        elif isinstance(error, commands.MissingPermissions):
            try:
                await ctx.message.add_reaction('❌')    
                embed=discord.Embed(
                title="**MODERATION COMMAND EXECUTION CANCELLED**",
                description=f"""You don't have permission to use the ban command.\nExecuted by { ctx.author.mention }""",
                color=discord.Color.red())
                embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
                error = await ctx.send(embed = embed)
                await ctx.author.send(f'{ ctx.author.mention } you dont have permission to ban anyone in { ctx.guild.name }')
                await asyncio.sleep(10)
                await ctx.message.delete()
                await error.delete()
                return
            except:
                embed4353534=discord.Embed(
                title="**MODERATION COMMAND EXECUTION CANCELLED**",
                description=f"""You don't have permission to use the ban command.\nExecuted by { ctx.author.mention }""",
                color=discord.Color.red())
                embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
                error = await ctx.send(embed = embed4353534)
                await ctx.author.send(f'{ ctx.author.mention } you dont have permission to ban anyone in { ctx.guild.name }')
                await asyncio.sleep(10)
                await ctx.message.delete()
                await error.delete()
                return
        elif isinstance(error, commands.MissingRequiredArgument):
            try:
                await ctx.message.add_reaction('❌')
                embed9=discord.Embed(
                description=f"""You must mention a user to ban.\n**Executed by **{ ctx.author.mention }""",
                color=discord.Color.red())
                error9 = await ctx.send(embed = embed9)
                await asyncio.sleep(10)
                await ctx.message.delete()
                await error9.delete()
                return
            except:
                embed9=discord.Embed(
                description=f"""You must mention a user to ban.\n**Executed by **{ ctx.author.mention }""",
                color=discord.Color.red())
                error9 = await ctx.send(embed = embed9)
                await asyncio.sleep(10)
                await ctx.message.delete()
                await error9.delete()
                return
        elif isinstance(error, BadArgument):
            try:
                await ctx.message.add_reaction('❌')
                embed999=discord.Embed(
                description=f"""You need to mention someone to ban.\n**Executed by **{ ctx.author.mention }""",
                color= discord.Color.red())
                error999 = await ctx.send(embed = embed999)
                await asyncio.sleep(10)
                await ctx.message.delete()
                await error999.delete()
                return
            except:
                embed9999=discord.Embed(
                description=f"""You need to mention someone to ban.\n**Executed by **{ ctx.author.mention }""",
                color= discord.Color.red())
                error9999 = await ctx.send(embed = embed9999)
                await asyncio.sleep(10)
                await ctx.message.delete()
                await error9999.delete()
                return
        
        elif isinstance(error, commands.CommandOnCooldown):
            await ctx.send(f"This command is on cooldown, try again after {round(error.retry_after)} seconds.", delete_after=5)
            print(error)
            return

def setup(bot):
    bot.add_cog(Commands(bot))
