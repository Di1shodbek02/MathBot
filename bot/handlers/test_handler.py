import random
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from bot.buttons.language import lang, uzb_lang, eng_lang
from bot.buttons.reply import level_btn
from bot.dispetcher import dp
from aiogram import types
from aiogram.dispatcher import FSMContext


@dp.message_handler(lambda msg: msg.text in list(lang.get(uzb_lang).values()) + list(lang.get(eng_lang).values()),
                    state="lvl")
async def lvl_handler(msg: types.Message, state: FSMContext):
    global question
    user_lang = await state.get_data()
    data = lang.get(user_lang.get("lang"))

    if msg.text == data.get('level1'):
        question = f"{random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)}"

    elif msg.text == data.get('level2'):
        question = f"{random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)}"

    elif msg.text == data.get('level3'):
        question = f"{random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)}"

    elif msg.text == data.get('level4'):
        question = f"{random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)}"

    async with state.proxy() as state_data:
        state_data["answer"] = eval(question)
        state_data["lvl"] = msg.text
        state_data["true"] = 0
        state_data["false"] = 0

    rkm = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    rkm.add("stop 🛑")
    await state.set_state("answer")
    await msg.answer(f"{data.get('task')}  {question}", reply_markup=rkm)


@dp.message_handler(lambda msg: msg.text == "stop 🛑", state="answer")
async def stop_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as state_data:
        pass
    data = lang.get(state_data.get("lang"))
    text = f"""{state_data.get('lvl')}
{data.get("task_count")}  {state_data.get("true") + state_data.get("false")}
✅: {state_data.get("true")}
❌: {state_data.get("false")}
    """
    await state.set_state("lvl")
    await msg.answer(text, reply_markup=level_btn(data), parse_mode="Markdown")


@dp.message_handler(lambda msg: msg.text.strip('-').isdigit(), state="answer")
async def answer_handler(msg: types.Message, state: FSMContext):
    async with state.proxy() as state_data:
        pass
    data = lang.get(state_data.get("lang"))

    if state_data.get("lvl") == data.get('level1'):
        question = f"{random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)}"

    elif state_data.get("lvl") == data.get('level2'):
        question = f"{random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)}"

    elif state_data.get("lvl") == data.get('level3'):
        question = f"{random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)}"

    elif state_data.get("lvl") == data.get('level4'):
        question = f"{random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)} {random.choice(['+', '-', '*'])} {random.randrange(1, 10)}"

    async with state.proxy() as state_data:
        if state_data.get("answer") == int(msg.text):
            await msg.answer("✅")
            state_data["true"] += 1
        else:
            await msg.answer("❌")
            state_data["false"] += 1
        state_data["answer"] = eval(question)
        state_data["lvl"] = state_data.get("lvl")
    rkm = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True)
    rkm.add("stop 🛑")
    await state.set_state("answer")
    await msg.answer(f"{data.get('task')}  {question}", reply_markup=rkm)
