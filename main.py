import discord
from commands import *
from functions import *
from discord.ext import commands

bot = commands.Bot(command_prefix="!")
default_unauthorized = "Sorry, vous n'êtes pas autorisé.e à faire ceci :("

###
# EVENTS
###

@bot.event
async def on_ready():
    print("We have logged in as {0.user}".format(bot))
    await bot.change_presence(status=discord.Status.idle, activity=discord.Game("révise ses cours"))


###
# COMMANDES
###

@test.error
async def on_command_error(ctx, error):
    # Gère les erreurs de commandes de manière générale : renvoie l'erreur
    await ctx.send(error)

@bot.command()
async def newclasse(ctx, class_name):
    ###
    # Créer une nouvelle classe si l'utilisateur a les persmissions de le faire
    # Entrées : contexte, nom de la classe (mettre entre "" si composé de plusieurs mots)
    # appel de la fonction creation()
    ###
    if await is_authorized(ctx): # l'utilisateur de la commande est un admin
        print(f"Creating a new class : {class_name}")
        guild = ctx.guild
        await creation(ctx, guild, class_name) # Procéder à la création de la catégorie et des chaînes
    else: # l'utilisateur de la commande n'est pas un admin
        await ctx.send(default_unauthorized)






bot.run("*") # Le token du bot a été remplacé par *
