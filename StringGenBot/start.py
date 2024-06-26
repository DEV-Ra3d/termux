from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message

from config import OWNER_ID


def filter(cmd: str):
    return filters.private & filters.incoming & filters.command(cmd)

@Client.on_message(filter("start"))
async def start(bot: Client, msg: Message):
    me2 = (await bot.get_me()).mention
    await bot.send_message(
        chat_id=msg.chat.id,
        text=f"""⎚¦ اެهِݪاެ بَكَ عَࢪ࣪يَࢪ࣪يَ

⎚¦ يَمِكَنِكَ اެسِتَخِࢪاެجَ اެݪتَاެݪيَ

⎚¦ تيࢪمكس تݪثيۅٛن اެݪحساެباެت

⎚¦ تيࢪمكس تݪثيۅٛن اެݪبۅٛتاެت

⎚¦ باެيࢪۅٛجࢪاެم ميۅٛࢪ࣪ك اެݪبۅٛتاެت

⎚¦ باެيࢪۅٛجࢪاެم ميۅٛࢪ࣪ك اެݪبۅٛتاެت

⎚¦ تَمِ اެنِشِاެ۽ اެݪبَۅٛتَ بَۅٛاެسِطَةِ [ㅤ𓏺 ˛𝐒𝐎𝐔𝐑𝐂𝐄 R𝐀3𝐃 .. 🧑‍💻 ˼](https://t.me/SK_LH)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(text="إاެضغط ݪبد۽ اެستخࢪاެج كۅٛد", callback_data="generate")
                ],
                [
                    InlineKeyboardButton("🔥 اެݪسۅٛࢪس 🔥", url="https://t.me/SK_LH"),
                    InlineKeyboardButton("🧑‍💻 اެݪمِطَۅٛࢪ 🧑‍💻", user_id=OWNER_ID)
                ]
            ]
        ),
        disable_web_page_preview=True,
    )
