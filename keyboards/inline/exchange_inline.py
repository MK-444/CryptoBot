from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# ========================== 💱 Exchange ========================
async def exchange_buttons() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="📈 Купить", callback_data="buy")
    btn2 = InlineKeyboardButton(text="📉 Продать", callback_data="sell")
    btn3 = InlineKeyboardButton(text="🗃 История обменов", callback_data="history")
    btn4 = InlineKeyboardButton(text="👝 Кошелек", callback_data="wallet")
    markup.row(btn1, btn2).add(btn3, btn4,)
    return markup


async def transaction() -> InlineKeyboardMarkup:
    # =============== 🗃 Transaction History ===============
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="📥 История пополнений", callback_data="history_deposit")
    btn2 = InlineKeyboardButton(text="📤 История отправок", callback_data="history_send")
    btn3 = InlineKeyboardButton(text="🔀 История трансферов", callback_data="history_transfer")
    btn4 = InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    markup.add(btn1, btn2, btn3, btn4)
    return markup

