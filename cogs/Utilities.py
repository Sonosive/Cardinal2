import discord
from discord.ext import commands

from user import User


class Utilities(commands.Cog):

    def __init(self, bot, users):
        self.bot = bot
        self.users = users

    @commands.command(brief="Pong!")
    async def ping(self, ctx):
        await ctx.send(f"Pong! **{round(self.bot.latency * 1000)}**ms")

    @commands.command(brief="More information")
    async def info(self, ctx):
        await ctx.send(f"**This is Cardinal, helper bot for the Space Factions Server!\n"
                       f"Cardinal was originally made to facilitate an economic system"
                       f"between factions, but has since then been repurposed to be an"
                       f"all around utility bot for you to use! More to come soon**")

    @commands.command(brief="Database all users. Slow!")
    async def initializeAllUsers(self, ctx):

        role = discord.utils.get(ctx.guild.roles, name="Cardinal admin")

        if role in ctx.author.roles:

            for member in ctx.guild.members:
                user = User(member.name)
                self.users.addUser(user)

            await ctx.send("**All users have been databased**")
        else:
            await ctx.send("**Only Cardinal Admins can run this command!**")


def setup(bot):
    bot.add_cog(Utilities(bot))
