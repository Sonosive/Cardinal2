
import discord
from discord.ext import commands

import Utilities


class FactionCommands(commands.Cog):
    
    def __init(self, bot, factions):
        self.bot = bot
        self.factions = factions

    @commands.command()
    async def addFaction(self, ctx, factionName, ceo):
        role = discord.utils.get(ctx.guild.roles, name="Cardinal admin")

        if role in ctx.author.roles:

            newFaction = Faction(factionName, ceo)
            self.factions.addFaction(newFaction)

            await ctx.send(f"**{factionName} has been added!**")
        else:
            await ctx.send(f"**Ony Cardinal Admins can add a new faction!**")


def setup(bot):
    bot.add_cog(FactionCommands(bot))

