from discord.ext import commands

from main import *
from functions import *


#bot = main.bot


@bot.command()
async def test(ctx):
    if await is_authorized(ctx):
        print("yes")
    else:
        print("no")






@newclasse.error
async def on_command_error(ctx, error):
    await ctx.send(error)


@bot.command()
async def deleteclasse(ctx, class_name):
    if await is_authorized(ctx): # l'utilisateur de la commande est admin
        print("Deleting a class")
        await suppression(ctx, class_name)
    else: # l'utilisateur de la commande n'est pas admin
        await ctx.send(default_unauthorized)


@deleteclasse.error
async def on_command_error(ctx, error):
    await ctx.send(error)


@bot.command()
async def infos(ctx):
    print(ctx)
    print(ctx.guild)
    print(ctx.guild.name)