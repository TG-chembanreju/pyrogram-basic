from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random
import os
from sample_config import Config

Devourd=Client(
    "Pyrogram bot",
    bot_token=Config.TG_BOT_TOKEN,
    api_id=Config.APP_ID,
    api_hash=Config.API_HASH,
)




ALL_PIC = [
 "https://telegra.ph/file/13e3a3db37e41e0dd789a.jpg",
 "https://telegra.ph/file/3352445c553755d81a0d0.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg"
]







@Devourd.on_message(filters.command("start")) 
async def start_message(bot, message): 
    await message.reply_photo(
        photo=random.choice(ALL_PIC),
        caption=f"""CLICK AND JOIN {message.from_user.mention}""",
        reply_markup=InlineKeyboardMarkup( [[
            InlineKeyboardButton("click this to join", url="t.me/septemberfilms"),
            InlineKeyboardButton("click this to join", url="t.me/septemberfilms")
            ],[
            InlineKeyboardButton("click this to join", url="t.me/septemberfilms")
            ]]
            )
        )




HELP_MESSAGE="""
Hello {} my help means fully detail of coammandshere is
/id - get your telegram id
/about - show your full details
/start - start the bot"""




@Devourd.on_message(filters.command("help")) 
async def help_message(bot, message):

    await message.reply_text(
        text=HELP_MESSAGE.format(message.from_user.mention)
    )
    
    
    
    
    
    
@Devourd.on_message(filters.command("about")) 
async def about_message(bot, message):
    text = f"""
FIRST NAME - {message.from_user.first_name}
LAST NAME - {message.from_user.last_name}
username - @{message.from_user.username}
id _ -{message.from_user.id}
mention - {message.from_user.mention}
source code - githb.com/kamarjahan/pyrorgramfbot"""
    
    
    
    await message.reply_text(text=text)
    
    
    
    
    
@Devourd.on_message(filters.command("id")) 
async def id_message(bot, message):
    text = f"""here is -{message.from_user.id}"""
    
    
    
    await message.reply_text(text=text)
    

    
    
    
@Devourd.on_message(filters.command("dev")) 
async def dev_message(bot, message):
    text = f"""here is 
FIRST NAME - DEVOUR
LAST NAME -  DEVILS
username -  @DEVOURDEVILS
id _ -{message.from_user.id}
mention - @DEVOURDEVILS"""
    
    
    
    await message.reply_text(text=text)
    
    
    
    
    
    
    

    
    

Devourd.run()
