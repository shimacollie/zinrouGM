import os
import discord
from discord import app_commands
from discord.ext import commands
from game import GameState

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)
tree = bot.tree

game = None

@tree.command(name="create", description="ゲームを作成")
async def create(interaction: discord.Interaction):
    guild = discord.Object(id=1288071655427543072)
    global game
    game = GameState(interaction.guild, interaction.channel)
    await interaction.response.send_message("ゲームを作成しました")

@tree.command(name="join", description="ゲームに参加")
async def join(interaction: discord.Interaction):
    guild = discord.Object(id=1288071655427543072)
    game.players.append(interaction.user)
    await interaction.response.send_message(f"{interaction.user.display_name} が参加しました")

@tree.command(name="start", description="ゲーム開始")
async def start(interaction: discord.Interaction):
    guild = discord.Object(id=1288071655427543072)
    await game.start()
    await interaction.response.send_message("ゲーム開始")

@bot.event
async def on_ready():
    guild = discord.Object(id=1288071655427543072)
    await tree.sync(guild=guild)
    print(f"ログインしました: {bot.user}")

bot.run(TOKEN)
