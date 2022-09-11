from telethon import events, Button, types
from JE313P import JE313P
from JE313P.status import *
from telethon.tl.types import ChannelParticipantsAdmins
from datetime import timedelta
from telethon.tl.functions.photos import GetUserPhotosRequest as P
from telethon.tl.functions.users import GetFullUserRequest


MISC_HELP = """
**چەند فەرمانێکی سادە بۆ دۆزینەوە و دەست.**

/ID
وەڵامی بەکارهێنەر بدە بۆ ئەوەی دەستی پیشان بدات یان دەستی گروپەکە

/info
بۆ پیشاندانی زانیاری بەکارهێنەر بە وەڵامدانەوەی

"""

@JE313P.on(events.NewMessage(pattern="^[!?/]ID"))
async def id(event):

    if event.is_private:
       await event.reply(f"ئایدی به رێزت `{event.sender_id}`.")
       return

    ID = """
**ئایدی گڕووپ :** `{}`
**ئایدی به کاڕهێنه ر :** `{}`
"""

    msg = await event.get_reply_message()
    if not msg:
      await event.reply(ID.format(event.chat_id, event.sender_id))
      return

    await event.reply(f"بەکارهێنەر {msg.sender.first_name} /n ئایدی `{msg.sender_id}`.")
 
@JE313P.on(events.NewMessage(pattern="^[!?/]info ?(.*)"))
async def info(event):

    sed = await JE313P(P(user_id=event.sender_id, offset=42, max_id=0, limit=80))
    hn = await JE313P(GetFullUserRequest(event.sender_id))
    text = "**زانیاری بەکارهێنەر:**\n\n"
    text += "**ناوی یەکەم:** {}\n"
    text += "**ناوی دووەم:** {}\n"
    text += "**ئایدی:** `{}`\n"
    text += "**ناسنامه:** @{}\n"
    text += "**ژمارەی وێنەکان:** `{}`\n"
    text += "**کورتەیەک:** `{}`\n"
    textn += "**لینکی ئەکاونتەکە:** [لێرەدا فشار بدە](tg://user?id={})\n"

    input_str = event.pattern_match.group(1)
    if not input_str:
          await JE313P.send_message(event.chat_id, text.format(hn.user.first_name, hn.user.last_name, event.sender_id, event.sender.username, sed.count, hn.about, event.sender_id))
          return
 
    input_str = event.pattern_match.group(1)
    ha = await JE313P.get_entity(input_str)
    hu = await JE313P(GetFullUserRequest(id=input_str))
    sedd = await JE313P(P(user_id=input_str, offset=42, max_id=0, limit=80))

    text = "**زانیاری بەکارهێنەر:**\n\n"
    text += "**ناوی یەکەم:** {}\n"
    text += "**ناوی دووەم:** {}\n"
    text += "**ئایدی:** `{}`\n"
    text += "**ناسنامه:** @{}\n"
    text += "**ژمارەی وێنەکان:** `{}`\n"
    text += "**کورتەیەک:** `{}`\n"
    textn += "**لینکی ئەکاونتەکە:** [لێرەدا فشار بدە](tg://user?id={})\n"

    await event.reply(textn.format(ha.first_name, ha.last_name, ha.id, ha.username, sedd.count, hu.about, ha.id))
   

@JE313P.on(events.callbackquery.CallbackQuery(data="misc"))
async def _(event):
    await event.edit(MISC_HELP, buttons=[[Button.inline("گه رانه وه", data="help")]])
