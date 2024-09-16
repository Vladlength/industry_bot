from aiogram import F, Router
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

import keyboards as kb

router = Router()


class Register(StatesGroup):
    name = State()
    surname = State()
    patronymic = State()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        "Привет! Я — бот для учёта рабочего времени. "
        "Моя задача — помочь тебе следить за своим рабочим графиком и временем отдыха."
        "Просто сообщи мне, когда ты начинаешь работать и когда заканчиваешь, а я буду вести учёт твоего времени")
    await message.answer(
        "Чтобы пользоваться всеми возможностями бота, зарегистрируйся /register, указав имя, фамилию, отчество и должность"
    )


@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.answer("/start запуск бота \n"
                         "/register регистрация пользователя \n"
                         "/help помощь \n")


@router.message(Command("register"))
async def register(message: Message, state: FSMContext):
    await state.set_state(Register.name)
    await message.answer("Введите ваше имя")


@router.message(Register.name)
async def register_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(Register.surname)
    await message.answer("Введите вашу фамилию")


@router.message(Register.surname)
async def register_surname(message: Message, state: FSMContext):
    await state.update_data(surname=message.text)
    await state.set_state(Register.patronymic)
    await message.answer("Введите ваше отчество")


@router.message(Register.patronymic)
async def register_patronymic(message: Message, state: FSMContext):
    await state.update_data(patronymic=message.text)
    data = await state.get_data()
    await message.answer(f"Ваше имя: {data['name']}\n"
                         f"Ваша фамилия: {data['surname']}\n"
                         f"Ваше отчество: {data['patronymic']}\n")
    # await state.clear()
    await message.answer("Всё верно?", reply_markup=kb.confirm)


@router.callback_query(F.data == "confirm")
async def register_confirm(callback: CallbackQuery, state: FSMContext):
    await state.clear()
    await callback.message.answer("Регистрация прошла успешно!")


@router.callback_query(F.data == "unconfirm")
async def register_unconfirm(callback: CallbackQuery, state: FSMContext):
    await state.set_state(Register.name)
    await callback.message.answer("Пройдите регистрацию повторно")
    await callback.message.answer("Введите ваше имя")
