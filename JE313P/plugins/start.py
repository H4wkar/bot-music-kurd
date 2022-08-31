from JE313P import JE313P, BOT_USERNAME
from Config import Config
from telethon import events, Button

PM_START_TEXT = """
 👋┇بەخێر بێیت ئازیزم ! {}
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘من بۆتێکی سادەم بۆ پاراستنی گروپەکەت و پەخشکردنی کلیپی دەنگی لە پەیوەندییەکدا*.
‣ **دەتوانم کلیپی دەنگی لە کاتی پەیوەندیدا لێبدەم**.
‣ **دەتوانم هەر بەکارهێنەرێک بلۆک بکەم و بێدەنگ بکەم**.
‣ **باشترین بۆت لە ڕووی تایبەتمەندییەوە**.
‣ **لەسەر بنەمای کتێبخانەی Telethon دروستکراوە بۆیە بۆتەکە خێرایە**!
➖➖➖➖➖➖➖➖➖➖➖➖➖➖
✘ اضغط على الاسفل لعرض الاوامر الخاصه بي.
[𖠄 𝗝𝗲𝗽𝘁𝗵𝗼𝗻 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 𖠄](https://t.me/JEPTHON)
"""

@JE313P.on(events.NewMessage(pattern="^[?!/]start$"))
async def start(event):

    if event.is_private:
       await event.client.send_file(event.chat_id,
             Config.START_IMG,
             caption=PM_START_TEXT.format(event.sender.first_name), 
             buttons=[
        [Button.url("➕ اضغط هنا لأضافتي", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("السورس", "https://t.me/JEPTHON")],
        [Button.url("الدعم", f"https://t.me/{Config.SUPPORT}"), Button.url("القناة", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("الاوامر", data="help")]])
       return

    if event.is_group:
       await event.reply("**- اهلا بك انا اعمل بنجاح**")
       return



@JE313P.on(events.callbackquery.CallbackQuery(data="start"))
async def _(event):
    if event.is_private:
       await event.edit(PM_START_TEXT.format(event.sender.first_name), buttons=[
        [Button.url("➕ اضغط هنا لاضافتي", f"https://t.me/{BOT_USERNAME}?startgroup=true")],
        [Button.url("السورس", "https://t.me/JEPTHON")],
        [Button.url("الدعم", f"https://t.me/{Config.SUPPORT}"), Button.url("القناة", f"https://t.me/{Config.CHANNEL}")],
        [Button.inline("الاوامر", data="help")]])
       return
