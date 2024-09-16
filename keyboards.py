from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

confirm = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="да", callback_data="confirm")],
                                                [InlineKeyboardButton(text="нет", callback_data="unconfirm")]])
