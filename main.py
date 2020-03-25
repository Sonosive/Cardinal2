import discord
import json
from discord.ext import commands


bot = commands.Bot(command_prefix='c!')


@bot.event
async def on_ready():
    game = discord.Game("c!info or c!help")
    await bot.change_presence(
        status=discord.Status.online, activity=game)
    print(f"Logged in as {bot.user.name} - {bot.user.id}\n"
          f"Version: {discord.__version__}")


with open('config.json') as config_file:
    data = json.load(config_file)
bot.run(data["token"], bot=True)
