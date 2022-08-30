import discord
from discord.ext import commands
import requests

intents = discord.Intents.default()
intents.message_content = True
ipinfo_api_token = "121010975c9f06"
ip = ""

token = "MTAxMzg1MzE2OTk3MDg1NTk1Nw.G6rdIf.OZm8e98UrNqbOsiQWpsqI6CsWeIW8RJAhIx5LM"
bot = commands.Bot(command_prefix='+', intents=intents)

@bot.command()
async def lookup(ctx, args):
	ipinfo_api_link = f"https://ipinfo.io/{args}?token={ipinfo_api_token}"
	look = requests.get(f"{ipinfo_api_link}")
	await ctx.send(f"""```{look.text}```""")

bot.run(token)