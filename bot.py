import discord
from discord.ext import commands
import asyncio
import random
import json


bot = commands.Bot(command_prefix=commands.when_mentioned_or('s.'), pm_help=True, owenr_id=185181025104560128, case_insensitive=True)
# bot.remove_command('help')

cogs = ['help', 'fun']

@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Activity(type=1,name="Playing status name"))
    print(bot.user.name)



@bot.event
async def on_command_error(msg,error):
    if error.args[0] == 'The check functions for command neko failed.':
        if type(msg.channel) == discord.channel.DMChannel:
            await msg.send("Currently can't use NSFW commands in DM")
        else:
            await msg.send("{} **is not an NSFW channel**".format(msg.channel.mention))

    if error.args[0] == 'The check functions for command lewd failed.':
        if type(msg.channel) == discord.channel.DMChannel:
            await msg.send("Currently can't use NSFW commands in DM")
        else:
            await msg.send("{} **is not an NSFW channel**".format(msg.channel.mention))

    if isinstance(error, commands.errors.CommandNotFound):
        await msg.send(f"{error.args[0]}")


    if isinstance(error,commands.errors.MissingPermissions):
        await msg.send(f"{error.args[0]}")

    if isinstance(error,commands.errors.BotMissingPermissions):
        await msg.send(f"{error.args[0]}")

    if isinstance(error, commands.DisabledCommand):
        await msg.send("**Command is not available**")

    if isinstance(error, commands.NoPrivateMessage):
        await msg.send("Can't be used in DM")

    if isinstance(error, commands.TooManyArguments):
        await msg.send("**Too many values given!**")

    if isinstance(error, commands.CommandOnCooldown):
        await msg.send("**Command is on cooldown**")



# @bot.command(hidden=True)
# async def play(msg):
#     pass

# @bot.command(hidden=True)
# async def leave(msg):
#     pass

# @bot.command(hidden=True)
# async def join(msg):
#     pass

# @bot.command(hidden=True)
# async def pause(msg):
#     pass

# @bot.command(hidden=True)
# async def resume(msg):
#     pass

# @bot.command(hidden=True)
# async def volume(msg):
#     pass

# @bot.command(hidden=True)
# async def skip(msg):
#     pass

# @bot.command(hidden=True)
# async def clear_songs(msg):
#     pass

# @bot.command(hidden=True)
# async def mark_song(msg):
#     pass




@bot.command(hidden=True, name='eval', aliases=['log'])
async def _eval(msg,*,cmd):
    if msg.author.id == 185181025104560128:
        try:
            await msg.send(eval(cmd))
        except:
            await msg.send("Something went wrong")


# LOADING THE COGS
if __name__ == '__main__':
    for i in cogs:
        bot.load_extension(i)
        print('{} loaded'.format(i))


bot.run('Your Bot Token Here')
