import discord
from discord import PermissionOverwrite
from discord.ext import commands
from discord.utils import get
from permissions import *


async def creation(ctx, guild, class_name):
    ###
    # Crée le rôle, la catégorie et les salons à partir du nom de la classe
    # Entrées :
    #   - contexte
    #   - serveur
    #   - nom de la classe (paramètre de commande entré par l'utilisateur)
    ###
    role = await guild.create_role(name=class_name, permissions=eleve_perm, hoist=True, mentionable=True)

    ###
    # Crée la catégorie et les channels du nom de la classe
    ###
    category = await guild.create_category(class_name)
    print("Catégorie créée")

    # Text Channels
    general_channel = await guild.create_text_channel(f"{class_name}-général", category=category)
    documents_channel = await guild.create_text_channel(f"{class_name}-documents", category=category)
    classe_channel = await guild.create_text_channel(f"{class_name}-classe", category=category)

    # Vocal Channel
    vocal_channel = await guild.create_voice_channel(f"{class_name}-général", category=category)

    ###
    # Changer les rôles spécifiques aux channels :
    # - catégorie : @everyone ne peut pas voir et @class_name peut voir
    # - documents : @class_name ne peut pas écrire
    ###
    await category.set_permissions(guild.default_role, view_channel=False)
    await category.set_permissions(role, view_channel=True)
    await documents_channel.set_permissions(role, view_channel=True, send_messages = False, send_tts_messages = False, attach_files = False)

    await ctx.send(f"La classe {class_name} a été créée")


async def suppression(ctx, class_name):
    guild = ctx.guild
    author_commande = ctx.message.author

    if get(guild.categories, name=class_name): # Le nom de la classe existe et a été trouvé
        category = get(guild.categories, name=class_name)
        role = get(guild.roles, name=class_name)
        # 1. Vérifier que l'utilisateur veut bien supprimer cette classe
        #ctx.send(f"Êtes-vous sûr.e de vouloir supprimer la classe {class_name} ? Cette action est irréversible !")

        # 2. Supprimer les channels et la catégorie
        for channel in category.channels:
            await channel.delete()
        await category.delete() # Supprime la catégorie

        # 3. Supprimer le rôle associé à la classe
        await role.delete()

        await ctx.send(f"La classe {class_name} a été supprimée")

    else: #Le nom de la classe n'a pas été trouvé
        await ctx.send("Cette classe n'existe pas")


async def is_authorized(ctx):
    if ctx.message.author.guild_permissions.administrator:
        # is admin
        return True
    else:
        # is not admin
        return False
