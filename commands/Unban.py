import discord
import asyncio
from discord.ext import commands
from discord import utils





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
    async def unban(self, ctx, id: int):

        await ctx.message.add_reaction('✅')
        
        
        embed = discord.Embed(
            description = f"""**finding  the  user. . .**""",
            color = 0xd89522
        )
        await ctx.send(embed = embed)
        await asyncio.sleep(4)
        user = await self.bot.fetch_user(id)

        embed8 = discord.Embed(
            description = f"""**user found!**""",
            color = 0xd89522
        ) 
        await ctx.send(embed = embed8)
        embed_conf = discord.Embed(
            description = f"""do you really want to unban the user if yes, message yes and if no, message no""",
            color = 0xd89522
        )
        await ctx.send(embed = embed_conf)
        def check(message):
            return ctx.author.id == message.author.id and ctx.channel.id == message.channel.id
        message = await self.bot.wait_for("message", check= check , timeout = 30)
        if "yes" in message.content:
            embed_conf_yes = discord.Embed(
                description = f"""**unban process in continuation...**""",
                color = 0xd89522
            )
            await ctx.send(embed = embed_conf_yes)
            await asyncio.sleep(4)
            embed2 = discord.Embed(
                description = f"""**user is unbanned successfully**""",
                color = 0xff4300
            )
            embed2.set_thumbnail(url='https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
            await ctx.guild.unban(user)
            await ctx.send(embed = embed2)
            embed3 = discord.Embed(
                description = f"""**{ctx.user.mention} you are unbanned from {ctx.guild.name}**""",
                color = 0xd89522
            )
            await ctx.message.user(embed = embed3)


        elif "no" in message.content:
            embed4 = discord.Embed(
                description = f"""**unban command execution was cancelled**""",
                color = 0xff4300
            )
            delete = await ctx.send(embed = embed4)
            await asyncio.sleep(4)
            await ctx.message.delete()
            await delete.delete()
            return

    @unban.error
    async def on_command_error(self, ctx, error):
        if isinstance(ctx.channel, discord.channel.DMChannel):
            await ctx.message.add_reaction('❌')
            embed = discord.Embed(
                title = "**UNBAN COMMAND EXECUTION FAILED**",
                description = f"""**UNBAN COMMAND CANNOT BE USED IN A DM CONVERSATION.
    Executed by { ctx.author.mention }**""",
                color=0xcde242
            )
            embed.set_footer(text= f"The command was used by {ctx.author.mention}")
       
            await ctx.send(embed = embed)
            return
        if isinstance(error, commands.MissingPermissions):
            await ctx.message.add_reaction('❌')    
            embed=discord.Embed(
            title="**MODERATION COMMAND EXECUTION CANCELLED**",
            description=f"""You don't have permission to use the unban command.
    Executed by { ctx.author.mention }""",
            color = 0x7cd700)
            embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
            error = await ctx.send(embed = embed)
            await ctx.author.send(f'{ ctx.author.mention } you dont have permission to unban anyone in { ctx.guild.name }')
            await asyncio.sleep(10)
            await ctx.message.delete()
            await error.delete()
            return








def setup(bot):
    bot.add_cog(Commands(bot))
