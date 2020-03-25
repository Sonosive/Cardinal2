import discord
import json
from discord.ext import commands

import traceback
from os import listdir
from os.path import isfile, join

from cogs.FactionCommands import FactionCommands
from cogs.Utilities import Utilities
from user import User
from users import Users
from factions import Factions


bot = commands.Bot(command_prefix='c!')
factions = Factions()
users = Users()


@bot.event
async def on_ready():
    game = discord.Game("c!info or c!help")
    await bot.change_presence(
        status=discord.Status.online, activity=game)
    print(f"Logged in as {bot.user.name} - {bot.user.id}\n"
          f"Version: {discord.__version__}")


@bot.event
async def on_member_join(member):
    users = []

    user = User(member.name)
    users.append(user)



# load cogs from cogs directory
cogs_dir = "cogs"

bot.add_cog(FactionCommands(bot, factions))
bot.add_cog(Utilities(bot, users))



#open config for token
with open('config.json') as config_file:
    data = json.load(config_file)
bot.run(data["token"], bot=True)
