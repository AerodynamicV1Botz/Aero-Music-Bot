#
# Copyright (C) 2021-2022 by TeamYukki@Github, < https://github.com/TeamYukki >.
#
# This file is part of < https://github.com/TeamYukki/YukkiMusicBot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TeamYukki/YukkiMusicBot/blob/master/LICENSE >
#
# All rights reserved.


from YukkiMusic.plugins.techzbots.start import start_menu_group, start_menu_private
from typing import Union

from pyrogram import filters, types
from pyrogram.types import InlineKeyboardMarkup, Message

from config import BANNED_USERS
from strings import get_command, get_string, helpers
from YukkiMusic import app
from YukkiMusic.misc import SUDOERS
from YukkiMusic.utils import help_pannel
from YukkiMusic.utils.database import get_lang, is_commanddelete_on
from YukkiMusic.utils.decorators.language import (LanguageStart,
                                                  languageCB)
from YukkiMusic.utils.inline.help import (help_back_markup,
                                          private_help_panel)

### Command
HELP_COMMAND = get_command("HELP_COMMAND")


@app.on_message(
    filters.command(HELP_COMMAND)
    & filters.private
    & ~filters.edited
    & ~BANNED_USERS
)
async def helper_private(
    client: app, update: Union[types.Message, types.CallbackQuery]
):
    return await start_menu_private(update)


@app.on_message(
    filters.command(HELP_COMMAND)
    & filters.group
    & ~filters.edited
    & ~BANNED_USERS
)
@LanguageStart
async def help_com_group(client, message: Message, _):
    return await start_menu_group(message)


@app.on_callback_query(filters.regex("help_callback") & ~BANNED_USERS)
@languageCB
async def helper_cb(client, CallbackQuery, _):
    callback_data = CallbackQuery.data.strip()
    cb = callback_data.split(None, 1)[1]
    keyboard = help_back_markup(_)
    if cb == "hb5":
        if CallbackQuery.from_user.id not in SUDOERS:
            return await CallbackQuery.answer(
                "Only for Sudo Users", show_alert=True
            )
        else:
            await CallbackQuery.edit_message_text(
                helpers.HELP_5, reply_markup=keyboard
            )
            return await CallbackQuery.answer()
    try:
        await CallbackQuery.answer()
    except:
        pass
    if cb == "hb1":
        await CallbackQuery.edit_message_text(
            helpers.HELP_1, reply_markup=keyboard
        )
    elif cb == "hb2":
        await CallbackQuery.edit_message_text(
            helpers.HELP_2, reply_markup=keyboard
        )
    elif cb == "hb3":
        await CallbackQuery.edit_message_text(
            helpers.HELP_3, reply_markup=keyboard
        )
    elif cb == "hb4":
        await CallbackQuery.edit_message_text(
            helpers.HELP_4, reply_markup=keyboard
        )
