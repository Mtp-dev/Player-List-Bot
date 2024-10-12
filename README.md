# Minecraft Server Player Count Discord Bot

This Discord bot provides real-time information about the number of players across multiple Minecraft servers. It automatically updates the bot's status with the total number of players and allows users to check the list of players online via a `/list` slash command.

## Features

- **Real-time Player Count:** Updates the bot’s status every 20 seconds with the total number of players across all configured Minecraft servers.
- **Player List Command:** Use the `/list` command to get a list of all players currently online, displayed in a neat embedded message split by server.
- **Multi-Server Support:** Supports querying multiple Minecraft servers.

## Prerequisites

Make sure you have the following installed:
- Python 3.8 or higher
- `discord.py` for interacting with the Discord API
- `discord-py-slash-command` for slash command support
- `mcstatus` for querying Minecraft server status

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Mtp-dev/Player-List-Bot.git
   cd your-repo-name
   ```

2. **Install the required dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up the bot:**
   - Replace `'your-bot-token'` in `app.py` with your actual Discord bot token.
   - Add your Minecraft server IPs and ports in the `servers` list inside `app.py`.

4. **Run the bot:**
   ```bash
   python app.py
   ```

## Usage

Once the bot is running, it will automatically update its status with the total number of players online across all configured servers.

### Slash Command: `/list`

Use the `/list` command to display a list of players online on each Minecraft server. The result will be shown in an embedded message, with each server's players listed separately.

## Example

If you have two servers, the bot will display the player count as:
```
All The Mods 9: 5 players online
All The Mods 10: 3 players online
```
You can also use `/list` to view the players:
```
Minecraft Server Players:
All The Mods 9:
- Player1
- Player2
- ...

All The Mods 10:
- PlayerA
- PlayerB
- ...
```

## Environment Variables (Optional)

You can set your bot token using environment variables:
```bash
export BOT_TOKEN='your-bot-token'
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
