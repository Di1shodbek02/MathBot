import random

from aiogram import types
from aiogram.dispatcher import FSMContext

from bot.buttons.language import lang, uzb_lang, eng_lang
from bot.buttons.reply import lang_btn, level_btn
from bot.dispetcher import dp


@dp.message_handler(lambda msg: msg.text in [lang.get(uzb_lang).get("back"), lang.get(eng_lang).get("back")],
                    state="lvl")
@dp.message_handler(commands='start')
async def start_handler(msg: types.Message, state: FSMContext):
    await state.set_state("lang")
    await msg.answer('Language 👇', reply_markup=lang_btn())


@dp.message_handler(lambda msg: msg.text in [uzb_lang, eng_lang], state="lang")
async def welcome_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as data: data["lang"] = msg.text
    logo = "https://telegra.ph/file/e6347c2f535f646fd5697.png"
    data = lang.get(msg.text)
    await state.set_state("lvl")
    await msg.answer_photo(logo, data.get("welcome").format(msg.from_user.first_name), reply_markup=level_btn(data))
