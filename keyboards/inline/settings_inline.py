from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton



# ========================== ⚙️ Settings ========================
async def settings_buttons() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="👅 Язык / Language", callback_data="language")
    btn2 = InlineKeyboardButton(text="🔒 2FA", callback_data="fa2")
    btn3 = InlineKeyboardButton(text="👤 Мой UID", callback_data="uid")
    btn4 = InlineKeyboardButton(text="💠 Активировать промокод", callback_data="activate_promocod")
    markup.add(btn1, btn2, btn3, btn4,)
    return markup

async def fa2_btn() -> InlineKeyboardMarkup:
    """🔒2FA"""
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="Добавить 2FA", callback_data="twofactory")
    btn2 = InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    markup.add(btn1, btn2)
    return markup


# ================ 🎁 Activate promo code ==========
async def promokod() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    btn2 = InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")
    markup.add(btn1, btn2)
    return markup

