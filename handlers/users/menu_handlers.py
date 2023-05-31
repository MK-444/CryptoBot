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
from loader import dp



# ========================== Menu ========================
@dp.message_handler(commands='menu')
async def get_menu(message: types.Message):
    await message.answer('Выберите действие', reply_markup=await keyboard())

@dp.message_handler(commands=['start','help'])
async def start(message: types.Message):
    await message.answer(f'Добро пожаловать, {message.from_user.first_name}!{start_text}', parse_mode='HTML', reply_markup=await keyboard())

@dp.message_handler(commands='wallet')
async def wallet(message: types.Message):
    await message.answer(msc, reply_markup=await wallet_buttons(), parse_mode=ParseMode.MARKDOWN)
    
@dp.message_handler(commands='swap')
async def swap(message: types.Message):
    await message.answer(msc, reply_markup=await exchange_buttons(), parse_mode=ParseMode.MARKDOWN)
    
@dp.message_handler(commands='settings')
async def settings(message: types.Message):
    await message.answer(settings, reply_markup=await settings_buttons(), parse_mode=ParseMode.MARKDOWN)
    
@dp.message_handler(commands='info')
async def info(message: types.Message):
    await message.answer(f'Ваш 👤 UID: `{uid}`', parse_mode=types.ParseMode.MARKDOWN, reply_markup=await info_buttons())
    
