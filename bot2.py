import discord
from discord.ext import commands
import random

TOKEN = 'NjgyOTcxMzgzNzg5MTI1NjUz.XnVGbg.DeWGOkFXdGPEEy8apCWAJllrxXA'
bot = commands.Bot(command_prefix='*')


@bot.command(pass_context=False)  # разрешаем передавать агрументы
async def roll(ctx):
    await ctx.send(random.randint(0, 100))

bot.run(TOKEN)
