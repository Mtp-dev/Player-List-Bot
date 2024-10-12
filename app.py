import discord
from discord.ext import tasks, commands
from mcstatus import MinecraftServer
from discord_slash import SlashCommand, SlashContext

# Server addresses (IP and Port)
servers = [
    {"name": "Server 1", "ip": "example1.mtp.gg", "port": 25565},
    {"name": "Server 2", "ip": "example2.mtp.gg", "port": 25565}
]

# Intents
intents = discord.Intents.default()

# Using commands.Bot instead of discord.Client
bot = commands.Bot(command_prefix="!", intents=intents)
slash = SlashCommand(bot, sync_commands=True)  # Enable slash commands and sync them automatically

async def fetch_player_counts():
    total_players = 0
    for server_info in servers:
        server = MinecraftServer.lookup(f"{server_info['ip']}:{server_info['port']}")
        try:
            status = server.status()
            total_players += status.players.online
        except Exception as e:
            print(f"Error fetching from {server_info['ip']}: {e}")
    return total_players

async def fetch_players():
    server_players = {}
    for server_info in servers:
        server = MinecraftServer.lookup(f"{server_info['ip']}:{server_info['port']}")
        try:
            status = server.status()
            if status.players.sample:  # Check if the sample exists (players online)
                player_list = [player.name for player in status.players.sample]
            else:
                player_list = ["No players online"]
            server_players[server_info['name']] = player_list
        except Exception as e:
            server_players[server_info['name']] = [f"Error fetching players: {e}"]
    return server_players

@tasks.loop(seconds=20)  # Update every 20 seconds
async def update_status():
    total_players = await fetch_player_counts()
    activity = discord.Game(f"{total_players} players online")
    await bot.change_presence(status=discord.Status.online, activity=activity)

@bot.event
async def on_ready():
    print(f'Bot connected as {bot.user}')
    update_status.start()
    print("Bot is ready!")

# /list command to display players on all Minecraft servers
@slash.slash(name="list", description="List players on all Minecraft servers")
async def list_players(ctx: SlashContext):
    server_players = await fetch_players()
    
    embed = discord.Embed(title="Minecraft Server Players", color=discord.Color.blue())
    
    for server_name, players in server_players.items():
        player_list_str = "\n".join(players)
        embed.add_field(name=f"{server_name}", value=player_list_str, inline=False)
    
    await ctx.send(embed=embed)

# Run the bot
bot.run('your-bot-token')
