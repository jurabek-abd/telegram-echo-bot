import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import CallbackQuery, Message
from aiogram.utils.keyboard import InlineKeyboardBuilder
from dotenv import load_dotenv

load_dotenv()


BOT_TOKEN = os.getenv("BOT_TOKEN", "")


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


user_states = {}


def get_menu_keyboard(menu_number: int):
    """Create inline keyboard for menus"""
    builder = InlineKeyboardBuilder()

    if menu_number == 1:
        builder.button(text="Next", callback_data="next")
    else:
        builder.button(text="Back", callback_data="back")
        builder.button(text="Tutorial", url="https://core.telegram.org/bots/tutorial")

    builder.adjust(1)
    return builder.as_markup()


@dp.message(Command("start"))
async def start_command(message: Message):
    user_full_name = message.from_user.full_name
    await message.answer(
        f"Hello, {user_full_name}! This is Echo Bot. If you need any help, just use /help command!"
    )


@dp.message(Command("help"))
async def help_command(message: Message):
    await message.answer(
        "/scream - Changes the mode to screaming. /whisper - Changes the mode to whispering."
    )


@dp.message(Command("menu"))
async def menu_command(message: Message):
    await message.answer(
        "<b>Menu 1</b>", reply_markup=get_menu_keyboard(1), parse_mode="HTML"
    )


@dp.message(Command("scream"))
async def scream_command(message: Message):
    user_id = message.from_user.id
    user_states[user_id] = "screaming"
    await message.answer("I AM SCREAMING NOW!")


@dp.message(Command("whisper"))
async def whisper_command(message: Message):
    user_id = message.from_user.id
    user_states[user_id] = "whispering"
    await message.answer("I'm whispering now...")


@dp.callback_query()
async def callback_handler(callback: CallbackQuery):
    """Handle button presses"""
    if callback.data == "next":
        await callback.message.edit_text(
            "<b>Menu 2</b>", reply_markup=get_menu_keyboard(2), parse_mode="HTML"
        )
    elif callback.data == "back":
        await callback.message.edit_text(
            "<b>Menu 1</b>", reply_markup=get_menu_keyboard(1), parse_mode="HTML"
        )

    await callback.answer()


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

    # await message.copy_to(
    #     chat_id=message.chat.id
    # )  # Copy any message type back to the user

    # user = message.from_user
    # if user is None:
    #     print(message.text)
    #     return
    # print(f"{user.first_name} wrote: {message.text}")

    # await bot.send_dice(chat_id=message.chat.id, emoji="🎰")


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
