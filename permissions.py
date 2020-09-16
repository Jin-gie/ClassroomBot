import discord

eleve_perm = discord.Permissions(
    create_instant_invite = False,
    kick_members = False,
    ban_members = False,
    administrator = False,
    manage_channels = False,
    manage_guild = False,
    view_audit_log = False,
    priority_speaker = False,
    stream = False,
    manage_messages = False,
    embed_links = False,
    external_emojis = False,
    view_guild_insights = False,
    mute_members = False,
    deafen_members = False,
    move_members = False,
    manage_nicknames = False,
    manage_roles = False,
    manage_webhooks = False,
    manage_emojis = False,

    add_reactions=True,
    read_messages = True,
    view_channel = True,
    send_messages = True,
    send_tts_messages = True,
    attach_files = True,
    read_message_history = True,
    mention_everyone = True,
    connect = True,
    speak = True,
    use_voice_activation = True,
    change_nickname = True
)

