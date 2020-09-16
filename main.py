import discord
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

@bot.command()
async def newclasse(ctx, class_name):
    ###
    # Créer une nouvelle classe si l'utilisateur a les permissions de le faire
    # Entrées :
    #   - contexte
    #   - nom de la classe (mettre entre "" si composé de plusieurs mots)
    # appel de la fonction creation()
    ###
    if await is_authorized(ctx): # l'utilisateur de la commande est un admin
        print(f"Creating a new class : {class_name}")
        guild = ctx.guild
        await creation(ctx, guild, class_name) # Procéder à la création de la catégorie et des chaînes
    else: # l'utilisateur de la commande n'est pas un admin
        await ctx.send(default_unauthorized)


@newclasse.error
async def on_command_error(ctx, error):
    ###
    # Gère les erreurs de la commande !newclasse
    ###
    await ctx.send(error)


@bot.command()
async def changeclasse(ctx, old_classe, new_classe):
    ###
    # Change les élèves dans un groupe vers un autre
    # Si pas de 2nd argument : juste enlever le rôle
    # Entrées :
    #   - contexte
    #   - nom de l'ancienne classe -> role à enlever
    #   - nom de la nouvelle classe -> role à mettre
    ###

    if await is_authorized(ctx): # l'utilisateur de la commande est un admin
        print("Ancienne classe : " + old_classe)
        print("Nouvelle classe : " + new_classe)
        await changement(ctx, old_classe, new_classe)

    else : # l'utilisateur de la commande n'est pas un admin
        await ctx.send(default_unauthorized)


@changeclasse.error
async def on_command_error(ctx, error):
    ###
    # Gère les erreurs de la commande !changeclasse
    ###
    await ctx.send(error)


@bot.command()
async def deleteclasse(ctx, class_name):
    ###
    # Supprime la classe donnée si l'utilisateur a les permissions de le faire
    # Entrées :
    #   - contexte
    #   - nom de la classe (mettre entre "" si composé de plusieurs mots)
    # appel de la fonction suppression()
    ###
    if await is_authorized(ctx): # l'utilisateur de la commande est admin
        print("Deleting a class")
        await suppression(ctx, class_name)
    else: # l'utilisateur de la commande n'est pas admin
        await ctx.send(default_unauthorized)


@deleteclasse.error
async def on_command_error(ctx, error):
    ###
    # Gère les erreurs de la commande !deleteclasse
    ###
    await ctx.send(error)


bot.run("NzQ2MjczMjU1MzI5MTAzOTY5.Xz97IQ.px9dkh9I24f3Ece4GO61aKDFRmQ")
