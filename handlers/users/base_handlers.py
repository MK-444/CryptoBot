# aiogram
from aiogram.types import  CallbackQuery
from aiogram import types
from aiogram.dispatcher.filters import Command

from loader import dp
from keyboards.inline.wallet_inline import *
from functions.message import *
from aiogram.dispatcher import FSMContext


# ==================== ✖️ Cancel ==============
@dp.callback_query_handler(text='cancel', state='*')
async def cancel(callback: types.CallbackQuery, state:FSMContext):
    await callback.message.answer(msc, reply_markup=await wallet_buttons())
    await state.finish()

# ================= ◀️ Back ==================
@dp.callback_query_handler(text='back', state='*')
async def back(callback: types.CallbackQuery, state:FSMContext):
    await callback.message.answer(msc, reply_markup=await wallet_buttons())
    await state.finish()

# =================== All right 👌🏻 ==================
@dp.callback_query_handler(text='all_right', state="*")
async def all_right_end(callback: types.CallbackQuery, state:FSMContext):
    await callback.message.answer(f'✅ Сохранено')
    await callback.message.answer(msc, reply_markup= await wallet_buttons())
    await state.finish()