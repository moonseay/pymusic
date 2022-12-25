import asyncio
import importlib
import sys

from pyrogram import idle
from pytgcalls.exceptions import NoActiveGroupCall

import config
from config import BANNED_USERS
from Py import LOGGER, app, userbot
from Py.core.call import Anon
from Py.plugins import ALL_MODULES
from Py.utils.database import get_banned_users, get_gbanned

loop = asyncio.get_event_loop()


async def init():
    if (
        not config.STRING1
        and not config.STRING2
        and not config.STRING3
        and not config.STRING4
        and not config.STRING5
    ):
        LOGGER("Py").error(
            "Hey Sayang WTF! Setidaknya tambahkan string pyrogram, Betapa Murahnya..."
        )
        return
    if (
        not config.SPOTIFY_CLIENT_ID
        and not config.SPOTIFY_CLIENT_SECRET
    ):
        LOGGER("Py").warning(
            "Sur spotify id aur secret toh daala hi nahi aapne ab toh spotify se nahi chala paaoge gaane."
        )
    try:
        users = await get_gbanned()
        for user_id in users:
            BANNED_USERS.add(user_id)
        users = await get_banned_users()
        for user_id in users:
            BANNED_USERS.add(user_id)
    except:
        pass
    await app.start()
    for all_module in ALL_MODULES:
        importlib.import_module("Py.plugins." + all_module)
    LOGGER("Py.plugins").info(
        "Necessary Modules Imported Successfully."
    )
    await userbot.start()
    await Anon.start()
    try:
        await Anon.stream_decall("https://telegra.ph/file/167df52d1790a49850cb5.mp4")
    except:
        pass
    try:
        await Anon.stream_call(
            "https://telegra.ph/file/167df52d1790a49850cb5.mp4"
        )
    except NoActiveGroupCall:
        LOGGER("Py").error(
            "[ERROR] - \n\nHei Sayang pertama-tama buka telegram dan nyalakan obrolan suara di Logger Group kalau tidak, pergilah. Jika Anda pernah mengakhiri obrolan suara di grup log, saya akan berhenti bekerja dan pengguna akan bercinta dengan Anda."
        )
        sys.exit()
    except:
        pass
    await Anon.decorators()
    LOGGER("Py").info("\x41\x6e\x6f\x6e\x58\x20\x4d\x75\x73\x69\x63\x20\x42\x6f\x74\x20\x53\x74\x61\x72\x74\x65\x64\x20\x53\x75\x63\x63\x65\x73\x73\x66\x75\x6c\x6c\x79\x2e\x2e\x2e\n\n\x4e\x6f\x77\x20\x64\x72\x6f\x70\x20\x79\x6f\x75\x72\x20\x67\x69\x72\x6c\x66\x72\x69\x65\x6e\x64\'\x73\x20\x6e\x75\x64\x65\x73\x20\x61\x74\x20\x40\x44\x65\x76\x69\x6c\x73\x48\x65\x61\x76\x65\x6e\x4d\x46")
    await idle()


if __name__ == "__main__":
    loop.run_until_complete(init())
    LOGGER("Py").info("Stopping Music Bot...")
