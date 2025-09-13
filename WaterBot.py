import discord
from discord.ext import commands

# Create a bot instance with a command prefix
bot = commands.Bot(command_prefix='!')

# Event that triggers when the bot is ready
@bot.event
async def on_ready():
    print(f'Logged in as {bot.user.name} (ID: {bot.user.id})')
    print('------')

# Command to respond to
@bot.command()
async def hello(ctx):
    await ctx.send('Hello! I am your friendly bot!')

# Run the bot with your token
bot.run('YOUR_BOT_TOKEN')
