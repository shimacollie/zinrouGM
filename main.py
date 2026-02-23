import os
import discord
from discord.ext import commands
from game import GameState

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

game = None

@bot.command()
async def create(ctx):
    global game
    game = GameState(ctx.guild, ctx.channel)
    await ctx.send("ゲームを作成しました")

@bot.command()
async def join(ctx):
    game.players.append(ctx.author)
    await ctx.send(f"{ctx.author.display_name} が参加しました")

@bot.command()
async def start(ctx):
    await game.start()
    await ctx.send("ゲーム開始")

bot.run(TOKEN)
