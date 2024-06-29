from typing import Final
import os, asyncio
from dotenv import load_dotenv
import discord
from discord import Message
import yt_dlp
from discord.ext import commands
from responses import get_response

from help_cog import help_cog
from music_cog import music_cog

# Load discord token
load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

intents_music = discord.Intents.all()
bot = commands.Bot(command_prefix='/', intents=intents_music)

bot.remove_command('help')


async def main_music():
    async with bot:
        await bot.add_cog(help_cog(bot))
        await bot.add_cog(music_cog(bot))
        await bot.start(TOKEN)


async def send_message(message: Message, user_message: str) -> None:
    if not user_message:
        return

    if is_private := user_message[0] == '?':
        user_message = user_message[1:]

    try:
        response: str = get_response(user_message, str(message.author))
        if response != "":
            await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


@client.event
async def on_ready() -> None:
    print(f'{client.user} is running')


@client.event
async def on_message(message: Message) -> None:
    if message.author == client.user:
        return

    username: str = str(message.author)
    user_message: str = message.content
    channel: str = str(message.channel)

    print(f'[{channel}] {username}: "{user_message}"')
    await send_message(message, user_message)


def main() -> None:
    client.run(token=TOKEN)


if __name__ == '__main__':
    asyncio.run(main_music())
    # main()
