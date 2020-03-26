import discord
from discord.ext import commands


class UserTools(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    
    @commands.command(brief="Pong!")
    async def ping(self, ctx):
        await ctx.send(f"Pong! **{round(self.bot.latency * 1000)}**ms")


    @commands.command(brief="More information")
    async def info(self, ctx):
        await ctx.send(f"**This is Cardinal, helper bot for the Space Factions Server!\n"
                       f"Cardinal was originally made to facilitate an economic system"
                       f"between factions, but has since then been repurposed to be an"
                       f"all around utility bot for you to use! More to come soon**")


    @commands.command(hidden=True)
    @commands.is_owner()
    async def shutdown(self, ctx):
        '''Shut down the bot'''
        await ctx.send("**Shutting down....**")
        await self.bot.logout()


def setup(bot):
    bot.add_cog(UserTools(bot))