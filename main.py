import sys
import tomllib

import discord
from discord.ext import commands
from loguru import logger

with open('config.toml', 'rb') as file:
    config = tomllib.load(file)

intents = discord.Intents.default()
intents.members = True
intents.messages = True
intents.message_content = True
intents.guilds = True
intents.reactions = True

bot = commands.Bot(
    intents=intents,
    help_command=commands.DefaultHelpCommand(),
    allowed_mentions=discord.AllowedMentions.none())

@bot.event
async def on_ready():
    logger.info(f'Logged in as {bot.user.name}#{bot.user.discriminator} ({bot.user.id})')


bot.load_extension('cogs', recursive=True)

sys.exit(bot.run(config['bot']['token']))
