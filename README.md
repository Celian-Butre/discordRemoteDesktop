# Discord Remote Desktop
## Brief Description
This program allows you to control your entire computer with your phone, it does this by hosting a discord bot on a private server, and through reactions to the bots messages, allows you to request different actions to your computer, those actions are described further bellow.

## Requirements
Works best on QWERTY keyboard\
Run the INSTALLME.py script to have everything needed installed\
You need to create a discord bot : https://discordpy.readthedocs.io/en/stable/discord.html \
You need to create a server where you will communicate with the discord bot \
Fill in the .env with your corresponding info

## Usage
### Built-in Commands
- !lc : performs a left click
- !rc : performs a right click
- !mouse x,y : moves your mouse to x,y coordinates
- !type aStringOfText : types out that string of text, do not include double quotes (") inside the message or it will crash, you can encapsulate the message in double quotes if you want to have spaces in the string.

### Reactions
- First row : Running man is escape, the rest are the corresponding numbers
- Second row : Index finger is tab, the rest are letters and the stop sign is backspace
- Third row : The triangle is a caps lock button, the letters are letters, the paperclips are double quotes, and the return emoji is the enter key
- Fourth row : CL is a control key that functions like caps lock (on/off), A is alt with the same caps lock method, the galaxy emoji is the space key, and the windows is the windows key
- Fifth row : in order : page up, up arrow, page down
- Sixt row : in order : left arrow, down arrow, right arrow
- Seventh row : Mouse buttons : exclamation mark is left click, and question mark is right click, the simple arrows move the mouse by Mouse Resolution pixels, and the doubled arrows respectivily double the Mouse Resolution and half the Mouse Resolution
- Screenshot Row : the reload button sends a new screenshot at 30 percent jpg compression and the up arrow sends a heavier raw jpg 
