import discord
from discord.ext import commands
import random

TOKEN = 'NjgyOTcxMzgzNzg5MTI1NjUz.XnVuRw.UarejcVg6hwSdE-RgO9nDpAXCUs'
bot = commands.Bot(command_prefix='*')


@bot.command(pass_context=True)  # разрешаем передавать агрументы
async def roll(ctx, *args):
    boards = list(map(int, args))
    await ctx.send(random.randint(boards[0], boards[1]))

    
@bot.command(pass_context=False)  # разрешаем передавать агрументы
async def flip(ctx):
    flag = random.randint(0, 1)
    await ctx.send('reshka' if flag else 'orel')

    

bot.run(TOKEN)
