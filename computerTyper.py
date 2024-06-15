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
keyboard = Controller()

import time
import pyautogui
import time

from datetime import datetime

import sys

from PIL import Image

from dotenv import load_dotenv
import os

# Redirect stdout and stderr to a file

load_dotenv()

programPath = os.getenv('programPath')

log_file = open(str(programPath + 'outputs/program_output'+ str(time.time())+ '.log'), 'w')

sys.stdout = log_file
sys.stderr = log_file


privilegedUser = int(os.getenv('privilegedUser'))
TOKEN = os.getenv('TOKEN')



keyboardChannel = int(os.getenv('keyboardChannel'))

intents = discord.Intents.all()

bot = commands.Bot(command_prefix="!",intents=intents)

print("program started successfully")

print(programPath, privilegedUser, TOKEN, keyboardChannel)



emojis = [
    '🇦', '🇧', '🇨', '🇩', '🇪', '🇫', '🇬', '🇭', '🇮', '🇯',
    '🇰', '🇱', '🇲', '🇳', '🇴', '🇵', '🇶', '🇷', '🇸', '🇹',
    '🇺', '🇻', '🇼', '🇽', '🇾', '🇿'
]

topArrowsRow = ['⏫', '⬆️', '⏬']
bottomArrowsRow = ['⬅️', '⬇️', '➡️']

numberRow = ['🏃‍♂️', '1️⃣', '2️⃣', '3️⃣', '4️⃣', '5️⃣', '6️⃣', '7️⃣', '8️⃣', '9️⃣', '0️⃣']


qwertyRow = ['👉', '🇶', '🇼', '🇪', '🇷', '🇹', '🇾', '🇺', '🇮', '🇴', '🇵', '⛔'] 

asdfRow = ['🔺', '🇦', '🇸', '🇩', '🇫', '🇬', '🇭', '🇯', '🇰', '🇱', "🖇️", "↩️"]

zxcRow = ['🆑','🅰️', '🇿', '🇽', '🇨', '🇻', '🇧', '🇳', '🇲', '🌌', '🪟'] 

mouseRow = ['❗', '⏫','⬅️', '⬆️', '⬇️', '➡️', '⏬', '❓']

screenshotRow = ['🔄', '⬆️']

numberCorrespondance = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

qwertyCorrespondance = ['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p']

asdfCorrespondance = ['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l']

zxcCorrespondance = ['z', 'x', 'c', 'v', 'b', 'n', 'm']



qwertyMessage = None
asdfMessage = None
zxcMessage = None
numberMessage = None
topArrowsMessage = None
bottomArrowsMessage = None
mouseMessage = None
screenshotMessage = None

capsMode = False
ctrlMode = False
altMode = False
windowsMode = False
mouseResolution = 64

screen_width, screen_height = pyautogui.size()

@bot.event
async def on_ready():
    global qwertyMessage, asdfMessage, zxcMessage, numberMessage, topArrowsMessage, bottomArrowsMessage, mouseMessage, screenshotMessage, mouseResolution
    print(f'Logged in as {bot.user.name} ({bot.user.id})')
    print('------')

    # Get the channel
    channel = bot.get_channel(keyboardChannel)
    
    print(channel)
    if channel is not None:
        # Send the message
        await channel.purge()
        
        numberMessage = await channel.send('\u200B')
        
        # React to the message with each emoji in the list
        for emoji in numberRow:
            await numberMessage.add_reaction(emoji)

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

        topArrowsMessage = await channel.send('\u200B')
        
        # React to the message with each emoji in the list
        for emoji in topArrowsRow:
            await topArrowsMessage.add_reaction(emoji)

        bottomArrowsMessage = await channel.send('\u200B')
        
        # React to the message with each emoji in the list
        for emoji in bottomArrowsRow:
            await bottomArrowsMessage.add_reaction(emoji)

        mouseMessage = await channel.send(str("Mouse Resolution is : "+ str(mouseResolution)))
        
        # React to the message with each emoji in the list
        for emoji in mouseRow:
            await mouseMessage.add_reaction(emoji)

        takeAScreenshot()
        with open(str(programPath + str("screenshots/screenshot.jpg")), "rb") as image:
            screenshotMessage = await channel.send('\u200B', file=discord.File(image))
        
        for emoji in screenshotRow:
            await screenshotMessage.add_reaction(emoji)


@bot.event
async def on_reaction_add(reaction, user):
    if str(user.id) == str(privilegedUser):
        await process_reaction(reaction, user)



@bot.event
async def on_reaction_remove(reaction, user):
    if str(user.id) == str(privilegedUser):
        await process_reaction(reaction, user)



def takeAScreenshot():
    screenshot = pyautogui.screenshot()
    screenshot = screenshot.convert('RGB')
    screenshot.save(str(programPath + str("screenshots/screenshot.jpg")), quality=10)

def takeAMaxResScreenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save(str(programPath + str("screenshots/screenshot.jpg")))

@bot.command(name = "lc")
async def leftCick(ctx):
    if str(ctx.author.id) == str(privilegedUser):
        pyautogui.click()
    await ctx.message.delete()
    return

@bot.command(name = "rc")
async def rightCick(ctx):
    if str(ctx.author.id) == str(privilegedUser):
        pyautogui.click(button='right')
    await ctx.message.delete()
    return

@bot.command(name = "mouse")
async def moveMouse(ctx, argument):
    argument = argument.split(",")
    if str(ctx.author.id) == str(privilegedUser):
        pyautogui.moveTo(int(argument[0]), int(argument[1]))
    await ctx.message.delete()
    return



@bot.command(name = "type")
async def unlockComputer(ctx, argument):
    print(argument, end = '')
    for char in argument:
        keyboard.type(char)
    await ctx.message.delete()
    return



async def process_reaction(reaction, user):
    global qwertyMessage, asdfMessage, zxcMessage, numberMessage, topArrowsMessage, bottomArrowsMessage, mouseMessage, screenshotMessage, capsMode, ctrlMode, altMode, windowsMode, mouseResolution
    # Check if the reaction is added by the bot itself
    channel = bot.get_channel(keyboardChannel)
    if user == bot.user:
        return
    
    
    

    # Check if the reaction is added in the keyboard channel
    if reaction.message.channel.id == keyboardChannel:
        # Check which row the reaction is from
        if reaction.message.id == numberMessage.id:
                letter = numberRow.index(str(reaction.emoji)) - 1
                if letter == -1:
                    pyautogui.press('esc')
                else :
                    print(numberCorrespondance[letter], end = '')
                    #print('hello')
                    pyautogui.typewrite(numberCorrespondance[letter])
        elif reaction.message.id == qwertyMessage.id:
            letter = qwertyRow.index(str(reaction.emoji)) - 1
            if letter == -1:
                pyautogui.press('tab')
                print('pressed Tab')
            elif letter == 10:
                pyautogui.press('backspace')
                print('backspace')
            else:
                print(qwertyCorrespondance[letter], end = '')
                #print('hello')
                pyautogui.typewrite(qwertyCorrespondance[letter])
        elif reaction.message.id == asdfMessage.id:
            letter = asdfRow.index(str(reaction.emoji)) - 1
            if letter == -1:
                if capsMode:
                    pyautogui.keyUp('shift')
                else:
                    pyautogui.keyDown('shift')
                capsMode = not capsMode
            elif letter == 9:
                print('"', end = '')
                #print('lol')
                keyboard.type('"')
            elif letter == 10:
                pyautogui.press('enter')
            else:
                print(asdfCorrespondance[letter], end = '')
                #print('bye')
                pyautogui.typewrite(asdfCorrespondance[letter])
        elif reaction.message.id == zxcMessage.id:
            letter = zxcRow.index(str(reaction.emoji)) - 2
            if letter == -2:
                if ctrlMode:
                    pyautogui.keyUp('ctrl')
                else:
                    pyautogui.keyDown('ctrl')
                ctrlMode = not ctrlMode
            elif letter == -1:
                if altMode:
                    print("pressed alt")
                    pyautogui.keyUp('alt')
                else:
                    print("")
                    pyautogui.keyDown('alt')
                altMode = not altMode
            elif letter == 7:
                print(' ', end = '')
                #print('lol')
                pyautogui.typewrite(' ')
            elif letter == 8:
                if windowsMode:
                    pyautogui.keyUp('winleft')
                else:
                    pyautogui.keyDown('winleft')
                windowsMode = not windowsMode
            else:
                print(zxcCorrespondance[letter], end = '')
                #print('lol')
                pyautogui.typewrite(zxcCorrespondance[letter])
        #await reaction.remove(user)
        elif reaction.message.id == topArrowsMessage.id:
            letter = topArrowsRow.index(str(reaction.emoji))
            if letter == 0:
                pyautogui.press('pageup')
            elif letter == 1:
                pyautogui.press('up')
            else :
                pyautogui.press('pagedown')
        elif reaction.message.id == bottomArrowsMessage.id:
            letter = bottomArrowsRow.index(str(reaction.emoji))
            if letter == 0:
                pyautogui.press('left')
            elif letter == 1:
                pyautogui.press('down')
            else :
                pyautogui.press('right')
        elif reaction.message.id == mouseMessage.id:
            letter = mouseRow.index(str(reaction.emoji))
            if letter == 0:
                pyautogui.click()
            elif letter == 1:
                mouseResolution *= 2
                mouseResolution = min(2048, mouseResolution)
            elif letter == 2:
                if pyautogui.position()[0] < mouseResolution:
                    pyautogui.moveTo(0, pyautogui.position()[1]) 
                else:
                    pyautogui.moveRel(-mouseResolution, 0)
            elif letter == 3:
                if pyautogui.position()[1] < mouseResolution:
                    pyautogui.moveTo(pyautogui.position()[0], 0) 
                else:
                    pyautogui.moveRel(0, -mouseResolution)
            elif letter == 4:
                if pyautogui.position()[1] > screen_height - mouseResolution:
                    pyautogui.moveTo(pyautogui.position()[0], screen_height) 
                else:
                    pyautogui.moveRel(0, mouseResolution)
            elif letter == 5:
                if pyautogui.position()[0] > screen_width - mouseResolution:
                    pyautogui.moveTo(screen_width, pyautogui.position()[1]) 
                else:
                    pyautogui.moveRel(mouseResolution, 0)
            elif letter == 6:
                mouseResolution //= 2
                mouseResolution = max(mouseResolution, 1)
            elif letter == 7:
                pyautogui.click(button='right')
            await mouseMessage.edit(content=str("Mouse Resolution is : "+ str(mouseResolution)))
        elif reaction.message.id == screenshotMessage.id:     
            letter = screenshotRow.index(str(reaction.emoji))
            if letter == 0:
                await screenshotMessage.delete()
                takeAScreenshot()
                with open(str(programPath + str("screenshots/screenshot.jpg")), "rb") as image:
                    screenshotMessage = await channel.send('\u200B', file=discord.File(image))
                for emoji in screenshotRow:
                    await screenshotMessage.add_reaction(emoji)
            if letter == 1:
                await screenshotMessage.delete()
                takeAMaxResScreenshot()
                with open(str(programPath + str("screenshots/screenshot.jpg")), "rb") as image:
                    screenshotMessage = await channel.send('\u200B', file=discord.File(image))
                for emoji in screenshotRow:
                    await screenshotMessage.add_reaction(emoji)
    
            

bot.run(TOKEN)
