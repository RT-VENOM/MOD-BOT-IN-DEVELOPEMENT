import discord
from discord.ext import commands
import discord.utils




class Commands(commands.Cog, name="Commands"):
    """
    **MOD BOT is a moderation bot made by RT_VENOM**
    """
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    
    async def on_guild_join(Guild, ctx):
        general = discord.utils.get(ctx.guild.channels, name="general")
        if not general:
            return


        
        embed = discord.Embed(
            title = f"""MOD BOT""",
            description = f"""thanks for inviting {self.bot.mention} in {ctx.guild.name}
            If you encounter any issues in `MOD BOT` then click on **[Support server!](https://discord.gg/4DSZ4skNgp)** to tell us the problem so that the dev of mod bot can fix it as soon as possible.""", 
            color = 0x00fff3
        )

        embed.set_thumbnail(url = 'https://media.discordapp.net/attachments/841947091659653162/854969004699156480/output-onlinegiftools.gif')
        await ctx.general.send(embed = embed)




def setup(bot):
    bot.add_cog(Commands(bot))
