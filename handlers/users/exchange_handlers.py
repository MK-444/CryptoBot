# aiogram
from aiogram.dispatcher.filters import Text
from aiogram.types import  CallbackQuery
from aiogram import Bot, Dispatcher, executor, types 
from aiogram.types import ReplyKeyboardRemove, ParseMode
from aiogram.dispatcher import FSMContext
from aiogram.types.message import ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# python libraries
import logging 
import pyotp
import os 

# pip install libraries
from py_currency_converter import convert
from pycoingecko import CoinGeckoAPI
from dotenv import load_dotenv

# import files
from aiogram import types
from aiogram.dispatcher.filters import Command
from aiogram.dispatcher import FSMContext
from aiogram.types import ParseMode

from keyboards.inline.exchange_inline import *
from keyboards.inline.wallet_inline import *
from keyboards.inline.base_inline import *
from keyboards.inline.settings_inline import *
from keyboards.inline.info_inline import *
from keyboards.default.default import *
from functions.message import *
from utils.db_api.db_commands import *
from loader import dp
from states.state import *
from functions.binance_price import * 

    
import uuid
import datetime
import datetime
import pytz


id_transaction = uuid.uuid4().hex[:9]
cg = CoinGeckoAPI()


# ========================== 💱 Exchange ========================
@dp.message_handler(Text(equals='💱 Exchange'))
async def exchange(message: types.Message):
    price = cg.get_price(ids='bitcoin', vs_currencies='usd')
    await message.answer(msc, reply_markup=await exchange_buttons(), parse_mode=types.ParseMode.MARKDOWN)


@dp.callback_query_handler(text='swap')
async def exhange_inline(callback: types.CallbackQuery):
    """========= 💱 Exchange ==========="""
    await callback.message.answer(msc, reply_markup=await exchange_buttons(), parse_mode=types.ParseMode.MARKDOWN)


# ========================== 📈 Buy ========================
@dp.callback_query_handler(text='buy')
async def buy(callback: types.CallbackQuery):
    """========= 📈 Купить ==========="""
    await callback.message.answer('Выбрано: *📈 Купить*',reply_markup=ReplyKeyboardRemove(), parse_mode=types.ParseMode.MARKDOWN)
    await callback.message.answer('Выберите валюту, которую хотите купить\n минимальная сумма = *45$*:', reply_markup=await buy_btn(), parse_mode=types.ParseMode.MARKDOWN)
    await ExchangeBuy.exchange_buy.set()


# ======================== 📈 Buy -> Crypto =================
@dp.callback_query_handler(lambda c: True, state=ExchangeBuy.exchange_buy)
async def exchange_usd(callback: types.CallbackQuery):
    """========= 📈 Buy -> Crypto ==========="""
    data = callback.data
    if data in cryptocurrency.keys():
        global buy_cryptocurrency
        buy_cryptocurrency = cryptocurrency[data]
        await callback.message.answer(f'Выбрано: *{buy_cryptocurrency}*', parse_mode=types.ParseMode.MARKDOWN)

        markup = InlineKeyboardMarkup(row_width=1)
        btn1 = InlineKeyboardButton(text=f"USD -> {cryptocurrency[data]}", callback_data="usd")
        btn2 = InlineKeyboardButton(text=f"Bitcoin BTC -> {cryptocurrency[data]}", callback_data="btc")
        btn3 = InlineKeyboardButton(text=f"Litecoin LTC -> {cryptocurrency[data]}", callback_data="ltc")
        btn4 = InlineKeyboardButton(text=f"Ethereum ETH -> {cryptocurrency[data]}", callback_data="eth")
        btn5 = InlineKeyboardButton(text=f"AAVE -> {cryptocurrency[data]}", callback_data="aave")
        btn6 = InlineKeyboardButton(text=f"APE-(ApeCoin, ERC20) -> {cryptocurrency[data]}", callback_data="ape")
        btn7 = InlineKeyboardButton(text=f"Tether USDT ERC20 -> {cryptocurrency[data]}", callback_data="usdt")
        btn8 = InlineKeyboardButton(text=f"USDC ERC20 -> {cryptocurrency[data]}", callback_data="usdc")
        btn9 = InlineKeyboardButton(text=f"COMP-Compound, ERC20 -> {cryptocurrency[data]}", callback_data="comp")
        btn10 = InlineKeyboardButton(text=f"CRV-Curve DAO Token ERC20 -> {cryptocurrency[data]}", callback_data="crv")
        btn11 = InlineKeyboardButton(text=f"DAI -> {cryptocurrency[data]}", callback_data="dai")
        btn12 = InlineKeyboardButton(text=f"Dogecoin (Doge) -> {cryptocurrency[data]}", callback_data="doge")
        btn13 = InlineKeyboardButton(text=f"Ethereum Classic #1 -> {cryptocurrency[data]}", callback_data="eth_clasic")
        btn14 = InlineKeyboardButton(text=f"Gala -> {cryptocurrency[data]}", callback_data="gala")
        btn15 = InlineKeyboardButton(text=f"CHZ-chiliZ -> {cryptocurrency[data]}", callback_data="chz")
        btn16 = InlineKeyboardButton(text=f"LINK, CHAIN LINK ERC20 -> {cryptocurrency[data]}", callback_data="link")
        btn17 = InlineKeyboardButton(text=f"Near Protocol ERC20 -> {cryptocurrency[data]}", callback_data="near")
        btn18 = InlineKeyboardButton(text=f"Pax Dollar USDP -> {cryptocurrency[data]}", callback_data="usdp")
        btn19 = InlineKeyboardButton(text=f"SNX (Synthetix ,ERC20) -> {cryptocurrency[data]}", callback_data="snx")
        btn20 = InlineKeyboardButton(text=f"SUSHI-SushiToken, ERC20 -> {cryptocurrency[data]}", callback_data="sushi")
        btn21 = InlineKeyboardButton(text=f"UNI-Uniswap ERC20 -> {cryptocurrency[data]}", callback_data="uni")
        btn22 = InlineKeyboardButton(text=f"USDC USD COIN ERC2O -> {cryptocurrency[data]}", callback_data="usdc-usd")
        btn23 = InlineKeyboardButton(text=f"WBTC-Wrapped BTC (ERC20) -> {cryptocurrency[data]}", callback_data="wbtc")
        btn24 = InlineKeyboardButton(text=f"YFI-yearn.finance, ERC20 -> {cryptocurrency[data]}", callback_data="yfi")
        btn25 = InlineKeyboardButton(text=f"USD COIN (USDC ERC20) -> {cryptocurrency[data]}", callback_data="usd-coin")
        markup.row(btn1, btn2).row(btn3, btn4).row(btn5, btn6).row(btn7, btn8).row(btn9, btn10).row(btn11, btn12).row(btn13, btn14).row(btn15, btn16).row(btn17, btn18).row(btn19, btn20).row(btn21, btn22).row(btn23, btn24).add(btn25)
        await callback.message.answer(f'Выберите направление обмена:', reply_markup=markup)
        await ExchangeBuy.next()
        
        
# ========= 📈 Buy -> Crypto -> Crypto to Crypto ===========
@dp.callback_query_handler(lambda c: True, state=ExchangeBuy.crypto_crypto)
async def eth_btc(callback: types.CallbackQuery):
    """========= 📈 Buy -> Crypto -> Crypto to Crypto ==========="""
    data = callback.data
    if data in cryptocurrency.keys():
        global buy_to_cryptocurrency 
        buy_to_cryptocurrency = cryptocurrency[data]
        await callback.message.answer(f'Выбрано: *{buy_to_cryptocurrency} -> {buy_cryptocurrency}*', parse_mode=types.ParseMode.MARKDOWN)
    await ExchangeBuy.exchange_price.set()
    await callback.message.answer('Введите сумму которую хотите купить \n Min: *45$*', parse_mode=types.ParseMode.MARKDOWN)
    
    
# ========= 📈 Buy -> Crypto -> Crypto to Crypto -> confirm
@dp.message_handler(state=ExchangeBuy.exchange_price)
async def give_usd(message: types.Message, state: FSMContext):
    """========= 📈 Buy -> Crypto -> Crypto to Crypto -> confirm ======="""
    global btc_amount
    btc_amount = message.text
    try:
        if int(btc_amount) >= 45:
            global eth_amount 
            eth_amount = float(btc_amount)*price_from_binance
            
            exchange_process = f"Зачисление: *{btc_amount} {buy_cryptocurrency}*\n\
Списание: *{'{:.2f}'.format(eth_amount)} {buy_to_cryptocurrency}*"

            await message.answer(exchange_process, reply_markup=await confirm_btn(), parse_mode=types.ParseMode.MARKDOWN)
            await ExchangeBuy.right_buy.set()
        else:
            await message.answer('Minimum 45')
    except:
        print('Неправильная сумма')

# Set the date UTC
dt = datetime.datetime.utcnow().replace(tzinfo=pytz.UTC)

# Convert to UTC+1
utc_plus_1 = pytz.timezone('Europe/Paris')
dt = dt.astimezone(utc_plus_1)

dt_str = dt.strftime("%d.%m.%Y, %H.%M.%S")

print(dt_str)

# ========= 📈 Buy -> Crypto -> Crypto to Crypto -> confirm -> everything is right ===========
@dp.callback_query_handler(text='right', state=ExchangeBuy.right_buy)
async def buy_end(callback: types.CallbackQuery, state:FSMContext):
    """========= 📈 Купить -> Crypto -> Crypto to Crypto -> confirm -> everything is right ==========="""
    await callback.message.answer(f"Обмен: *{buy_cryptocurrency} -> {buy_to_cryptocurrency}* \n\
ID: {id_transaction}\n\
\n\
Статус: 🕐 Открыт\n\
\n\
Зачисление: *{btc_amount} {buy_cryptocurrency}*\n\
Списание: *{'{:.2f}'.format(eth_amount)} {buy_to_cryptocurrency}*\n\
\n\
Создан: {dt_str} UTC+1\n\
", parse_mode=types.ParseMode.MARKDOWN, reply_markup=await confirm_btn())
    await ExchangeBuy.all_right.set()
    
# =================== All right 👌🏻 ==================
@dp.callback_query_handler(text='right', state=ExchangeBuy.all_right)
async def all_right(callback: types.CallbackQuery, state:FSMContext):
    await callback.message.answer('✅ Сохранено')
    await callback.message.answer(msc, reply_markup=await wallet_buttons()) 
    await state.finish()


# ========================== 📉 Sell ========================
@dp.callback_query_handler(text='sell')
async def buy(callback: types.CallbackQuery):
    """==================== 📉 Sell ====================="""
    await callback.message.answer('Выбрано: *📉 Продать*',reply_markup=ReplyKeyboardRemove(), parse_mode=types.ParseMode.MARKDOWN)
    await callback.message.answer('Выберите валюту, которую хотите продать\n минимальная сумма = *50$*:', reply_markup=await buy_btn(), parse_mode=types.ParseMode.MARKDOWN)
    await ExchangeSell.exchange_sell.set()
    

# ========= 📉 Sell -> Crypto ===========
@dp.callback_query_handler(lambda c: True, state=ExchangeSell.exchange_sell)
async def exchange_usd(callback: types.CallbackQuery):
    """========= 📉 Sell -> Crypto ==========="""
    data = callback.data
    if data in cryptocurrency.keys():
        global sell_cryptocurrency 
        sell_cryptocurrency = cryptocurrency[data]
        await callback.message.answer(f'Выбрано: *{sell_cryptocurrency}*', parse_mode=types.ParseMode.MARKDOWN)

        markup = InlineKeyboardMarkup(row_width=1)
        btn1 = InlineKeyboardButton(text=f"USD -> {cryptocurrency[data]}", callback_data="usd")
        btn2 = InlineKeyboardButton(text=f"Bitcoin BTC -> {cryptocurrency[data]}", callback_data="btc")
        btn3 = InlineKeyboardButton(text=f"Litecoin LTC -> {cryptocurrency[data]}", callback_data="ltc")
        btn4 = InlineKeyboardButton(text=f"Ethereum ETH -> {cryptocurrency[data]}", callback_data="eth")
        btn5 = InlineKeyboardButton(text=f"AAVE -> {cryptocurrency[data]}", callback_data="aave")
        btn6 = InlineKeyboardButton(text=f"APE-(ApeCoin, ERC20) -> {cryptocurrency[data]}", callback_data="ape")
        btn7 = InlineKeyboardButton(text=f"Tether USDT ERC20 -> {cryptocurrency[data]}", callback_data="usdt")
        btn8 = InlineKeyboardButton(text=f"USDC ERC20 -> {cryptocurrency[data]}", callback_data="usdc")
        btn9 = InlineKeyboardButton(text=f"COMP-Compound, ERC20 -> {cryptocurrency[data]}", callback_data="comp")
        btn10 = InlineKeyboardButton(text=f"CRV-Curve DAO Token ERC20 -> {cryptocurrency[data]}", callback_data="crv")
        btn11 = InlineKeyboardButton(text=f"DAI -> {cryptocurrency[data]}", callback_data="dai")
        btn12 = InlineKeyboardButton(text=f"Dogecoin (Doge) -> {cryptocurrency[data]}", callback_data="doge")
        btn13 = InlineKeyboardButton(text=f"Ethereum Classic #1 -> {cryptocurrency[data]}", callback_data="eth_clasic")
        btn14 = InlineKeyboardButton(text=f"Gala -> {cryptocurrency[data]}", callback_data="gala")
        btn15 = InlineKeyboardButton(text=f"CHZ-chiliZ -> {cryptocurrency[data]}", callback_data="chz")
        btn16 = InlineKeyboardButton(text=f"LINK, CHAIN LINK ERC20 -> {cryptocurrency[data]}", callback_data="link")
        btn17 = InlineKeyboardButton(text=f"Near Protocol ERC20 -> {cryptocurrency[data]}", callback_data="near")
        btn18 = InlineKeyboardButton(text=f"Pax Dollar USDP -> {cryptocurrency[data]}", callback_data="usdp")
        btn19 = InlineKeyboardButton(text=f"SNX (Synthetix ,ERC20) -> {cryptocurrency[data]}", callback_data="snx")
        btn20 = InlineKeyboardButton(text=f"SUSHI-SushiToken, ERC20 -> {cryptocurrency[data]}", callback_data="sushi")
        btn21 = InlineKeyboardButton(text=f"UNI-Uniswap ERC20 -> {cryptocurrency[data]}", callback_data="uni")
        btn22 = InlineKeyboardButton(text=f"USDC USD COIN ERC2O -> {cryptocurrency[data]}", callback_data="usdc-usd")
        btn23 = InlineKeyboardButton(text=f"WBTC-Wrapped BTC (ERC20) -> {cryptocurrency[data]}", callback_data="wbtc")
        btn24 = InlineKeyboardButton(text=f"YFI-yearn.finance, ERC20 -> {cryptocurrency[data]}", callback_data="yfi")
        btn25 = InlineKeyboardButton(text=f"USD COIN (USDC ERC20) -> {cryptocurrency[data]}", callback_data="usd-coin")
        markup.row(btn1, btn2).row(btn3, btn4).row(btn5, btn6).row(btn7, btn8).row(btn9, btn10).row(btn11, btn12).row(btn13, btn14).row(btn15, btn16).row(btn17, btn18).row(btn19, btn20).row(btn21, btn22).row(btn23, btn24).add(btn25)
        await callback.message.answer(f'Выберите направление обмена:', reply_markup=markup)
        await ExchangeSell.next()


# ========= 📉 Sell -> Crypto -> Crypto to Crypto ===========
@dp.callback_query_handler(lambda c: True, state=ExchangeSell.crypto_crypto_sell)
async def eth_btc(callback: types.CallbackQuery):
    """========= 📉 Sell -> Crypto -> Crypto to Crypto ==========="""
    data = callback.data
    if data in cryptocurrency.keys():
        global sell_to_cryptocurrency 
        sell_to_cryptocurrency = cryptocurrency[data]
        await callback.message.answer(f'Выбрано: *{sell_to_cryptocurrency} -> {sell_cryptocurrency}*', parse_mode=types.ParseMode.MARKDOWN)
    await ExchangeSell.exchange_price_sell.set()
    await callback.message.answer('Введите сумму которую хотите продать \n Min: *50$*', parse_mode=types.ParseMode.MARKDOWN)
    
    
# ========= 📉 Sell -> Crypto -> Crypto to Crypto -> confirm =======
@dp.message_handler(state=ExchangeSell.exchange_price_sell)
async def give_usd(message: types.Message, state: FSMContext):
    """========= 📉 Sell -> Crypto -> Crypto to Crypto -> confirm ======="""
    global btc_amount
    btc_amount = message.text
    try:
        if int(btc_amount) >= 50:
            global eth_amount
            eth_amount = float(btc_amount)*price_from_binance
            exchange_process = f"Зачисление: *{btc_amount} {sell_cryptocurrency}*\n\
Списание: *{'{:.2f}'.format(eth_amount)} {sell_to_cryptocurrency}*\n\
        "
            await message.answer(exchange_process, reply_markup=await confirm_btn(), parse_mode=types.ParseMode.MARKDOWN)
            await ExchangeSell.right_sell.set()
        else:
            await message.answer('Minimum 50')
    except:
        print('Неправильная сумма')
        
    


# ========= 📉 Sell -> Crypto -> Crypto to Crypto -> confirm -> everything is right ===========
@dp.callback_query_handler(text='right', state=ExchangeSell.right_sell)
async def eth_btc(callback: types.CallbackQuery, state:FSMContext):
    """========= 📉 Sell -> Crypto -> Crypto to Crypto -> confirm -> everything is right ==========="""
    await callback.message.answer(f"Обмен: *{sell_cryptocurrency} -> {sell_to_cryptocurrency}* \n\
ID: {id_transaction}\n\
\n\
Статус: 🕐 Открыт\n\
\n\
Зачисление: *{btc_amount} {sell_cryptocurrency}*\n\
Списание: *{'{:.2f}'.format(eth_amount)} {sell_to_cryptocurrency}*\n\
\n\
Создан: {dt_str} UTC+1\n\
", parse_mode=types.ParseMode.MARKDOWN, reply_markup=await confirm_btn())
    await ExchangeSell.all_right.set()
    
    
# =================== All right 👌🏻 ==================
@dp.callback_query_handler(text='right', state=ExchangeSell.all_right)
async def all_right(callback: types.CallbackQuery, state:FSMContext):
    """========  ========"""
    await callback.message.answer('✅ Сохранено')
    await callback.message.answer(msc, reply_markup=await wallet_buttons()) 
    # await callback.message.edit_reply_markup(reply_markup=None)
    await state.finish()


#========================= 🔀 Transaction History ======================
@dp.callback_query_handler(text='history')
async def get_history(callback: types.CallbackQuery):
    pass



cryptocurrency = {
        'btc': 'Bitcoin BTC',
        'ltc': 'Litecoin LTC',
        'eth': 'Ethereum ETH',
        'aave':'AAVE',
        'ape':'APE-(ApeCoin, ERC20)',
        'usdt':'Tether USDT ERC20',
        'usdc':'USDC ERC20',
        'comp':'COMP-Compound, ERC20',
        'crv':'CRV-Curve DAO Token ERC20',
        'dai': 'DAI',
        'doge':'Dogecoin (Doge)',
        'eth_clasic':'Ethereum Classic #1',
        'gala':'Gala',
        'chz':'CHZ-chiliZ',
        'link':'LINK, CHAIN LINK ERC20',
        'near':'Near Protocol ERC20',
        'usdp':'Pax Dollar USDP',
        'snx':'SNX (Synthetix ,ERC20)',
        'sushi':'SUSHI-SushiToken, ERC20',
        'uni':'UNI-Uniswap ERC20',
        'usdc-usd':'USDC USD COIN ERC2O',
        'wbtc':'WBTC-Wrapped BTC (ERC20)',
        'yfi':'YFI-yearn.finance, ERC20',
        'usd-coin':'USD COIN (USDC ERC20)'
    }


#====================================================

confirm_send = "Подтвердите сумму или укажите другую.\n\
Доступный баланс:<balans><crypto>\n\
\n\
Перевод: <suma><crypto>\n\
UID получателя: <uid>"


end_send = "Трансфер: #<crypto>\n\
ID: #<random_symbol>\n\
\n\
Статус: <status, Завершен>\n\
\n\
UID получателя: <uid>\n\
Сумма отправки: <suma><crypto>\n\
\n\
Создан: <datetime>\n\
Завершен: <datetime>"

