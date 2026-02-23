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

game = {}  

@@tree.command(name="create", description="ゲームを作成", guild=GUILD_OBJ)
async def create(interaction: discord.Interaction):

    guild_id = interaction.guild.id

    if guild_id in games:
        await interaction.response.send_message("すでにゲームがあります")
        return

    games[guild_id] = GameState(interaction.guild, interaction.channel)

    await interaction.response.send_message("ゲームを作成しました")

@tree.command(name="join", description="ゲームに参加", guild=GUILD_OBJ)
async def join(interaction: discord.Interaction):

    guild_id = interaction.guild.id

    game = games.get(guild_id)

    if not game:
        await interaction.response.send_message("先に /create してください")
        return

    game.players.append(interaction.user)

    await interaction.response.send_message(
        f"{interaction.user.display_name} が参加しました"
    )

    @@tree.command(name="start", description="ゲーム開始", guild=GUILD_OBJ)
async def start(interaction: discord.Interaction):

    guild_id = interaction.guild.id
    game = games.get(guild_id)

    if not game:
        await interaction.response.send_message("ゲームがありません")
        return

    await game.start()
    await interaction.response.send_message("ゲーム開始")

@bot.event
async def on_ready():
    guild = discord.Object(id=1288071655427543072)
    await tree.sync(guild=guild)
    print(f"ログインしました: {bot.user}")

bot.run(TOKEN)
