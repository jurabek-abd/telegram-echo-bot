# Telegram Echo Bot

A simple yet feature-rich Telegram bot built with Python and aiogram that echoes messages back to users with fun modes like screaming and whispering.

## Features

- 🔄 **Echo Functionality** - Copies any message (text, photos, stickers, etc.) back to the user
- 🔊 **Scream Mode** - Converts text messages to UPPERCASE
- 🔇 **Whisper Mode** - Returns messages normally
- 📋 **Interactive Menus** - Navigate through inline keyboard menus
- 💬 **Command Support** - Multiple commands for different functionalities
- 👤 **Per-User State** - Each user has their own scream/whisper mode

## Prerequisites

- Python 3.8 or higher
- A Telegram Bot Token (get one from [@BotFather](https://t.me/botfather))

## Installation

### Option 1: Using uv (Recommended - Fast & Modern)

1. **Install uv** (if not already installed)

```bash
# On macOS/Linux
curl -LsSf https://astral.sh/uv/install.sh | sh

# On Windows
powershell -c "irm https://astral.sh/uv/install.ps1 | iex"
```

2. **Clone or download the project**

```bash
git clone <your-repo-url>
cd <project-directory>
```

3. **Sync dependencies**

```bash
uv sync
```

That's it! uv will automatically create a virtual environment and install all dependencies.

### Option 2: Using pip (Traditional)

1. **Clone or download the project**

```bash
git clone <your-repo-url>
cd <project-directory>
```

2. **Create a virtual environment**

```bash
python -m venv venv
```

3. **Activate the virtual environment**

On Windows:
```bash
venv\Scripts\activate
```

On macOS/Linux:
```bash
source venv/bin/activate
```

4. **Install dependencies**

```bash
pip install -r requirements.txt
```

## Configuration

1. **Create a `.env` file** in the project root:

```bash
touch .env  # On macOS/Linux
# or just create the file manually on Windows
```

2. **Add your bot token** to the `.env` file:

```env
BOT_TOKEN=your_bot_token_here
```

Replace `your_bot_token_here` with the actual token you received from [@BotFather](https://t.me/botfather).

> **⚠️ Important:** Never commit your `.env` file to version control. Make sure it's listed in your `.gitignore` file.

## Running the Bot

### With uv

```bash
uv run main.py
```

### With pip

Make sure your virtual environment is activated, then:

```bash
python main.py
```

You should see the bot start up. The terminal will be quiet until someone sends a message to your bot.

## Usage

Once the bot is running, open Telegram and find your bot. You can interact with it using these commands:

### Available Commands

- `/start` - Start the bot and get a welcome message
- `/help` - Show available commands and their descriptions
- `/menu` - Display an interactive menu with navigation buttons
- `/scream` - Enable scream mode (replies in UPPERCASE)
- `/whisper` - Enable whisper mode (replies normally)

### Example Usage

1. Send `/start` to begin
2. Send any message - the bot will echo it back
3. Send `/scream` to activate scream mode
4. Send "hello world" - bot replies "HELLO WORLD"
5. Send `/whisper` to return to normal mode
6. Send `/menu` to see the interactive menu
7. Use the navigation buttons to explore Menu 1 and Menu 2

## Project Structure

```
.
├── main.py              # Main bot application
├── .env                # Environment variables (create this)
├── .env.example        # Example environment file
├── pyproject.toml      # Project configuration and dependencies (for uv)
├── requirements.txt    # Python dependencies (for pip)
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## Dependencies

The bot uses the following Python packages:

- **aiogram** (3.x) - Modern Telegram Bot API framework
- **python-dotenv** - Load environment variables from .env file

Dependencies are managed in:
- `pyproject.toml` - For uv users
- `requirements.txt` - For pip users

## Troubleshooting

### Bot doesn't respond

1. Make sure the bot is running (check your terminal)
2. Verify your BOT_TOKEN is correct in the `.env` file
3. Ensure you've started a conversation with your bot on Telegram
4. Check for any error messages in the terminal

### ModuleNotFoundError

Make sure you've installed the dependencies:

With uv:
```bash
uv sync
```

With pip:
```bash
pip install -r requirements.txt
```

### Bot token not found

Ensure your `.env` file exists and contains:
```env
BOT_TOKEN=your_actual_token_here
```

## Development

### Adding New Commands

To add a new command, use the `@dp.message(Command("your_command"))` decorator:

```python
@dp.message(Command("hello"))
async def hello_command(message: Message):
    await message.answer("Hello there!")
```

### Adding New Menu Buttons

Modify the `get_menu_keyboard()` function to add more buttons:

```python
builder.button(text="New Button", callback_data="new_action")
```

Then handle the callback in the `callback_handler()` function.

## Deployment

For production deployment, consider:

1. **VPS Hosting** - Deploy on DigitalOcean, Linode, or AWS
2. **PaaS** - Use Heroku, Railway, or Render for easy deployment
3. **Containers** - Dockerize your application for consistency

See the [deployment guide](https://docs.aiogram.dev/en/latest/dispatcher/deployment.html) in aiogram documentation for more details.

## Resources

- [Telegram Bot API Documentation](https://core.telegram.org/bots/api)
- [aiogram Documentation](https://docs.aiogram.dev/)
- [aiogram GitHub Repository](https://github.com/aiogram/aiogram)
- [Telegram Bot Features](https://core.telegram.org/bots/features)

## License

This project is open source and available under the MIT License.

## Support

If you encounter any issues:

1. Check the [aiogram documentation](https://docs.aiogram.dev/)
2. Visit the [aiogram community](https://t.me/aiogram)
3. Contact [@BotSupport](https://t.me/botsupport) for Telegram Bot API issues

## Contributing

Feel free to fork this project and submit pull requests with improvements!

---

**Happy Botting! 🤖**
