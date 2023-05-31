# aiogram
from aiogram.dispatcher.filters import Text
from aiogram.types import  CallbackQuery
from aiogram import Bot, Dispatcher, executor, types 
from aiogram.types import ReplyKeyboardRemove, ParseMode
from aiogram.dispatcher import FSMContext
# from aiogram.types.message import ContentType
from aiogram.contrib.fsm_storage.memory import MemoryStorage

# python libraries
import logging 
import pyotp
import os 

# pip install libraries
from py_currency_converter import convert
from pycoingecko import CoinGeckoAPI
from dotenv import load_dotenv
import qrcode

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

from states.state import *
from loader import dp, bot



# ========================== ⚙️ Settings ========================
@dp.message_handler(Text(equals='⚙️ Settings'))
async def get_settings(message: types.Message):
    await message.answer(message.text, reply_markup=await settings_buttons())


@dp.callback_query_handler(text='fa2')
async def get_2fa(callback: types.CallbackQuery):
    """=============== 🔒 2FA ============"""
    await callback.message.answer(twofactory,reply_markup= await fa2_btn())

@dp.callback_query_handler(text='twofactory')
async def create_2fa_input(callback: types.CallbackQuery):
    """========== 🔒 2FA -> Add 2FA ============"""
    await callback.message.answer('Введите название для нового 2FA')
    await ProfileStatesGroup.name.set() 

@dp.message_handler(state=ProfileStatesGroup.name)
async def confirm_2fa(message: types.Message, state:FSMContext):
    """=============== Add 2FA ============"""
    global msg 
    msg = message.text
    await ProfileStatesGroup.next()
    await message.answer(f'Подтвердите название 2FA или отправьте новое `{msg}`',  parse_mode=types.ParseMode.MARKDOWN, reply_markup=await confirm_btn())
    await ProfileStatesGroup.confirm.set()


@dp.callback_query_handler(text='right', state=ProfileStatesGroup.confirm)
async def get_2fa_input(callback: types.CallbackQuery, state:FSMContext):
    """========== 🔒 2FA -> Add 2FA ============"""
    await callback.message.answer('2FA название подтверждено')
    global secret_key
    secret_key = pyotp.random_base32()
    url = pyotp.totp.TOTP(secret_key).provisioning_uri(msg, issuer_name="MKCryptoBot")
    qr = qrcode.QRCode(version = 1, box_size = 7, border = 4)
    qr.add_data(url)
    qr.make(fit = True)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('/home/maria/Документы/IT/MKcryptoBot/handlers/users/qrcodes/MyQRCode2fac.png')
    k = open('/home/maria/Документы/IT/MKcryptoBot/handlers/users/qrcodes/MyQRCode2fac.png', 'rb')
    authe = f"Вы собираетесь добавить 2FA {msg}\n\
\n\
Сохраните секретный код ниже:\n\
\n\
`{secret_key}`\n\
\n\
Код будет показан лишь 1 раз и удален сразу после подтверждения!\n\
\n\
Для подтверждения создания 2FA напишите шестизначный код"
    await bot.send_photo(callback.from_user.id, photo=k, caption=authe, parse_mode=ParseMode.MARKDOWN)
    await ProfileStatesGroup.six_digit_code.set()
    
    
@dp.message_handler(state=ProfileStatesGroup.six_digit_code)
async def cmd_create(message: types.Message, state:FSMContext):
    """=============== Add 2FA ============"""
    global msg_code 
    msg_code = message.text
    totp = pyotp.TOTP(secret_key)
    if totp.verify(msg_code):
        await message.answer("Code is valid.")
    else:
        await message.answer("Invalid code.")
    await state.finish()


@dp.callback_query_handler(text='uid')
async def get_uid(callback: types.CallbackQuery):
    """======== 👤 My UID =========="""
    await callback.message.answer(f'Your 👤 UID:{uid}', reply_markup=await buy_btn())


