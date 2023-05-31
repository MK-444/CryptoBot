from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# =================== right 👌🏻  ==================
async def confirm_btn() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text='Верно 👌🏻', callback_data='right')
    btn2 = InlineKeyboardButton(text="✖️ Отмена", callback_data="back")
    markup.row(btn1, btn2)
    return markup

# =================== All right 👌🏻 ==================
async def all_right_btn() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text='Всё верно 👌🏻', callback_data='all_right')
    btn2 = InlineKeyboardButton(text="✖️ Отмена", callback_data="back")
    markup.row(btn1, btn2)
    return markup

# ==================== ✖️ Cancel ==============
async def cancel_btn() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")
    markup.row(btn1)
    return markup

# ============ ◀️ Back ==================
async def back_btn() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    markup.row(btn1)
    return markup