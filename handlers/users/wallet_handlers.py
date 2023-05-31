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
from functions import *
from states.state import *
from loader import dp, bot
from utils.db_api import db_commands
import uuid

# from aiogram.contrib.middlewares.i18n import I18nMiddleware
# from pathlib import Path


# BASE_DIR = Path(__file__).parent
# I18N_DOMAIN = 'cryptobot'
# LOCALES_DIR = BASE_DIR / 'locales'
# i18n = I18nMiddleware(I18N_DOMAIN, LOCALES_DIR)
# dp.middleware.setup(i18n)
# _ = i18n.gettext

id_transaction = uuid.uuid4().hex[:9]


# ========================== 👝 Wallet ========================
@dp.message_handler(Text(equals='👝 Wallet'))
async def deposit_wallet(message: types.Message):
    await bot.delete_message(message.from_user.id, message.message_id)
    await message.answer(msc, reply_markup=await wallet_buttons()) 

# =============== 📥 Deposit ============
@dp.callback_query_handler(text='deposit')
async def deposit(callback: types.CallbackQuery):
    """=============== 📥 Deposit ============"""
    await callback.message.answer('Выбрано: 📥Пополнить')
    await callback.message.answer('Выберите валюту, которую хотите пополнить', reply_markup=await buy_btn())
    await Buy.buy_confirm.set()


# =========== 📥 Пополнить -> USD ==============
@dp.callback_query_handler(text='usd', state=Buy.buy_confirm)
async def deposit_usd(callback: types.CallbackQuery, state: FSMContext):
    """=========== 📥 Deposti -> USD =============="""
    await callback.message.answer("Выбрано: *USD*", parse_mode=types.ParseMode.MARKDOWN)
    await callback.message.answer(usd, reply_markup=await get_usd())

    
    
    
# ======== 📥 Deposit -> USD -> CZK - USD ===========
@dp.callback_query_handler(text='czk', state="*")
async def deposit_czk(callback: types.CallbackQuery, state: FSMContext):
    """======== 📥 Deposit -> USD -> CZK - USD ========"""
    await callback.message.answer('Выбрано: *CZK -> USD*', parse_mode=types.ParseMode.MARKDOWN)
    await callback.message.answer(f'Выберите в чем удобнее вводить сумму:', reply_markup= await get_pay(), parse_mode=types.ParseMode.MARKDOWN)
    

# =========== 📥 Deposit -> USD -> CZK - USD -> The amount I give =======
@dp.callback_query_handler(text='give', state="*")
async def give_usd_czk(callback: types.CallbackQuery, state: FSMContext):
    """=========== 📥 Deposit -> USD -> CZK - USD -> The amount I give ======="""
    await Usd.give.set()
    await callback.message.answer(czk_give, reply_markup= await cancel_btn())
    
    
# ========= The amount I give=======
@dp.message_handler(state=Usd.give)
async def give_usd(message: types.Message, state: FSMContext):
    """========= The amount I give ======="""
    global your_amount
    your_amount = message.text
    try:
        if int(your_amount) >= 2500:
            currency_give = 'CZK'
            currency_get = 'USD'
            global currency
            currency = float(float(your_amount) / float(value))
            deposit_process = f"Депозит #USD создан!\n\
ID: #{id_transaction}\n\
\n\
Статус: Обрабатывается 🌀\n\
\n\
Сумма отдаю: *{your_amount} {currency_give}* \n\
Сумма получаю: *{'{:.2f}'.format(currency)} {currency_get}*\n\
Комиссия: 25 CZK\n\
\n\
Метод:\n\
    `2502061515/2010` из чехии,\n\
    IBAN:`CZ5620100000002002416156`\n\
    BIC/SWIFT:`FIOBCZPPXXX`"
            await message.answer(deposit_process, reply_markup=await all_right_btn(), parse_mode=types.ParseMode.MARKDOWN)
        else:
            await message.answer('Minimum 2500')
    except:
        print('Неправильная сумма')
        

    
# ==================== ✖️ Cancel ==============
@dp.callback_query_handler(text='cancel', state=Usd.cancel)
async def cancel(callback: types.CallbackQuery, state:FSMContext):
    await callback.message.answer(msc, reply_markup=await wallet_buttons())
    

# =================== Right👌🏻 ==================
@dp.callback_query_handler(text='right', state=Send.right_confirm)
async def deposit_czk(callback: types.CallbackQuery, state: FSMContext):
    """======== Right👌🏻 ========"""
    await callback.message.answer(f'Выберите в чем удобнее вводить сумму:', reply_markup= await get_pay())
    await Send.send_pay.set()


# ======== 📥 Deposit -> USD -> CZK - USD -> The amount I get =========
@dp.callback_query_handler(text='get', state="*")
async def get_money(callback: types.CallbackQuery, state: FSMContext):
    """======== 📥 Пополнить -> USD -> CZK - USD -> The amount I get ========="""
    await Usd.get.set()
    await callback.message.answer(usd_get, reply_markup= await cancel_btn())

# ======== The amount I get =========
@dp.message_handler(state=Usd.get)
async def get_money_usd(message: types.Message, state: FSMContext):
    """======== The amount I get ========="""
    your_amount = message.text
    try: 
        if int(your_amount) >= 100:
            currency_give = 'USD'
            currency_get = 'CZK'
            currency = float(float(your_amount) * float(value))
            deposit_process = f"Депозит #USD создан!\n\
ID: #{id_transaction}\n\
\n\
Статус: Обрабатывается 🌀\n\
\n\
Сумма получаю: *{your_amount} {currency_give}* \n\
Сумма отдаю: *{'{:.2f}'.format(currency)} {currency_get}*\n\
Комиссия: 25 CZK\n\
\n\
Метод:\n\
    `2502061515/2010` из чехии,\n\
    IBAN:`CZ5620100000002002416156`\n\
    BIC/SWIFT:`FIOBCZPPXXX`"
            await message.answer(deposit_process, reply_markup=await all_right_btn(), parse_mode=types.ParseMode.MARKDOWN)
        else:
            await message.answer('Minimum 100')
    except:
        print('Неправильная сумма')



# ========== 📥 Deposit -> USD -> Bank transfer in the Czech Republic =======
@dp.callback_query_handler(text='banking', state="*")
async def deposit_banking(callback: types.CallbackQuery, state:FSMContext):
    """========== 📥 Пополнить -> USD -> Bank transfer in the Czech Republic ======="""
    await callback.message.answer('Выбрано: *Банковский перевод в рамках Чехии*', parse_mode=types.ParseMode.MARKDOWN)
    # await callback.message.answer(online_banking, reply_markup=await get_pay())
    await callback.message.answer(f'Выберите в чем удобнее вводить сумму:', reply_markup= await get_pay())
    await callback.message.edit_reply_markup(reply_markup=None)
    
    
    
# ========== 📥 Deposit -> USD -> IBAN + BIC/SWIFT ============
@dp.callback_query_handler(text='iban', state="*")
async def deposit_iban(callback: types.CallbackQuery, state:FSMContext):
    """========== 📥 Пополнить -> USD -> IBAN + BIC/SWIFT ============"""
    await callback.message.answer('Выбрано: *IBAN + BIC/SWIFT*', parse_mode=types.ParseMode.MARKDOWN)
    await callback.message.answer(f'Выберите в чем удобнее вводить сумму:', reply_markup= await get_pay())
  
    
    
    
# ========= 📥 Deposit -> USD -> Cash ===========
@dp.callback_query_handler(text='nalichka', state="*")
async def deposit_cash(callback: types.CallbackQuery, state:FSMContext):
    """========= 📥 Deposit -> USD -> Cash ==========="""
    await callback.message.answer('Выбрано: *Наличные*', parse_mode=types.ParseMode.MARKDOWN)
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="Написать в личку администратору", callback_data="write", url='tg://user?id=430859244')
    btn2 = InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")
    markup.add(btn1, btn2)
    await callback.message.answer(nalichka, reply_markup=markup, parse_mode=types.ParseMode.MARKDOWN)
    await callback.message.edit_reply_markup(reply_markup=None)
    


# ============ 📥 Deposit -> USDT ==========
@dp.callback_query_handler(text='usdt')
async def deposit_usdt(callback: types.CallbackQuery):
    """============ 📥 Deposit -> USDT =========="""
    await callback.message.answer('Выбрано: *USDT*', reply_markup=await get_credit_card(), parse_mode=types.ParseMode.MARKDOWN)
    # await callback.message.answer('Выберите валюту, которую хотите отдать')
    await callback.message.edit_reply_markup(reply_markup=None)
    
    
# ========== 📥 Deposit -> USDT -> Visa/Master ============
@dp.callback_query_handler(text='master')
async def deposit_mastercard(callback: types.CallbackQuery):
    """========== 📥 Deposit -> USDT -> Visa/Master ============"""
    await callback.message.answer('Выбрано: *Visa/Master*', parse_mode=types.ParseMode.MARKDOWN)
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")
    markup.add(btn1)
    await callback.message.answer('In Process 👩‍💻', reply_markup=markup)
    # await callback.message.answer('Выберите в чем удобнее вводить сумму:', reply_markup=await get_pay())
    await callback.message.edit_reply_markup(reply_markup=None)



# ============= 📥 Deposit -> USDT -> Visa/Master P24 ==========
@dp.callback_query_handler(text='masterp24')
async def deposit_mastercardp24(callback: types.CallbackQuery):
    """============= 📥 Deposit -> USDT -> Visa/Master P24 =========="""
    await callback.message.answer('Выбрано: *Visa/Master P24*', parse_mode=types.ParseMode.MARKDOWN)
    markup = InlineKeyboardMarkup(row_width=1)
    btn1 = InlineKeyboardButton(text="✖️ Отмена", callback_data="cancel")
    markup.add(btn1)
    await callback.message.answer('*In Process* 👩‍💻', reply_markup=markup, parse_mode=types.ParseMode.MARKDOWN)
    await callback.message.edit_reply_markup(reply_markup=None)




cryptocurrency = {
        'usd': 'USD',
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



# ============ 📥 Deposit -> BTC ============
@dp.callback_query_handler(lambda c: True, state=Buy.buy_confirm)
async def deposit_btc(callback: types.CallbackQuery):
    """========== 📥 Deposit -> BTC ============"""
    data = callback.data
    if data in cryptocurrency.keys():
        btc_msg = f"\n\
Вы собираетесь пополнить баланс: *{cryptocurrency[data]}*\n\
\n\
Min: *0.001* \n\
Комиссия: *0*\n\
\n\
Метод: *{cryptocurrency[data]}*\n\
\n\
⚠️ Внимание\n\
Средства будут зачислены на ваш баланс после 3 подтверждений\
"
        await callback.message.answer(f'Выбрано: *{cryptocurrency[data]}*', parse_mode=types.ParseMode.MARKDOWN)
        await callback.message.answer(btc_msg, reply_markup=await get_btc(), parse_mode=types.ParseMode.MARKDOWN)
        await Buy.qrcode.set()



# ======= 📥 Deposit -> BTC -> Get a wallet address ==========
@dp.callback_query_handler(text='confirm_send', state=Buy.qrcode)
async def confirm_btc(callback: types.CallbackQuery, state:FSMContext):
    """======= 📥 Deposit -> BTC -> Get a wallet address =========="""
    p = open('./functions/qrcodes/MyQRCode1.png', 'rb')
    await bot.send_photo(callback.from_user.id, photo=p, caption=btc, parse_mode=ParseMode.MARKDOWN)
    await callback.message.edit_reply_markup(reply_markup=None)
    await state.finish()
    
    
    
# ============ 📥 Deposit -> LTC ==============
@dp.callback_query_handler(text='ltc')
async def get_deposit_ltc(callback: types.CallbackQuery):
    """============ 📥 Deposit -> LTC =============="""
    await callback.message.answer('Выбрано: *LTC*', parse_mode=types.ParseMode.MARKDOWN)
    await callback.message.answer('Выбрано: *Litecoin*', parse_mode=types.ParseMode.MARKDOWN)
    await callback.message.answer(deposit_ltc, reply_markup=await get_btc())
    await callback.message.edit_reply_markup(reply_markup=None)
    
    
# ============ 📥 Deposit -> LTC -> confirm ==============
@dp.callback_query_handler(text='confirm_send')
async def confirm_ltc(callback: types.CallbackQuery):
    """============ 📥 Deposit -> LTC -> confirm =============="""
    p = open('MKcryptoBot/functions/qrcodes/MyQRCode1.png', 'rb')
    await bot.send_photo(callback.from_user.id, photo=p, caption=btc, parse_mode=ParseMode.MARKDOWN)
    await callback.message.edit_reply_markup(reply_markup=None)



# ================= 📤 Withdraw  =====================
@dp.callback_query_handler(text='send')
async def send(callback: types.CallbackQuery):
    await callback.message.answer('Выберите валюту, которую хотите отправить:', reply_markup=await buy_btn())
    await Send.send.set()
    
    
# ================= 📤 Withdraw -> Crypto =====================
@dp.callback_query_handler(lambda c: True, state=Send.send)
async def choose_crypto(callback: types.CallbackQuery):
    data = callback.data
    if data in cryptocurrency.keys():
        global send_crypto 
        send_crypto = cryptocurrency[data]
        await callback.message.answer(f'Выбрано: *{send_crypto}*', parse_mode=types.ParseMode.MARKDOWN)
        markup = InlineKeyboardMarkup(row_width=1)
        btn1 = InlineKeyboardButton(text=send_crypto, callback_data="send_crypto")
        btn2 = InlineKeyboardButton(text="Наличные", callback_data="nalichka")
        btn3 = InlineKeyboardButton(text="◀️ Назад", callback_data="back")
        markup = markup.add(btn1, btn2, btn3)
        await callback.message.answer('Выберите метод', reply_markup=markup)
        await Send.get_method.set()


# ================= 📤 Withdraw  -> Crypto -> Crypto/Сash =====================
@dp.callback_query_handler(lambda c: True, state=Send.get_method)
async def method_send(callback: types.CallbackQuery):
    method = {
    'send_crypto':send_crypto,
    'nalichka': 'Наличные'}
    data = callback.data
    if data in method.keys():
        global send_method 
        send_method = method[data]
        await callback.message.answer(f'Выбрано: *{send_method}*', parse_mode=types.ParseMode.MARKDOWN)
        await callback.message.answer('Введите свой кошелек')
        await Send.get_address.set()
        

# ================= 📤 Withdraw -> Crypto -> Wallet =====================
@dp.message_handler(state=Send.get_address)
async def give_usd(message: types.Message, state: FSMContext):
    """================= 📤 Withdraw -> Crypto -> Wallet ====================="""
    global your_address
    your_address = message.text
    try:
        if len(your_address) >= 26:
            send_confirm = f"\n\
Вы собираетесь вывести: *{send_crypto}*\n\
\n\
Min: 0.001 \n\
Комиссия: 0\n\
\n\
Метод: *{send_crypto}*\n\
Адрес: *{your_address}*\n\
\n\
⚠️ Внимание\n\
Средства будут зачислены на ваш баланс после 3 подтверждений"
            await message.answer(send_confirm, reply_markup=await confirm_btn(), parse_mode=types.ParseMode.MARKDOWN)
            await Send.all_right.set()
        else:
            await message.answer('Minimum lenght 26')
    except:
        await message.answer('Попробуй еще')


# =================== Right 👌🏻 ==================
@dp.callback_query_handler(text='right', state=Send.all_right)
async def all_right(callback: types.CallbackQuery, state: FSMContext):
    """========  ========"""
    await callback.message.answer(f'Выберите в чем удобнее вводить сумму:', reply_markup= await get_pay(), parse_mode=types.ParseMode.MARKDOWN)
    await Send.send_pay.set()


# =========== The amount I give =======
@dp.callback_query_handler(text='give', state=Send.send_pay)
async def give_usd_czk(callback: types.CallbackQuery, state: FSMContext):
    """=========== The amount I give ======="""
    await Send.send_give.set()
    await callback.message.answer(czk_give, reply_markup= await cancel_btn())
    
    
# ========= The amount I give =======
@dp.message_handler(state=Send.send_give)
async def give_usd(message: types.Message, state: FSMContext):
    """========= The amount I give ======="""
    global your_amount
    your_amount = message.text
    try:
        if int(your_amount) >= 2500:
            currency_give = 'CZK'
            currency_get = 'USD'
            global currency
            currency = float(float(your_amount) / float(value))
            if send_crypto == 'USD':
                deposit_process = f"Заявка #{send_crypto} на вывод создана!\n\
ID: #{id_transaction}\n\
\n\
Статус: Обрабатывается 🌀\n\
\n\
Сумма отдаю: *{your_amount} {currency_give}* \n\
Сумма получаю: *{'{:.2f}'.format(currency)} {currency_get}*\n\
Комиссия: *25 CZK*\n\
\n\
Метод:\n\
    `2502061515/2010` из чехии,\n\
    IBAN:`CZ34 2010 0000 0025 0206 1515`\n\
    BIC/SWIFT:`FIOBCZPPXXX`"
            else:
                deposit_process = f"Заявка #{send_crypto} на вывод создана!\n\
        ID: #{id_transaction}\n\
        \n\
        Статус: Обрабатывается 🌀\n\
        \n\
        Сумма отдаю: *{your_amount} {currency_give}* \n\
        Сумма получаю: *{'{:.2f}'.format(currency)} {currency_get}*\n\
        Комиссия: 1 *{send_crypto}*\n\
        \n\
        Cпособ вывода: *{send_crypto}*\n\
        \n\
        Адрес: *{your_address}*"
            await message.answer(deposit_process, reply_markup=await confirm_btn(), parse_mode=types.ParseMode.MARKDOWN)
            await Send.end_right.set()
        else:
            await message.answer('Minimum 2500')
    except:
        print('Неправильная сумма')



# ======== 📥 Deposit -> USD -> CZK - USD -> The amount I get =========
@dp.callback_query_handler(text='get', state=Send.send_pay)
async def get_money(callback: types.CallbackQuery, state: FSMContext):
    """======== 📥 Deposit -> USD -> CZK - USD -> The amount I get ========="""
    await Send.send_get.set()
    await callback.message.answer(usd_get, reply_markup= await cancel_btn())

# ======== The amount I get =========
@dp.message_handler(state=Send.send_get)
async def get_money_usd(message: types.Message, state: FSMContext):
    """======== The amount I get ========="""
    your_amount = message.text
    try:
        if int(your_amount) >= 2500:
            currency_give = 'USD'
            currency_get = 'CZK'
            currency = float(float(your_amount) * float(value))
            deposit_process = f"Депозит #USD создан!\n\
        ID: #{id_transaction}\n\
        \n\
        Статус: Обрабатывается 🌀\n\
        \n\
        Сумма получаю: *{your_amount} {currency_give}* \n\
        Сумма отдаю: *{'{:.2f}'.format(currency)} {currency_get}*\n\
        Комиссия: *25 CZK*\n\
        \n\
        Метод:\n\
            `2502061515/2010` из чехии,\n\
            *IBAN:*`CZ34 2010 0000 0025 0206 1515`\n\
            *BIC/SWIFT:*`FIOBCZPPXXX`"
            
            await message.answer(deposit_process, reply_markup=await all_right_btn(), parse_mode=types.ParseMode.MARKDOWN)
            await Send.end_right.set()
        else:
            await message.answer('Minimum 2500')
    except:
        print('Неправильная сумма')
            

# =================== All right 👌🏻 ==================
@dp.callback_query_handler(text='all_right', state=Send.end_right)
async def all_right_end(callback: types.CallbackQuery, state:FSMContext):
    """========  ========"""
    await callback.message.answer(f'✅ Сохранено')
    await callback.message.answer(msc, reply_markup= await wallet_buttons())
    await state.finish()
    
    
# =========== 📥 Deposit -> USD ==============
@dp.callback_query_handler(text='usd', state=Send.send_usd)
async def deposit_usd(callback: types.CallbackQuery, state:FSMContext):
    """=========== 📥 Пополнить -> USD =============="""
    await callback.message.answer('Выбрано: *USD*', parse_mode=types.ParseMode.MARKDOWN)
    await callback.message.answer(usd, reply_markup=await get_usd())
    await Send.send_usd_banking.set()
    
    
# ========== 📥 Deposit -> USD -> Bank transfer in the Czech Republic =======
@dp.callback_query_handler(text='banking', state=Send.send_usd_banking)
async def deposit_banking(callback: types.CallbackQuery, state:FSMContext):
    """========== 📥 Deposti -> USD -> Bank transfer in the Czech Republic ======="""
    await callback.message.answer('Выбрано: *Банковский перевод в рамках Чехии*', parse_mode=types.ParseMode.MARKDOWN)
    await callback.message.answer(f'Выберите в чем удобнее вводить сумму:', reply_markup= await get_pay())
    await callback.message.edit_reply_markup(reply_markup=None)
    


# ============ ⤴️ Send to user =========
@dp.callback_query_handler(text='send_to_user')
async def send_to_user(callback: types.CallbackQuery):
    markup = InlineKeyboardMarkup(resize_keyboard=True)
    btn1 = InlineKeyboardButton(text='✖️ Отмена', callback_data='cancel')
    markup.add(btn1)
    await callback.message.answer('Введите UID пользователя', reply_markup=markup)


# =============== 🗃 Transaction History ================
@dp.callback_query_handler(text='history')
async def transaction(callback: types.CallbackQuery):
    await callback.message.answer('Выберите тип транзакций', reply_markup=await wallet_buttons())
    
    
# ================ 🎁 Activate promo code ================
@dp.callback_query_handler(text='promo_code')
async def activate_promokod(callback: types.CallbackQuery):
    await callback.message.answer('Введите промокод', reply_markup=await promokod())
    

