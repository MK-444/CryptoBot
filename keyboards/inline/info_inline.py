from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# ========================== ℹ️ Info ========================
async def info_buttons() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="🔗 Комиссии", callback_data="fees")
    btn2 = InlineKeyboardButton(text="💸 Реферальная программа", callback_data="referal")
    btn3 = InlineKeyboardButton(text="📖 Правила", callback_data="rules", url="https://drive.google.com/file/d/1lRZzth4lLowX5izRbDq3ajD71j30oN2e/view?usp=sharing")
    btn4 = InlineKeyboardButton(text="🗿❔ FAQ", callback_data="faq", url="https://telegra.ph/FAQ-08-26-9")
    btn5 = InlineKeyboardButton(text="📄 Инструкция по использованию бота", callback_data="guide", url="https://telegra.ph/Bot-Guide-08-24")
    btn6 = InlineKeyboardButton(text="💬 Поддержка", callback_data="support", url="https://web.telegram.org/k/#@mkostenko444")
    markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
    return markup

# ================= 🔗 Commissions ==========
async def komisie_btn() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="📥 Пополнение", callback_data="deposit_fees")
    btn2 = InlineKeyboardButton(text="📤 Вывод", callback_data="output_fees")
    btn3 = InlineKeyboardButton(text="💱 Обмен", callback_data="swap")
    btn4 = InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    markup.add(btn1, btn2, btn3, btn4)
    return markup

# ================= 💸 Referral program ==========
async def referal_btn() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="Описание", callback_data="description")
    btn2 = InlineKeyboardButton(text="Моя статистика", callback_data="statistic")
    btn3 = InlineKeyboardButton(text="Мои инвайты", callback_data="invait")
    btn4 = InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    markup.add(btn1, btn2, btn3, btn4)
    return markup


