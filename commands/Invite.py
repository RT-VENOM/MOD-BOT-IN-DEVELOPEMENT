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

    @commands.command(aliases = ['inv'], brief = '[Bot invite command]', description = 'This command is used to invite the bot in your server')
    async def invite(self, ctx):
        await ctx.message.add_reaction('✅')
        embed=discord.Embed(
            title="**======== *WANNA ADD ME IN YOUR SERVER!* ========**",
            description=f"""Do you liked using { self.bot.user.mention } and wanna add `MOD BOT` in your server
                
        Then click on **[Invite me!](https://discord.com/api/oauth2/authorize?client_id=831208296018083890&permissions=8&scope=bot)** to add `MOD BOT` in your server.
                """,
            color= 0xd89522)
        embed.set_footer(text = "ENJOY USING ME IN YOUR SERVER")
        embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
        embed.set_author(name = "MOD BOT", url='https://www.youtube.com/channel/UCt0g05Q4JTm1a5mxGj7JPQQ', icon_url= 'https://cdn.discordapp.com/attachments/845324641521107004/845391299196747796/3dgifmaker81594_1.gif')
        embed.set_image(url= 'https://media.discordapp.net/attachments/854545082634862622/854931871291670528/download_6_Fotor.jpg')
        await ctx.author.send(embed=embed)
        await asyncio.sleep(5)
        await ctx.message.delete()
    


# your code here

def setup(bot):
    bot.add_cog(Invitation(bot))
