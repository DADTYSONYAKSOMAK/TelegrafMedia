import os
import logging
from pyrogram import Client, filters
from telegraph import upload_file
from config import Config
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
sbot = Client(
   "Telegraph Uploader",
   api_id=Config.APP_ID,
   api_hash=Config.API_HASH,
   bot_token=Config.TG_BOT_TOKEN,
)
@sbot.on_message(filters.command("start"))
async def start(client, message):
   if message.chat.type == 'private':
       await sbot.send_message(
               chat_id=message.chat.id,
               text="""<b>مرحبًا ، أنا بوت تحويل الصور الي تليجراف ميديا \n يمكنني تحميل الصور أو مقاطع الفيديو إلى تليجراف ميديا. \n تم صناعتي بواسطة @S_W_I1 \n اضغط على زر المساعدة لمعرفة المزيد حول كيفية استخدامي</b>""",   
                            reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "♆ المساعده ♆", callback_data="help"),
                                        InlineKeyboardButton(
                                            "♆ قناة التحديثات ♆", url="https://t.me/SO_Fra3nh")
                                    ],[
                                      InlineKeyboardButton(
                                            "♆ الدعم ♆", url="https://t.me/SP_Fra3nh")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")
@sbot.on_message(filters.command("help"))
async def help(client, message):
    if message.chat.type == 'private':   
        await sbot.send_message(
               chat_id=message.chat.id,
               text="""<b>مساعدة بوت تليجراف ميديا! \n ما عليك سوى إرسال صورة أو مقطع فيديو أقل من حجم ملف 5 ميجابايت ، سأقوم بتحميله إلى تلجراف ميديا. \n ~ @h_m_saT</b>""",
        reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "♆ رجوع ♆", callback_data="start"),
                                        InlineKeyboardButton(
                                            "♆ معلومات ♆", callback_data="about")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")
@sbot.on_message(filters.command("about"))
async def about(client, message):
    if message.chat.type == 'private':   
        await sbot.send_message(
               chat_id=message.chat.id,
               text="""<b>حول بوت تليجراف مبديا!</b> \n <b>♞ ⍣ المطور ⍣:</b> <a href="https://t.me/S_W_I1"> ⧛ SoUrCe FaR3Nh </a> \n <b>♞ ⍣ الدعم ⍣:</b> <a href="https://t.me/SP_Fra3nh">far3nh Support</a> \n <b>~ @S_W_I1</b>""",
     reply_markup=InlineKeyboardMarkup(
                                [[
                                        InlineKeyboardButton(
                                            "♆ رجوع ♆", callback_data="help")
                                    ]]
                            ),        
            disable_web_page_preview=True,        
            parse_mode="html")
@sbot.on_message(filters.photo)
async def telegraphphoto(client, message):
    msg = await message.reply_text("جاري تحويل الصوره الي تليجراف ميديا...")
    download_location = await client.download_media(
        message=message, file_name='root/SBtg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("يجب ان يكون حجم الملف اقل من 5 ميجا!") 
    else:
        await msg.edit_text(f'**تم التحويل الي تليجراف ميديا!\n\n👉 https://telegra.ph{response[0]}\n\nانضم هنا @h_m_saT**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)
@sbot.on_message(filters.video)
async def telegraphvid(client, message):
    msg = await message.reply_text("جاري التحويل الي تليجراف ميديا...")
    download_location = await client.download_media(
        message=message, file_name='root/SBtg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("بجب ان يكون حجم الفيديو اقل من 5 ميجا!") 
    else:
        await msg.edit_text(f'**تم التحويل الي تليجراف ميديا!\n\n👉 https://telegra.ph{response[0]}\n\nانضم هنا @h_m_saT**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)
@sbot.on_message(filters.animation)
async def telegraphgif(client, message):
    msg = await message.reply_text("جاري التحويل الي تليجراف ميديا...")
    download_location = await client.download_media(
        message=message, file_name='root/SBtg')
    try:
        response = upload_file(download_location)
    except:
        await msg.edit_text("يجب ان تكون الصوره المتحركه اقل من 5 ميجا!") 
    else:
        await msg.edit_text(f'**تم التحويل الي تليجراف ميديا!\n\n👉 https://telegra.ph{response[0]}\n\nانضم هنا @h_m_saT**',
            disable_web_page_preview=True,
        )
    finally:
        os.remove(download_location)
@sbot.on_callback_query()
async def button(bot, update):
      cb_data = update.data
      if "help" in cb_data:
        await update.message.delete()
        await help(bot, update.message)
      elif "about" in cb_data:
        await update.message.delete()
        await about(bot, update.message)
      elif "start" in cb_data:
        await update.message.delete()
        await start(bot, update.message)
print(
    """
Bot Started!
Join @h_m_saT
"""
)
sbot.run()
                                   
