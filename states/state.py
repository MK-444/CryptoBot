from aiogram.dispatcher.filters.state import StatesGroup, State


class Usd(StatesGroup):
    """========== USD State =========="""
    give = State()
    get = State()  
    cancel = State()

class ProfileStatesGroup(StatesGroup):
    """========== 🔒 2FA State =========="""
    name = State()
    confirm = State()
    six_digit_code = State()


class Buy(StatesGroup):
    buy_confirm = State()
    qrcode = State()
    
class Sell(StatesGroup):
    sell_confirm = State()
    
    
class Send(StatesGroup):
    send = State()
    get_method = State()
    get_address = State()
    right_confirm = State()
    send_pay = State()
    send_give = State()
    send_get = State()
    end_right = State()
    send_usd = State()
    send_usd_banking = State()
    all_right = State()
    

class ExchangeBuy(StatesGroup):
    exchange_buy = State()
    crypto_crypto = State()
    exchange_price = State()
    right_buy = State()
    all_right = State()

    
    
class ExchangeSell(StatesGroup):
    exchange_sell = State()
    crypto_crypto_sell = State()
    exchange_price_sell = State()
    right_sell = State()
    all_right = State()

