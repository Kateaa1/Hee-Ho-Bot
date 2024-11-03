#FOR REDISTRIBUTION

# Leave this here or nothing will work lmao, you need discord.py installed
import discord
from discord.ext import commands


#Put your bot token where it says 'put token here' !!!DELETE IT FROM THE CODE BEFORE REDISTRIBUTING!!!
TOKEN = 'put token here'

# This gives the bot intents
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='.',intents=intents)

# Print message to terminal when connected
@bot.event
async def on_ready():
    print(f'Connect success')

# Test thing I left in, dunno if deleting it causes issues, file is tiny anyway so who cares
@bot.command()
async def ping(ctx):
    await ctx.send ('Pong!') 

@bot.event
async def on_message(message):
    # Prevent bot from causing a feedback loop
    if message.author == bot.user:
        return

    # Check for a specific string, remove the ".lower" for case sensitivity
    if message.content.lower() == 'hee ho':  # Ensure this line is correctly formatted or it will break
        await message.channel.send('Hee ho')

    
    # Allow the bot to process commands
    await bot.process_commands(message)



# This will run the bot, make sure your token is correctly set at the top of file.
bot.run(TOKEN)