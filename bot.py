import discord
import json
import traceback
import inspect
import os
from discord.ext import commands
from cogs import UserTools, FactionCommands
from cogs.objects import Factions



bot = commands.Bot(command_prefix='c!')

factions = Factions()

bot.add_cog(UserTools(bot))
bot.add_cog(FactionCommands(bot, factions))


@bot.event
async def on_ready():
    game = discord.Game("c!info or c!help")
    await bot.change_presence(status=discord.Status.online, activity=game)
    print(f"Logged in as {bot.user.name} - {bot.user.id}\n"
          f"Version: {discord.__version__}")



with open('config.json') as config_file:
    data = json.load(config_file)
bot.run(data["token"], bot=True)
