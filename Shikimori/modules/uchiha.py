"""
STATUS: Code is working. ✅
"""

"""
GNU General Public License v3.0

Copyright (C) 2022, SOME-1HING [https://github.com/SOME-1HING]

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <https://www.gnu.org/licenses/>.
"""

from Shikimori import dispatcher
from Shikimori.vars import NETWORK_USERNAME
from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update, ParseMode

from telegram.ext import (
    CallbackContext,
    CommandHandler,
)

PHOTO = "https://telegra.ph/file/5c21dc236bf53833bdde6.jpg"

network_name = NETWORK_USERNAME.lower()

if network_name == "macnetwork7":
    def uchiha(update: Update, context: CallbackContext):

        TEXT = f"""
ᴡᴇʟᴄᴏᴍᴇ ᴛᴏ [ MAC NETWORK ](https://t.me/macnetwork7/12),
MAC(My Anime Club) 𝙞𝙨 𝙖𝙣 𝙖𝙣𝙞𝙢𝙚 𝙗𝙖𝙨𝙚𝙙 𝘾𝙤𝙢𝙢𝙪𝙣𝙞𝙩𝙮 𝙬𝙞𝙩𝙝 𝙖 𝙢𝙤𝙩𝙞𝙫𝙚 𝙩𝙤 𝙨𝙥𝙧𝙚𝙖𝙙 𝙡𝙤𝙫𝙚 𝙖𝙣𝙙 𝙥𝙚𝙖𝙘𝙚 𝙖𝙧𝙤𝙪𝙣𝙙 𝙩𝙚𝙡𝙚𝙜𝙧𝙖𝙢. Its a network under which inter-connects all the groups and channel we have created or manage.
"""

        update.effective_message.reply_photo(
            PHOTO, caption= TEXT,
            parse_mode=ParseMode.MARKDOWN,

                reply_markup=InlineKeyboardMarkup(
                [
                    [InlineKeyboardButton(text="MAC NETWORK", url="https://t.me/macnetwork7/12")],
                    [
                    InlineKeyboardButton(text="★彡[ᴜꜱᴇʀ ᴛᴀɢ]彡★", url="https://t.me/macnetwork7"),
                    InlineKeyboardButton(text="★彡[ᴏꜰꜰɪᴄɪᴀʟ ɢʀᴏᴜᴘ]彡★", url="https://t.me/AnimeChattingGrp")
                    ],
                ]
            ),
        )


    uchiha_handler = CommandHandler(("mac", "network", "net"), uchiha, run_async = True)
    dispatcher.add_handler(uchiha_handler)

    __help__ = """
    ──「 MAC 𝘕𝘌𝘛𝘞𝘖𝘙𝘒 」──
    
    ❂ /mac: Get information about our community! Using it in groups may create promotion so we don't support using it in groups."""
    
    __mod_name__ = "「 MAC 」"
