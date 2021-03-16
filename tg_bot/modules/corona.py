import random
from telegram.ext import run_async, Filters
from telegram import Message, Chat, Update, Bot, MessageEntity
from tg_bot import dispatcher
from tg_bot.modules.disable import DisableAbleCommandHandler

SFW_STRINGS = (
    "HOW CAN I PROTECT MYSELF FROM CORONAVIRUS?",
    "🧼BAR BAR HATH DHOLE BETA",
    "🚴‍♂️NIND PURI KRO RAT RAT BHAR GIRLFRIENDS SE BAT NA KRO🛌 WILL BOLSTER THE IMMUNE SYSTEM",
    "🛀MAINTAIN GOOD HYGIENE HABHITS AT ALL TIMES",
    "👬2 GAJ DURI BANAO",
    "😷BHAIYA MASK JRUR PEHNE JAB HOSPITALS YA BAHAR GHUMNE JAO TO",
    "🧻USE TISSUES WHEN COUGHING OR BLOWING NOSE",
    "🍎AGR BAHAR SE KUCH LAO TO PEHLE SAF KRO ESE BHUTNIKE KI TARAH KHANE NA BETH JAO",
    "STAY HOME STAY SAFE",
  )

@run_async
def corona(bot: Bot, update: Update):
    bot.sendChatAction(update.effective_chat.id, "typing") # Bot typing before send messages
    message = update.effective_message
    if message.reply_to_message:
      message.reply_to_message.reply_text(random.choice(SFW_STRINGS))
    else:
      message.reply_text(random.choice(SFW_STRINGS))

__help__ = """
- /corona  😷.
"""

__mod_name__ = "BREAK THE CHAIN"

CRNA_HANDLER = DisableAbleCommandHandler("corona", corona)

dispatcher.add_handler(CRNA_HANDLER)
