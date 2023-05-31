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

from keyboards.inline.info_inline import *
from keyboards.inline.wallet_inline import *
from functions.message import *

from loader import dp



# ========================== ℹ️ Info ========================

@dp.message_handler(Text(equals='ℹ️ Info'))
async def get_info(message: types.Message):
    await message.answer(f'Ваш 👤 UID: `{uid}`', parse_mode=types.ParseMode.MARKDOWN, reply_markup=await info_buttons())

@dp.callback_query_handler(text='fees')
async def get_fees(callback: types.CallbackQuery):
    """ ================ 🔗 Commission =========== """
    await callback.message.edit_text('Выберите интересующие вас комиссии', reply_markup=await komisie_btn())

@dp.callback_query_handler(text='deposit_fees')
async def get_deposit_fees(callback: types.CallbackQuery):
    """ ================ 🔗 Commission -> 📥 Replenish =========== """
    await callback.message.answer(fee_deposit)

@dp.callback_query_handler(text='output_fees')
async def output_fees(callback: types.CallbackQuery):
    """ ================ 🔗 Commission -> 📤  Withdrawal =========== """
    await callback.message.answer(fee_withdrawal)

@dp.callback_query_handler(text='referal')
async def get_referal_create(callback: types.CallbackQuery):
    """=============== 💸 Referral program ============"""
    await callback.message.edit_text(regeral, reply_markup=await referal_btn())
    
@dp.callback_query_handler(text='description')
async def get_referal(callback: types.CallbackQuery):
    """=============== 💸 Referral program ============"""
    await callback.message.answer(referal_msc)
