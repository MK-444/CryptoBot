from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


# ========================== 👝 Wallet ========================
async def wallet_buttons() -> InlineKeyboardMarkup:
    markup = InlineKeyboardMarkup(row_width=1, one_time_keyboard=True)
    btn1 = InlineKeyboardButton(text="📥 Пополнить",callback_data='deposit')
    btn2 = InlineKeyboardButton(text="📤 Вывести", callback_data='send')
    btn3 = InlineKeyboardButton(text="💱 Обмен", callback_data='swap')
    btn4 = InlineKeyboardButton(text="⤴️ Отправить пользователю",callback_data='send_to_user')
    btn5 = InlineKeyboardButton(text="🗃 История транзакций",callback_data='history')
    btn6 = InlineKeyboardButton(text="🎁 Активировать промокод",callback_data='promo_code')
    markup.row(btn1, btn2).add(btn3, btn4, btn5, btn6)
    return markup

async def buy_btn() -> InlineKeyboardMarkup:
    """📥 Deposit"""
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="USD", callback_data="usd")
    btn2 = InlineKeyboardButton(text="Bitcoin BTC", callback_data="btc")
    btn3 = InlineKeyboardButton(text="Litecoin LTC", callback_data="ltc")
    btn4 = InlineKeyboardButton(text="Ethereum ETH", callback_data="eth")
    btn5 = InlineKeyboardButton(text="AAVE", callback_data="aave")
    btn6 = InlineKeyboardButton(text="APE-(ApeCoin, ERC20)", callback_data="ape")
    btn7 = InlineKeyboardButton(text="Tether USDT ERC20", callback_data="usdt")
    btn8 = InlineKeyboardButton(text="USDC ERC20", callback_data="usdc")
    btn9 = InlineKeyboardButton(text="COMP-Compound, ERC20", callback_data="comp")
    btn10 = InlineKeyboardButton(text="CRV-Curve DAO Token ERC20", callback_data="crv")
    btn11 = InlineKeyboardButton(text="DAI", callback_data="dai")
    btn12 = InlineKeyboardButton(text="Dogecoin (Doge)", callback_data="doge")
    btn13 = InlineKeyboardButton(text="Ethereum Classic #1", callback_data="eth_clasic")
    btn14 = InlineKeyboardButton(text="Gala", callback_data="gala")
    btn15 = InlineKeyboardButton(text="CHZ-chiliZ", callback_data="chz")
    btn16 = InlineKeyboardButton(text="LINK, CHAIN LINK ERC20", callback_data="link")
    btn17 = InlineKeyboardButton(text="Near Protocol ERC20", callback_data="near")
    btn18 = InlineKeyboardButton(text="Pax Dollar USDP", callback_data="usdp")
    btn19 = InlineKeyboardButton(text="SNX (Synthetix ,ERC20)", callback_data="snx")
    btn20 = InlineKeyboardButton(text="SUSHI-SushiToken, ERC20", callback_data="sushi")
    btn21 = InlineKeyboardButton(text="UNI-Uniswap ERC20", callback_data="uni")
    btn22 = InlineKeyboardButton(text="USDC USD COIN ERC2O", callback_data="usdc-usd")
    btn23 = InlineKeyboardButton(text="WBTC-Wrapped BTC (ERC20)", callback_data="wbtc")
    btn24 = InlineKeyboardButton(text="YFI-yearn.finance, ERC20", callback_data="yfi")
    btn25 = InlineKeyboardButton(text="USD COIN (USDC ERC20)", callback_data="usd-coin")
    markup.row(btn1, btn2).row(btn3, btn4).row(btn5, btn6).row(btn7, btn8).row(btn9, btn10).row(btn11, btn12).row(btn13, btn14).row(btn15, btn16).row(btn17, btn18).row(btn19, btn20).row(btn21, btn22).row(btn23, btn24).add(btn25)
    return markup

async def get_usd()-> InlineKeyboardMarkup:
    """📥 Deposit -> USD"""
    markup = InlineKeyboardMarkup(row_width=1)
    btn2 = InlineKeyboardButton(text="CZK -> USD", callback_data="czk")
    btn3 = InlineKeyboardButton(text="Банковский перевод в рамках Чехии", callback_data="banking")
    btn4 = InlineKeyboardButton(text="IBAN + BIC/SWIFT  + SEPA ", callback_data="iban")
    btn5 = InlineKeyboardButton(text="Наличные", callback_data="nalichka")
    btn6 = InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    markup.add(btn2, btn3, btn4, btn5, btn6)
    return markup

async def get_pay() -> InlineKeyboardMarkup:
    """📥 Replenish -> USD -> CZK - USD"""
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="Сумма отдаю", callback_data="give")
    btn2 = InlineKeyboardButton(text="Сумма получаю", callback_data="get")
    markup.add(btn1, btn2)
    return markup

async def get_btc() -> InlineKeyboardMarkup:
    """📥 Deposit -> BTC"""
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="Получить адрес кошелька", callback_data="confirm_send")
    btn2 = InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")
    markup.add(btn1, btn2)
    return markup


async def get_credit_card() -> InlineKeyboardMarkup:
    """📥 Deposit -> USDT"""
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="Visa/Master", callback_data="master")
    btn2 = InlineKeyboardButton(text="Visa/Master P24", callback_data="masterp24")
    btn3 = InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    markup.add(btn1, btn2, btn3)
    return markup


async def give_btc() -> InlineKeyboardMarkup:
    """Withdraw -> USDT"""
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="BTC Bitcoin", callback_data="send_btc")
    btn2 = InlineKeyboardButton(text="USD", callback_data="cach")
    btn3 = InlineKeyboardButton(text="◀️ Назад", callback_data="back")
    markup.add(btn1, btn2, btn3)
    return markup



