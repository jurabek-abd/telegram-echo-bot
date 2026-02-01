# From BotFather to 'Hello World' - Python aiogram Edition

This guide will walk you through everything you need to know to build your first **Telegram Bot** using Python and the aiogram library.

If you already know your way around some of the basic steps, you can jump directly to the part you're missing.

## Table of Contents

* [Introduction](#introduction)
* [**Basic Tutorial**](#getting-ready)
  * [Environment](#getting-ready)
  * [First Run](#first-run)
  * [Echo Bot](#echo-bot)
* [**Advanced Tutorial**](#executing-commands)
  * [Commands](#executing-commands)
  * [Navigation](#navigation)
  * [Database](#database)
  * [Hosting](#hosting)
* [Further Reading](#further-reading)

---

## Introduction

At its core, you can think of the Telegram [Bot API](https://core.telegram.org/bots/api) as software that provides JSON-encoded responses to your queries.

A bot, on the other hand, is essentially a routine, software or script that queries the API by means of an HTTPS request and waits for a response. There are several types of requests you can make, as well as many different objects that you can use and receive as responses.

Since **your browser** is capable of sending HTTPS requests, you can use it to quickly try out the API. After obtaining your token, try pasting this string into your browser:

```
https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getMe
```

In theory, you could interact with the API with **basic requests** like this, either via your browser or other tailor-made tools like cURL. While this can work for simple requests like the example above, it's not practical for larger applications and doesn't scale well.

For that reason, this guide will show you how to use **aiogram**, a modern and fully asynchronous Python framework for the Telegram Bot API, along with some **basic programming skills**, to build a more robust and scalable project.

If you know how to code in Python, you'll fly right through each step in no time – and if you're just starting out, this guide will show you everything you need to learn.

> We will use Python 3.8+ throughout this guide as aiogram 3.x requires it. Python is beginner-friendly and works on all major operating systems.

## Getting Ready

First, we will briefly cover how to **create your first project**, obtain your **API token** and install all necessary **dependencies and libraries**.

For the purposes of this guide, a copy of the bot you will be creating is also live at [@TutorialBot](https://t.me/tutorialbot) – feel free to check it out along the way to see how your own implementation should look after each step.

### Obtain Your Bot Token

In this context, a **token** is a string that authenticates your bot (not your account) on the bot API. Each bot has a unique token which can also be revoked at any time via [@BotFather](https://t.me/botfather).

Obtaining a token is as simple as contacting [@BotFather](https://t.me/botfather), issuing the `/newbot` command and following the steps until you're given a new token. You can find a step-by-step guide [here](https://core.telegram.org/bots/features#creating-a-new-bot).

Your token will look something like this:

```
4839574812:AAFD39kkdpWt3ywyRZergyOLMaJhac60qc
```

> Make sure to save your token in a secure place, treat it like a password and **don't share it with anyone**.

### Install Python

To program in Python you'll need Python installed on your system. Most Linux and macOS systems come with Python pre-installed. For Windows, you can download it from [python.org](https://www.python.org/downloads/).

To check if Python is installed, open your terminal (Command Prompt on Windows) and run:

```bash
python --version
# or
python3 --version
```

You should see something like `Python 3.11.0` or higher. We recommend Python 3.8 or newer for aiogram 3.x.

### Choose a Code Editor

While you can use any text editor, we recommend:

* **VS Code** - Free, powerful, with great Python support
* **PyCharm** - Professional IDE with excellent Python features
* **Sublime Text** - Lightweight and fast
* **Any text editor** you're comfortable with

For beginners, VS Code is a great choice as it's free and has excellent extensions for Python development.

### Create Your Project

Let's create a project folder and set up a virtual environment:

```bash
# Create a project directory
mkdir telegram_bot_tutorial
cd telegram_bot_tutorial

# Create a virtual environment
python -m venv venv

# Activate the virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

After activation, you should see `(venv)` in your terminal prompt.

### Install aiogram

With your virtual environment activated, install aiogram:

```bash
pip install aiogram
```

This will install aiogram 3.x along with all its dependencies.

> aiogram is a modern, fully asynchronous framework that makes working with the Telegram Bot API in Python elegant and efficient.

## Start Coding

We are ready to start coding. If you're familiar with Python and async programming, this will be straightforward. If you're new to async/await, don't worry – we'll explain everything step by step.

### Creating Your Bot File

Create a new file called `bot.py` in your project directory:

```bash
touch bot.py  # On macOS/Linux
# or just create the file in your editor on Windows
```

### Basic Bot Structure

Let's start with the most basic bot setup. Open `bot.py` and add the following code:

```python
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

# Replace with your actual bot token
BOT_TOKEN = "4839574812:AAFD39kkdpWt3ywyRZergyOLMaJhac60qc"

# Create bot and dispatcher instances
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


# Handler for all messages
@dp.message()
async def echo_handler(message: Message):
    print(message)


# Main function to start the bot
async def main():
    # Start polling
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
```

Let's break down what each part does:

* **Bot** - Represents your bot instance and is used to make API calls
* **Dispatcher** - Routes updates (messages, callbacks, etc.) to appropriate handlers
* **@dp.message()** - A decorator that registers a handler for all messages
* **asyncio.run(main())** - Starts the event loop and runs your bot

> In production, you should store your token in environment variables or a config file. Keeping it in the code is fine for this tutorial, but it's not recommended for real applications.

## First Run

It's time to **run your bot** for the first time.

Make sure your virtual environment is activated, then run:

```bash
python bot.py
```

*And then there was nothing*. Yes, a bit anticlimactic.  
Actually, your bot is now running and waiting for messages! The terminal might look quiet, but it's working.

If you try messaging your bot on Telegram, you'll see **new updates** printed in the console. Each message will appear as a detailed Message object. At this point, you have your very own Telegram Bot – quite the achievement. Now, on to making it a bit more intelligent.

> If nothing pops up, make sure you messaged the right bot and that the token you pasted in the code is correct.

## Receiving Messages

Every time someone sends a **private message** to your bot, your handler function will be called automatically and you'll be able to handle the `message` parameter, which contains the message along with a great deal of other info.

Let's focus on two values for now:

* **The user** - Who sent the message. Access it via `message.from_user`
* **The message text** - What was sent. Access it via `message.text`

Knowing this, we can make it more clear in the **console output**:

```python
@dp.message()
async def echo_handler(message: Message):
    user = message.from_user
    print(f"{user.first_name} wrote: {message.text}")
```

This is just a basic example – you can now play around with all the attributes to see everything you can access. You can try `user.username`, `user.language_code`, `message.date`, and dozens more.

Knowing how to receive, process and print **incoming messages**, now it's time to learn how to **answer them**.

> Remember to stop (Ctrl+C) and re-run your bot after each change to the code.

## Sending Messages

To send a private text message, you generally need **two things**:

* The user **must** have contacted your bot first
* The **chat ID** - typically the user's ID (`message.from_user.id` or `message.chat.id`)

Let's update our bot to send messages back to the user:

```python
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

BOT_TOKEN = "4839574812:AAFD39kkdpWt3ywyRZergyOLMaJhac60qc"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def echo_handler(message: Message):
    user = message.from_user
    print(f"{user.first_name} wrote: {message.text}")
    
    # Send a message back
    await message.answer("Hello World!")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
```

Now, every time someone messages your bot, it will reply with "Hello World!".

The `message.answer()` method is a convenient shortcut that automatically sends a message to the same chat. You could also use:

```python
await bot.send_message(chat_id=message.chat.id, text="Hello World!")
```

> Try experimenting with other types of messages, like `send_photo()`, `send_sticker()`, `send_dice()`...  
> A full list is available in the [aiogram documentation](https://docs.aiogram.dev/en/latest/).

## Echo Bot

Let's practice everything we tried so far by coding an **Echo Bot**.  
Its functionality will be rather simple: every text message it receives will be sent right back to the user.

### Copying Text

The most intuitive way of coding this is simply sending back the text we received:

```python
@dp.message()
async def echo_handler(message: Message):
    await message.answer(message.text)
```

This works for text messages specifically.

### Copying Everything

There are more specific functions that can be used to copy any type of message and send it back, including photos, stickers, files, etc.:

```python
@dp.message()
async def echo_handler(message: Message):
    await message.copy_to(chat_id=message.chat.id)
```

The `copy_to()` method will copy any message type - text, photos, videos, stickers, documents, etc. - and send it back.

Here's a complete working Echo Bot:

```python
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message

BOT_TOKEN = "your_token_here"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message()
async def echo_handler(message: Message):
    # Copy any message type back to the user
    await message.copy_to(chat_id=message.chat.id)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
```

> This tutorial assumes that all updates contain messages for simplicity. In production, you should implement proper checks and handlers for different update types.

## Executing Commands

To learn what a command is and how it works, we recommend reading the [dedicated summary](https://core.telegram.org/bots/features#commands).  
In this guide, we'll focus on the technical side of things.

### Creating Your Command

Begin by opening [@BotFather](https://t.me/botfather).  
Type `/mybots` > *Your\_Bot\_Name* > Edit Bot > Edit Commands.

Now send a new command, followed by a brief description.  
For the purpose of this tutorial, we'll implement two simple commands:

```
scream - Speak, I'll scream right back
whisper - Shhhhhhh
```

### Command Logic

We want the **Echo Bot** to reply in uppercase when it's in **scream mode** and normally otherwise.

aiogram makes handling commands very easy with the `Command` filter. Here's how to implement our scream/whisper bot:

```python
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = "your_token_here"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Store screaming state (simple version - applies to all users)
screaming = False


@dp.message(Command("scream"))
async def scream_command(message: Message):
    global screaming
    screaming = True
    await message.answer("I'M SCREAMING NOW!")


@dp.message(Command("whisper"))
async def whisper_command(message: Message):
    global screaming
    screaming = False
    await message.answer("I'm whispering now...")


@dp.message()
async def echo_handler(message: Message):
    if screaming:
        # Scream mode - convert to uppercase
        if message.text:
            await message.answer(message.text.upper())
        else:
            # Can't scream a sticker, just copy it
            await message.copy_to(chat_id=message.chat.id)
    else:
        # Normal mode - just copy
        await message.copy_to(chat_id=message.chat.id)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
```

Let's break down the new parts:

* **Command("scream")** - A filter that only matches messages starting with `/scream`
* **global screaming** - Modifies the module-level variable (simple approach for this tutorial)
* **Handler order matters** - Command handlers come before the general message handler

Naturally, this simplified logic will change the bot's behavior for **everyone** – not just the person who sent the command. In a production environment, you'd want to track state per user. Here's a better approach:

```python
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = "your_token_here"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Store screaming state per user
user_states = {}


@dp.message(Command("scream"))
async def scream_command(message: Message):
    user_states[message.from_user.id] = "screaming"
    await message.answer("I'M SCREAMING NOW!")


@dp.message(Command("whisper"))
async def whisper_command(message: Message):
    user_states[message.from_user.id] = "whispering"
    await message.answer("I'm whispering now...")


@dp.message()
async def echo_handler(message: Message):
    user_id = message.from_user.id
    mode = user_states.get(user_id, "whispering")
    
    if mode == "screaming":
        if message.text:
            await message.answer(message.text.upper())
        else:
            await message.copy_to(chat_id=message.chat.id)
    else:
        await message.copy_to(chat_id=message.chat.id)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
```

> Remember to implement basic global commands like `/start` and `/help`. You can practice by adding these yourself!

## Buttons and Keyboards

To streamline and simplify user interaction with your bot, you can replace many text-based exchanges with handy buttons. These buttons can perform a wide variety of actions and can be customized for each user.

### Button Types

There are two main types of buttons:

* **Reply Keyboards** - used to provide a list of predefined text reply options
* **Inline Keyboards** - used to offer quick navigation, shortcuts, URLs, games and so much more

This guide will focus on **inline buttons** since they're more versatile and don't clutter the chat interface.

### Creating Buttons and Keyboards

In aiogram 3.x, creating inline keyboards is straightforward using builders:

```python
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

BOT_TOKEN = "your_token_here"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def get_menu_keyboard(menu_number: int):
    """Create inline keyboard for menus"""
    builder = InlineKeyboardBuilder()
    
    if menu_number == 1:
        # Menu 1 - only Next button
        builder.button(text="Next", callback_data="next")
    else:
        # Menu 2 - Back and Tutorial buttons
        builder.button(text="Back", callback_data="back")
        builder.button(text="Tutorial", url="https://core.telegram.org/bots/api")
    
    # Adjust to have one button per row
    builder.adjust(1)
    return builder.as_markup()


@dp.message(Command("menu"))
async def menu_command(message: Message):
    await message.answer(
        "<b>Menu 1</b>",
        reply_markup=get_menu_keyboard(1),
        parse_mode="HTML"
    )


@dp.callback_query()
async def callback_handler(callback: CallbackQuery):
    """Handle button presses"""
    if callback.data == "next":
        await callback.message.edit_text(
            "<b>Menu 2</b>",
            reply_markup=get_menu_keyboard(2),
            parse_mode="HTML"
        )
    elif callback.data == "back":
        await callback.message.edit_text(
            "<b>Menu 1</b>",
            reply_markup=get_menu_keyboard(1),
            parse_mode="HTML"
        )
    
    # Always answer callback queries to remove loading state
    await callback.answer()


@dp.message()
async def echo_handler(message: Message):
    await message.copy_to(chat_id=message.chat.id)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
```

Let's break down the new components:

* **InlineKeyboardBuilder** - A convenient way to build inline keyboards
* **builder.button()** - Adds a button with text and callback_data (or url)
* **builder.adjust(1)** - Arranges buttons (1 button per row)
* **callback_data** - Identifies which button was pressed
* **@dp.callback_query()** - Handler for button presses
* **callback.message.edit_text()** - Edits the message with the new menu
* **callback.answer()** - MUST be called to remove the loading indicator

Try sending `/menu` to your bot now. You should see a menu with navigation buttons!

### Navigation

When building complex bots, navigation is essential. In the example above, we already implemented basic navigation:

* The `Next` button navigates from Menu 1 to Menu 2
* The `Back` button returns to Menu 1
* The `Tutorial` button opens a URL

You can expand on this pattern to create complex menu systems, settings pages, and dynamic content. Here's a more complete example with multiple menus:

```python
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

BOT_TOKEN = "your_token_here"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def create_keyboard(buttons: list[tuple[str, str]], row_width: int = 1):
    """
    Create an inline keyboard from a list of (text, callback_data) tuples
    """
    builder = InlineKeyboardBuilder()
    for text, callback_data in buttons:
        if callback_data.startswith("http"):
            builder.button(text=text, url=callback_data)
        else:
            builder.button(text=text, callback_data=callback_data)
    builder.adjust(row_width)
    return builder.as_markup()


# Define our menus
MENUS = {
    "main": {
        "text": "<b>🏠 Main Menu</b>\n\nChoose an option:",
        "buttons": [
            ("⚙️ Settings", "settings"),
            ("ℹ️ About", "about"),
            ("📚 Help", "help"),
        ]
    },
    "settings": {
        "text": "<b>⚙️ Settings</b>\n\nConfigure your preferences:",
        "buttons": [
            ("🔔 Notifications", "notifications"),
            ("🌐 Language", "language"),
            ("🔙 Back", "main"),
        ]
    },
    "about": {
        "text": "<b>ℹ️ About</b>\n\nThis is a tutorial bot built with aiogram!",
        "buttons": [
            ("📖 Documentation", "https://docs.aiogram.dev"),
            ("🔙 Back", "main"),
        ]
    },
    "help": {
        "text": "<b>📚 Help</b>\n\nAvailable commands:\n/menu - Show this menu\n/start - Start the bot",
        "buttons": [
            ("🔙 Back", "main"),
        ]
    }
}


@dp.message(Command("start", "menu"))
async def show_menu(message: Message):
    menu = MENUS["main"]
    await message.answer(
        menu["text"],
        reply_markup=create_keyboard(menu["buttons"]),
        parse_mode="HTML"
    )


@dp.callback_query()
async def handle_callback(callback: CallbackQuery):
    # Get the menu based on callback data
    menu_key = callback.data
    
    if menu_key in MENUS:
        menu = MENUS[menu_key]
        await callback.message.edit_text(
            menu["text"],
            reply_markup=create_keyboard(menu["buttons"]),
            parse_mode="HTML"
        )
    
    # Always answer the callback
    await callback.answer()


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
```

This creates a navigable menu system with multiple pages. You can easily add more menus by adding entries to the `MENUS` dictionary.

## Database

Telegram **does not** host an update database for you – once you process and consume an update, it will no longer be available. This means that features like user lists, message history, user settings, statistics, etc. **have to be implemented and maintained** by you.

If your bot needs persistent data storage, here are some popular options for Python:

### SQLite (Recommended for Beginners)

SQLite is a lightweight, file-based database that's perfect for small to medium-sized bots:

```python
import sqlite3
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

BOT_TOKEN = "your_token_here"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def init_db():
    """Initialize the database"""
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            user_id INTEGER PRIMARY KEY,
            username TEXT,
            first_name TEXT,
            message_count INTEGER DEFAULT 0
        )
    ''')
    conn.commit()
    conn.close()


def save_user(user_id: int, username: str, first_name: str):
    """Save or update user in database"""
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO users (user_id, username, first_name, message_count)
        VALUES (?, ?, ?, 1)
        ON CONFLICT(user_id) DO UPDATE SET
            message_count = message_count + 1,
            username = excluded.username,
            first_name = excluded.first_name
    ''')
    conn.commit()
    conn.close()


def get_user_stats(user_id: int):
    """Get user statistics"""
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    cursor.execute('SELECT message_count FROM users WHERE user_id = ?', (user_id,))
    result = cursor.fetchone()
    conn.close()
    return result[0] if result else 0


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Welcome! Send me messages and I'll count them.")


@dp.message(Command("stats"))
async def stats_command(message: Message):
    count = get_user_stats(message.from_user.id)
    await message.answer(f"You've sent {count} messages!")


@dp.message()
async def message_handler(message: Message):
    # Save user and increment message count
    save_user(
        user_id=message.from_user.id,
        username=message.from_user.username or "",
        first_name=message.from_user.first_name
    )
    await message.answer("Message counted!")


async def main():
    # Initialize database on startup
    init_db()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
```

### Asynchronous Databases

For more advanced use cases, you might want to use asynchronous database libraries:

```bash
# Install aiosqlite for async SQLite
pip install aiosqlite

# Or install asyncpg for PostgreSQL
pip install asyncpg
```

Example with aiosqlite:

```python
import aiosqlite
from aiogram import Bot, Dispatcher
from aiogram.types import Message

# Async database initialization
async def init_db():
    async with aiosqlite.connect('bot.db') as db:
        await db.execute('''
            CREATE TABLE IF NOT EXISTS users (
                user_id INTEGER PRIMARY KEY,
                username TEXT,
                message_count INTEGER DEFAULT 0
            )
        ''')
        await db.commit()

async def save_user(user_id: int, username: str):
    async with aiosqlite.connect('bot.db') as db:
        await db.execute('''
            INSERT INTO users (user_id, username, message_count)
            VALUES (?, ?, 1)
            ON CONFLICT(user_id) DO UPDATE SET
                message_count = message_count + 1
        ''', (user_id, username))
        await db.commit()
```

### Other Database Options

* **Redis** - Fast in-memory cache, great for temporary data
* **MongoDB** - NoSQL database for flexible document storage
* **PostgreSQL** - Full-featured SQL database for large applications

> Always ensure that user data is **encrypted and secure** in your database to protect user privacy.

## Hosting

So far, your bot has been running on your **local machine**. While this is fine for development and testing, it's not ideal for production. You'll want your bot to be available 24/7.

### Option 1: Virtual Private Server (VPS)

A VPS is a virtual machine running on a cloud provider. Popular options include:

* **DigitalOcean** - Droplets starting at $5/month
* **Linode** - Simple cloud hosting
* **Vultr** - High-performance VPS
* **AWS EC2** - Amazon's cloud computing platform
* **Google Cloud** - Google's cloud platform

#### Basic VPS Setup:

```bash
# 1. Connect to your VPS via SSH
ssh root@your_vps_ip

# 2. Update system
apt update && apt upgrade -y

# 3. Install Python
apt install python3 python3-pip python3-venv -y

# 4. Create a directory for your bot
mkdir /opt/telegram_bot
cd /opt/telegram_bot

# 5. Upload your bot files (from your local machine)
scp -r /path/to/your/bot/* root@your_vps_ip:/opt/telegram_bot/

# 6. Create virtual environment
python3 -m venv venv
source venv/bin/activate

# 7. Install dependencies
pip install aiogram

# 8. Test run
python bot.py
```

#### Running Bot as a Service (systemd)

Create a systemd service file to keep your bot running:

```bash
# Create service file
nano /etc/systemd/system/telegram-bot.service
```

Add this content:

```ini
[Unit]
Description=Telegram Bot
After=network.target

[Service]
Type=simple
User=root
WorkingDirectory=/opt/telegram_bot
Environment="PATH=/opt/telegram_bot/venv/bin"
ExecStart=/opt/telegram_bot/venv/bin/python bot.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

Enable and start the service:

```bash
systemctl enable telegram-bot
systemctl start telegram-bot
systemctl status telegram-bot

# View logs
journalctl -u telegram-bot -f
```

### Option 2: Platform as a Service (PaaS)

Easier alternatives that handle infrastructure for you:

#### Heroku (Free tier available)

```bash
# 1. Install Heroku CLI
# 2. Create Procfile
echo "bot: python bot.py" > Procfile

# 3. Create requirements.txt
pip freeze > requirements.txt

# 4. Initialize git and deploy
git init
heroku create your-bot-name
git add .
git commit -m "Initial commit"
git push heroku main

# 5. Scale worker
heroku ps:scale bot=1
```

#### Railway.app (Simple deployment)

1. Push code to GitHub
2. Connect Railway to your repo
3. It auto-detects Python and installs dependencies
4. Your bot runs automatically

#### Render (Free tier available)

Similar to Railway - connect your GitHub repo and it handles deployment.

### Option 3: Docker

For better portability and consistency:

Create `Dockerfile`:

```dockerfile
FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "bot.py"]
```

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  bot:
    build: .
    restart: always
    volumes:
      - ./bot.db:/app/bot.db
    environment:
      - BOT_TOKEN=${BOT_TOKEN}
```

Run with:

```bash
docker-compose up -d
```

### Option 4: Serverless (Advanced)

For experienced developers, AWS Lambda or Google Cloud Functions can run your bot serverless using webhooks instead of polling.

### Best Practices for Production

1. **Use environment variables** for sensitive data:

```python
import os
BOT_TOKEN = os.getenv("BOT_TOKEN")
```

2. **Add logging**:

```python
import logging
logging.basicConfig(level=logging.INFO)
```

3. **Use webhooks** instead of polling (more efficient):

```python
from aiogram.webhook.aiohttp_server import SimpleRequestHandler, setup_application
from aiohttp import web

WEBHOOK_PATH = f"/bot/{BOT_TOKEN}"
WEBHOOK_URL = f"https://yourdomain.com{WEBHOOK_PATH}"

async def on_startup(bot: Bot):
    await bot.set_webhook(WEBHOOK_URL)

def main():
    dp.startup.register(on_startup)
    app = web.Application()
    webhook_requests_handler = SimpleRequestHandler(
        dispatcher=dp,
        bot=bot,
    )
    webhook_requests_handler.register(app, path=WEBHOOK_PATH)
    setup_application(app, dp, bot=bot)
    web.run_app(app, host="0.0.0.0", port=8000)
```

4. **Monitor your bot** - Use services like UptimeRobot to ensure it stays online

5. **Implement graceful shutdown**:

```python
async def main():
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()
```

## Further Reading

If you got this far, you might be interested in these resources:

* [aiogram Documentation](https://docs.aiogram.dev/) - Official aiogram docs
* [Telegram Bot API Reference](https://core.telegram.org/bots/api) - Complete API reference
* [General Bot Platform Overview](https://core.telegram.org/bots) - Telegram's bot overview
* [Detailed List of Bot Features](https://core.telegram.org/bots/features) - All bot capabilities
* [aiogram GitHub](https://github.com/aiogram/aiogram) - Source code and examples

### Complete Example Bot

Here's a complete example that brings everything together:

```python
import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message, CallbackQuery
from aiogram.utils.keyboard import InlineKeyboardBuilder

# Configure logging
logging.basicConfig(level=logging.INFO)

BOT_TOKEN = "your_token_here"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Store user states
user_modes = {}


def get_main_menu():
    """Create main menu keyboard"""
    builder = InlineKeyboardBuilder()
    builder.button(text="⚙️ Settings", callback_data="settings")
    builder.button(text="ℹ️ About", callback_data="about")
    builder.adjust(1)
    return builder.as_markup()


def get_settings_menu():
    """Create settings menu keyboard"""
    builder = InlineKeyboardBuilder()
    builder.button(text="🔊 Scream Mode", callback_data="scream")
    builder.button(text="🔇 Whisper Mode", callback_data="whisper")
    builder.button(text="🔙 Back", callback_data="main")
    builder.adjust(1)
    return builder.as_markup()


@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer(
        f"👋 Hello, {message.from_user.first_name}!\n\n"
        "I'm a tutorial bot built with aiogram. Here's what I can do:\n\n"
        "• Send me any message and I'll echo it back\n"
        "• Use /scream to make me reply in UPPERCASE\n"
        "• Use /whisper to make me reply normally\n"
        "• Use /menu to see the menu\n\n"
        "Try it out!"
    )


@dp.message(Command("menu"))
async def menu_command(message: Message):
    await message.answer(
        "<b>🏠 Main Menu</b>\n\nChoose an option:",
        reply_markup=get_main_menu(),
        parse_mode="HTML"
    )


@dp.message(Command("scream"))
async def scream_command(message: Message):
    user_modes[message.from_user.id] = "scream"
    await message.answer("🔊 SCREAM MODE ACTIVATED! I'LL SHOUT EVERYTHING!")


@dp.message(Command("whisper"))
async def whisper_command(message: Message):
    user_modes[message.from_user.id] = "whisper"
    await message.answer("🔇 Whisper mode activated. I'll speak normally now.")


@dp.callback_query()
async def callback_handler(callback: CallbackQuery):
    if callback.data == "main":
        await callback.message.edit_text(
            "<b>🏠 Main Menu</b>\n\nChoose an option:",
            reply_markup=get_main_menu(),
            parse_mode="HTML"
        )
    elif callback.data == "settings":
        mode = user_modes.get(callback.from_user.id, "whisper")
        current = "🔊 Scream" if mode == "scream" else "🔇 Whisper"
        await callback.message.edit_text(
            f"<b>⚙️ Settings</b>\n\nCurrent mode: {current}",
            reply_markup=get_settings_menu(),
            parse_mode="HTML"
        )
    elif callback.data == "about":
        await callback.message.edit_text(
            "<b>ℹ️ About</b>\n\n"
            "This is a tutorial bot created with aiogram 3.x.\n\n"
            "It demonstrates:\n"
            "• Command handling\n"
            "• Inline keyboards\n"
            "• State management\n"
            "• Message echoing",
            reply_markup=InlineKeyboardBuilder()
            .button(text="🔙 Back", callback_data="main")
            .as_markup(),
            parse_mode="HTML"
        )
    elif callback.data == "scream":
        user_modes[callback.from_user.id] = "scream"
        await callback.answer("🔊 Scream mode activated!")
        await callback.message.edit_text(
            "<b>⚙️ Settings</b>\n\nCurrent mode: 🔊 Scream",
            reply_markup=get_settings_menu(),
            parse_mode="HTML"
        )
    elif callback.data == "whisper":
        user_modes[callback.from_user.id] = "whisper"
        await callback.answer("🔇 Whisper mode activated!")
        await callback.message.edit_text(
            "<b>⚙️ Settings</b>\n\nCurrent mode: 🔇 Whisper",
            reply_markup=get_settings_menu(),
            parse_mode="HTML"
        )
    
    await callback.answer()


@dp.message()
async def echo_handler(message: Message):
    mode = user_modes.get(message.from_user.id, "whisper")
    
    if mode == "scream" and message.text:
        await message.answer(message.text.upper())
    else:
        await message.copy_to(chat_id=message.chat.id)


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
```

If you encounter any issues, you can:
* Check the [aiogram documentation](https://docs.aiogram.dev/)
* Join the [aiogram community](https://t.me/aiogram)
* Contact Telegram Bot Support at [@BotSupport](https://t.me/botsupport)

Happy coding! 🤖
