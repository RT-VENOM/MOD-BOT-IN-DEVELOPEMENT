from asyncio import exceptions
from logging import exception
import discord
import asyncio
from discord import message
from discord.ext import commands
from discord import utils
from discord.ext.commands.errors import BadArgument
from discord.ext.commands.cooldowns import BucketType





class Commands(commands.Cog, name="Commands"):
    """
    **MOD BOT is a moderation bot made by RT_VENOM**
    """
    def __init__(self, bot):
        self.bot = bot
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        pass



    @commands.command(aliases = ['unb'], brief = "[Used to unban a member]")
    @commands.has_permissions(ban_members= True)
    @commands.cooldown(rate=1, per=60, commands.BucketType.guild)
    async def unban(self, ctx, id: int):
        try:
            await ctx.message.add_reaction('✅')
            
            
            embed = discord.Embed(
                description = f"""**finding  the  user. . .**""",
                color = 0xd89522
            )
            finding = await ctx.send(embed = embed)
            await asyncio.sleep(4)
            try:
                user = await self.bot.fetch_user(id)
            except:
                embed93 = discord.Embed(
                    description = f"""User not found\n**Executed by **{ctx.author.mention}""",
                    color = discord.Color.red()
                )
                usernotfound=await ctx.send(embed = embed93)
                await ctx.message.clear_reactions()
                await ctx.message.add_reaction('❌')
                await asyncio.sleep(10)
                await usernotfound.delete()
                await finding.delete()
                await ctx.message.delete()
                return
            embed8 = discord.Embed(
                description = f"""**user found!**""",
                color = 0xd89522
            ) 
            userfound= await ctx.send(embed = embed8)
            embed_conf = discord.Embed(
                description = f"""Confirm by messaging yes or no.\nNote: Responce will be taken only from {ctx.author.mention} in between 10 sec""",
                color = 0xd89522
            )
            yesorno = await ctx.send(embed = embed_conf)
            
        
            def check(message):
                return ctx.author.id == message.author.id and ctx.channel.id == message.channel.id
            
            ml = await self.bot.wait_for("message", check= check , timeout = 10)
            if "yes" in ml.content:
                embed_conf_yes = discord.Embed(
                    description = f"""**unban process in continuation...**""",
                    color = 0xd89522
                )
                await ctx.send(embed = embed_conf_yes)
                await asyncio.sleep(4)
                embed2 = discord.Embed(
                    description = f"""**user is unbanned successfully**\nExecuted by: {ctx.author.mention} """,
                    color = discord.Color.green()
                )
                embed2.set_thumbnail(url='https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
                await ctx.guild.unban(user)
                await ctx.send(embed = embed2)
                embed3 = discord.Embed(
                    description = f"""**{ctx.user.mention} you are unbanned from {ctx.guild.name}**""",
                    color = 0xd89522
                )
                await ctx.message.user(embed = embed3)
                return
            elif "no" in ml.content:
                embed4 = discord.Embed(
                    description = f"""**unban command execution was cancelled**""",
                    color = discord.Color.green()
                )
                delete = await ctx.send(embed = embed4)
                await asyncio.sleep(4)
                await ctx.message.delete()
                await delete.delete()
                await userfound.delete()
                await finding.delete()
                await yesorno.delete()
                await ml.delete()
                return
        except asyncio.exceptions.TimeoutError:
            embed = discord.Embed(
                description = f"""{ctx.author.mention} your unban command was cancelled due to the timeout of 10 sec.\n**Executed by {ctx.author.mention}""",
                color = discord.Color.green()
            )
            await ctx.message.clear_reactions()
            await ctx.message.add_reaction('❌')
            timeoutio = await ctx.send(embed = embed)
            await asyncio.sleep(10)
            await timeoutio.delete()
            await yesorno.delete() 
            await finding.delete()
            await userfound.delete()
            await asyncio.sleep(3)
            await ctx.message.delete()
            return
        

        


    @unban.error
    async def on_command_error(self, ctx, error):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            try:
                await ctx.message.add_reaction('❌')
                embed = discord.Embed(
                    title = "**UNBAN COMMAND EXECUTION FAILED**",
                    description = f"""**UNBAN COMMAND CANNOT BE USED IN A DM CONVERSATION.\nExecuted by { ctx.author.mention }**""",
                    color=0xcde242
                )
                embed.set_footer(text= f"The command was used by {ctx.author.mention}")
        
                await ctx.send(embed = embed)
                return
            except:
                embed = discord.Embed(
                    title = "**UNBAN COMMAND EXECUTION FAILED**",
                    description = f"""**UNBAN COMMAND CANNOT BE USED IN A DM CONVERSATION.\nExecuted by { ctx.author.mention }**""",
                    color=0xcde242
                )
                embed.set_footer(text= f"The command was used by {ctx.author.mention}")
        
                await ctx.send(embed = embed)
                return
        elif isinstance(error, commands.MissingPermissions):
            try:
                await ctx.message.add_reaction('❌')    
                embed=discord.Embed(
                title="**MODERATION COMMAND EXECUTION CANCELLED**",
                description=f"""You don't have permission to use the unban command.0\nExecuted by { ctx.author.mention }""",
                color = 0x7cd700)
                embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
                error = await ctx.send(embed = embed)
                await ctx.author.send(f'{ ctx.author.mention } you dont have permission to unban anyone in { ctx.guild.name }')
                await asyncio.sleep(10)
                await ctx.message.delete()
                await error.delete()
                return
            except:
                embed=discord.Embed(
                title="**MODERATION COMMAND EXECUTION CANCELLED**",
                description=f"""You don't have permission to use the unban command.0\nExecuted by { ctx.author.mention }""",
                color = 0x7cd700)
                embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
                error = await ctx.send(embed = embed)
                await ctx.author.send(f'{ ctx.author.mention } you dont have permission to unban anyone in { ctx.guild.name }')
                await asyncio.sleep(10)
                await ctx.message.delete()
                await error.delete()
                return
        elif isinstance(error, commands.MissingRequiredArgument):
            try:
                await ctx.message.add_reaction('❌')
                embed9=discord.Embed(
                description=f"""You must send a users id to unban.\n**Executed by **{ ctx.author.mention }""",
                color= discord.Color.red())
                error9 = await ctx.send(embed = embed9)
                await asyncio.sleep(10)
                await ctx.message.delete()
                await error9.delete()
                return
            except:
                embed9=discord.Embed(
                description=f"""You must send a users id to unban.\n**Executed by **{ ctx.author.mention }""",
                color= discord.Color.red())
                error9 = await ctx.send(embed = embed9)
                await asyncio.sleep(10)
                await ctx.message.delete()
                await error9.delete()
                return

        elif isinstance(error, BadArgument):
            try:
                await ctx.message.add_reaction('❌')
                embed999=discord.Embed(
                description=f"""ID should always be in a integer format.\n**Executed by **{ ctx.author.mention }""",
                color= discord.Color.red())
                error999 = await ctx.send(embed = embed999)
                await asyncio.sleep(10)
                await ctx.message.delete()
                await error999.delete()
                return
            except:
                embed9999=discord.Embed(
                description=f"""ID should always be in a integer format.\n**Executed by **{ ctx.author.mention }""",
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


