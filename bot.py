import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.reactions = True

bot = commands.Bot(command_prefix="!", intents=intents)

CHANNEL_ID = 1378448023625007287

@bot.event
async def on_ready():
    print(f"Connecté en tant que {bot.user}")

@bot.event
async def on_message(message):
    if message.channel.id == CHANNEL_ID and message.author != bot.user:
        await message.add_reaction("✅")
        await message.add_reaction("❌")

bot.run("MTM3ODQ3ODA5NzUyMjg4NDYzOA.GYmZMj.9L3OZANYvgeIZ7UYCtDMOj9-eoaShyuuX19LQw")