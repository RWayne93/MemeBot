import os 
from discord.ext import commands

bot = commands.Bot(command_prefix="!")

for filename in os.listdir("./cogs"):
    if filename.endswith(".py") and filename != "__init__.py":
        bot.load_extension(f'cogs.{filename[:-3]}')

bot.run("NzkxMTU4MTExNzA4MzgxMjA0.X-LFaA.AFXP0fZ_wzc0vJ0RfbovA-CEDA0")