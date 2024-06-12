import os
import discord
from discord.ext import commands

from datetime import datetime, timedelta
from date_time_event import Untiltime

import threading
import asyncio

import discord,asyncio,os
from discord.ext import commands, tasks

import atexit
import signal

import subprocess

from pynput.keyboard import Key, Controller
import time
import pyautogui
import time

from datetime import datetime

import sys

# Redirect stdout and stderr to a file
sys.stdout = log_file
sys.stderr = log_file


intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!",intents=intents)

print("hihi")




emojis = [
    '🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯',
    '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹',
    '🇺', '🇻', '🇼', '🇽', '🇾', '🇿'
]

qwertyRow = ['🇶', '🇼', '🇪', '🇷', '🇹', '🇾', '🇺', '🇮', '🇴', '🇵'] 

asdfRow = ['🇦', '🇸', '🇩', '🇫', '🇬', '🇭', '🇯', '🇰', '🇱']

zxcRow = ['⬛', '🇿', '🇽', '🇨', '🇻', '🇧', '🇳', '🇲'] 

qwertyCorrespondance = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']

asdfCorrespondance = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']

zxcCorrespondance = ['z', 'x', 'c', 'v', 'b', 'n', 'm']

qwertyMessage = None
asdfMessage = None
zxcMessage = None

@bot.command(name = "click")
async def unlockComputer(ctx):
    if str(ctx.author.id) == str(privilegedUser):
        pyautogui.click()
    await ctx.message.delete()
    return

@bot.event
async def on_ready():
    global qwertyMessage, asdfMessage, zxcMessage
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

    # Get the channel
    channel = bot.get_channel(keyboardChannel)
    
    if channel is not None:
        # Send the message
        await channel.purge()
        qwertyMessage = await channel.send('\u200B')
        
        # React to the message with each emoji in the list
        for emoji in qwertyRow:
            await qwertyMessage.add_reaction(emoji)
        
        asdfMessage = await channel.send('\u200B')
        
        # React to the message with each emoji in the list
        for emoji in asdfRow:
            await asdfMessage.add_reaction(emoji)

        zxcMessage = await channel.send('\u200B')
        
        # React to the message with each emoji in the list
        for emoji in zxcRow:
            await zxcMessage.add_reaction(emoji)

@bot.event
async def on_reaction_add(reaction, user):
    await process_reaction(reaction, user)



@bot.event
async def on_reaction_remove(reaction, user):
    await process_reaction(reaction,user )


async def process_reaction(reaction, user):
    global qwertyMessage, asdfMessage, zxcMessage
    # Check if the reaction is added by the bot itself
    if user == bot.user:
        return

    # Check if the reaction is added in the keyboard channel
    if reaction.message.channel.id == keyboardChannel:
        # Check which row the reaction is from
        if reaction.message.id == qwertyMessage.id:
            letter = qwertyRow.index(str(reaction.emoji))
            print(qwertyCorrespondance[letter], end = '')
            print('hello')
            pyautogui.typewrite(qwertyCorrespondance[letter])
        elif reaction.message.id == asdfMessage.id:
            letter = asdfRow.index(str(reaction.emoji))
            print(asdfCorrespondance[letter], end = '')
            print('bye')
            pyautogui.typewrite(asdfCorrespondance[letter])
        elif reaction.message.id == zxcMessage.id:
            letter = zxcRow.index(str(reaction.emoji)) - 1
            if letter != -1:
                print(zxcCorrespondance[letter], end = '')
                print('lol')
                pyautogui.typewrite(zxcCorrespondance[letter])
        #await reaction.remove(user)


bot.run(TOKEN)
