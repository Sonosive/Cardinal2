import discord
import json
from discord.ext import commands

import traceback
from os import listdir
from os.path import isfile, join


bot = commands.Bot(command_prefix='c!')


@bot.event
async def on_ready():
    game = discord.Game("c!info or c!help")
    await bot.change_presence(
        status=discord.Status.online, activity=game)
    print(f"Logged in as {bot.user.name} - {bot.user.id}\n"
          f"Version: {discord.__version__}")

cogs_dir = "cogs"

for extension in [f.replace('.py', '') for f in listdir(cogs_dir) if isfile(join(cogs_dir, f))]:
    try:
        bot.load_extension(cogs_dir + "." + extension)
    except (discord.ClientException, ModuleNotFoundError):
        print(f'Failed to load extension {extension}.')
        traceback.print_exc()


with open('config.json') as config_file:
    data = json.load(config_file)
bot.run(data["token"], bot=True)
