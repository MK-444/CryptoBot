from aiogram.types import ReplyKeyboardMarkup, KeyboardButton



async def keyboard():
    """========= Menu ===========
    When you click on one of these buttons 
    you will go the way of the inline buttons
    """
    markup = ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = KeyboardButton(text="👝 Wallet")# -> path/inline/wallet_inline
    btn2 = KeyboardButton(text="💱 Exchange")# -> path/inline/exchange_inline
    btn3 = KeyboardButton(text="⚙️ Settings")# -> path/inline/settings_inline
    btn4 = KeyboardButton(text="ℹ️ Info")# -> path/inline/info_inline
    # btn5 = KeyboardButton(text = 'Web version', url='http://127.0.0.1:8000/items{id}')
    markup.row(btn1, btn2)
    markup.row(btn3, btn4)
    # markup.add(btn5)
    return markup


