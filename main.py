from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
import random



Devourd=Client(
    "Pyrogram bot",
    bot_token="5110802092:AAFEH_XwJnHt4Pz-L2KccpAiz9uwWa0rqjM",
    api_id="10707816",
    api_hash="9726c3908f543bb2b81654ace45dd674"
)




ALL_PIC = [
 "https://telegra.ph/file/5150076a5e8d3ea3de995.jpg",
 "https://telegra.ph/file/b308d89346393bae36e67.jpg",
 "https://telegra.ph/file/c9e6e4ed8ad3269aca2bd.jpg",
 "https://telegra.ph/file/e02dad176eeca63fa83bf.jpg",
 "https://telegra.ph/file/37fd55f07a4670db6c2c6.jpg"
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
