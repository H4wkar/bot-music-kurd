import os

from telethon import Button, events

from JE313P import *

IMG = os.environ.get(
    "PING_PIC", "https://telegra.ph/file/2e9d4b0c76cf8c67f07df.jpg"
)
ms = 4

ALIVE = os.environ.get(
    "ALIVE", "@lMl10l"
)

CAPTION = f"**خێرای ئینته رنیتی بوت:** {ms}\n المالك:『{ALIVE}』"


@JE313P.on(events.NewMessage(pattern="^/خه ت"))
async def _(event):
    UMM = [[Button.url("خاوه نی بۆت", "https://t.me/SARKAUT")]]
    await JE313P.send_file(event.chat_id, IMG, caption=CAPTION, buttons=UMM)
