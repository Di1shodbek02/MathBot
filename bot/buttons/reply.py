from aiogram.types import ReplyKeyboardMarkup
from bot.buttons.language import uzb_lang, eng_lang, lang


def level_btn(data):
    design = [
        [data.get("level1"), data.get("level2")],
        [data.get("level3"), data.get("level4")],
        [data.get("back")]
    ]

    markup = ReplyKeyboardMarkup(design, resize_keyboard=True, one_time_keyboard=True)
    return markup


def lang_btn():
    design = [
        [uzb_lang, eng_lang]
    ]

    markup = ReplyKeyboardMarkup(design, resize_keyboard=True, one_time_keyboard=True)
    return markup
