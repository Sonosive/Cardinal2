
import discord
from discord.ext import commands
from .objects import Faction


class FactionCommands(commands.Cog):

    def __init__(self, bot, factions):
        self.bot = bot
        self.factions = factions


    @commands.command(brief="Add a new faction")
    @commands.has_role("Cardinal admin")
    async def addFaction(self, ctx, factionName, ceo):
        newFaction = Faction(factionName, ceo)
        self.factions.addFaction(newFaction)

        await ctx.send(f"**Faction {factionName} has been added!**")


def setup(bot):
    bot.add_cog(FactionCommands(bot))