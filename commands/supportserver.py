import discord
import asyncio
from discord.ext import commands
from discord import utils
from discord.ext.commands import bot



class Invitation(commands.Cog, name="Invitation"):
    """
    **MOD BOT is a moderation bot made by RT_VENOM**
    """
    def __init__(self, bot):
        self.bot = bot
    @commands.command(aliases = ['ss'], brief = '[Support server invitation]', description = 'Upon the usage of this command `Mod Bot` will dm you with the invitation link of its support server')
    async def supportserver(self, ctx):
        embed=discord.Embed(
            title="**======== *SUPPORT SERVER!* ========**",
            description=f"""Click on **[Support server!](https://discord.gg/4DSZ4skNgp)** to join the official `MOD BOT` support server.

Command executed by {ctx.author.mention}""",
            color= 0xd89522)
        embed.set_footer(text = "ENJOY USING ME IN YOUR SERVER")
        embed.set_thumbnail(url = 'https://cdn.discordapp.com/attachments/845324641521107004/845391299196747796/3dgifmaker81594_1.gif')
        embed.set_author(name = "MOD BOT", url='https://www.youtube.com/channel/UCt0g05Q4JTm1a5mxGj7JPQQ', icon_url= 'https://cdn.discordapp.com/attachments/845324641521107004/845391299196747796/3dgifmaker81594_1.gif')
        await ctx.message.delete()
        await asyncio.sleep(2)
        await ctx.author.send(embed=embed)
        




def setup(bot):
    bot.add_cog(Invitation(bot))

