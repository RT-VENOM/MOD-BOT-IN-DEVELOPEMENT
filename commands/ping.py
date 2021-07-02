import discord
from discord.ext import commands
import asyncio



class Commands(commands.Cog, name="Commands"):
    """
    **MOD BOT is a moderation bot made by RT_VENOM**
    """
    def __init__(self, bot):
        self.bot = bot
    @commands.command()
    async def ping(self, ctx):
        embed = discord.Embed(
            description = f""":ping_pong: **Pong! {round(self.bot.latency * 1000)}ms** \n{ctx.author.mention}""",
            color = 0x3c1361
        )
        await ctx.send(embed = embed)
        await ctx.message.delete()




def setup(bot):
    bot.add_cog(Commands(bot))
