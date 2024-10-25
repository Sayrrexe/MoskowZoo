from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputFile, FSInputFile
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from app.keyboards import link_kb, start_quiz
from app.quiz_module import answer_render
from app.states import Victory_State
import app.keyboards as kb
from config import (question1_text, question2_text, question3_text, question4_text, question5_text,
                    question6_text, question7_text, question8_text, question9_text,
                    question10_text, answer_a, answer_d, answer_c, answer_b, share_a, share_c,
                    share_d, share_b, welcome_text, description_text, info_text, benefits_text,
                    quiz_start_text)

user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(welcome_text)
    await message.answer(description_text, reply_markup=kb.menu)

@user.message(Command('menu'))
async def cmd_menu(message: Message, state: FSMContext):
    await state.clear()
    await message.answer('Вы в меню!', reply_markup=kb.menu)

@user.message(F.text.lower() =='что такое опекунство?')
async def text_prems(message: Message):
    await message.answer(info_text, reply_markup=kb.menu)

@user.message(F.text =='Преимущества статуса опекуна')
async def text_prems(message: Message):
    await message.answer(benefits_text, reply_markup=kb.menu)
    
@user.message(F.text.lower() =='пройти викторину')
async def start_user(message: Message, state: FSMContext):
        await message.answer(quiz_start_text, reply_markup=kb.start_quiz_button)
        await state.set_state(Victory_State.start)


@user.callback_query(F.data == 'menu')
async def start_user(callback: CallbackQuery, state: FSMContext):
    await callback.message.answer(quiz_start_text, reply_markup=kb.start_quiz_button)
    await state.set_state(Victory_State.start)

async def check_answer(message):
    text = str(message.text)
    if text == 'А' or text ==  'Б' or text == 'В' or text == 'Г':
        return True
    else:
        await message.answer('Используйте встроенную клавиатуру!')
        return False

@user.message(Victory_State.start)
async def question1(message: Message, state: FSMContext):
    await message.answer(question1_text, reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_1)

@user.message(Victory_State.question_1)
async def question1(message: Message, state: FSMContext):
    if not await check_answer(message):
        return
    await state.update_data(question_1 = message.text)
    await message.answer(question2_text, reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_2)

@user.message(Victory_State.question_2)
async def question1(message: Message, state: FSMContext):
    if not await check_answer(message):
        return
    await state.update_data(question_2 = message.text)
    await message.answer(question3_text, reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_3)
    
@user.message(Victory_State.question_3)
async def question1(message: Message, state: FSMContext):
    if not await check_answer(message):
        return
    await state.update_data(question_3 = message.text)
    await message.answer(question4_text, reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_4)
    
@user.message(Victory_State.question_4)
async def question1(message: Message, state: FSMContext):
    if not await check_answer(message):
        return
    await state.update_data(question_4 = message.text)
    await message.answer(question5_text, reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_5)
    
@user.message(Victory_State.question_5)
async def question1(message: Message, state: FSMContext):
    if not await check_answer(message):
        return
    await state.update_data(question_5 = message.text)
    await message.answer(question6_text, reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_6)
    
@user.message(Victory_State.question_6)
async def question1(message: Message, state: FSMContext):
    if not await check_answer(message):
        return
    await state.update_data(question_6 = message.text)
    await message.answer(question7_text, reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_7)
    
@user.message(Victory_State.question_7)
async def question1(message: Message, state: FSMContext):
    if not await check_answer(message):
        return
    await state.update_data(question_7 = message.text)
    await message.answer(question8_text, reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_8)
    
@user.message(Victory_State.question_8)
async def question1(message: Message, state: FSMContext):
    if not await check_answer(message):
        return
    await state.update_data(question_8 = message.text)
    await message.answer(question9_text, reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_9)
    
@user.message(Victory_State.question_9)
async def question1(message: Message, state: FSMContext):
    if not await check_answer(message):
        return
    await state.update_data(question_9 = message.text)
    await message.answer(question10_text, reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_10)
    
@user.message(Victory_State.question_10)
async def question1(message: Message, state: FSMContext):
    if not await check_answer(message):
        return
    await state.update_data(question_10 = message.text)
    await message.answer('Анализ Данных...')
    data = await state.get_data()
    key = await answer_render(data)
    if key == 'a':
        image, text = answer_a[0], answer_a[1]
        await message.answer_photo(photo=FSInputFile(image, filename="pingvin"),
                                   caption=text, reply_markup=await kb.share_kb(key))
    if key == 'b':
        image, text = answer_b[0], answer_b[1]
        await message.answer_photo(photo=FSInputFile(image, filename="puma"),
                                   caption=text, reply_markup=await kb.share_kb(key))
    if key == 'c':
        image, text = answer_c[0], answer_c[1]
        await message.answer_photo(photo=FSInputFile(image, filename="bars"),
                                   caption=text, reply_markup=await kb.share_kb(key))
    if key == 'd':
        image, text = answer_d[0], answer_d[1]
        await message.answer_photo(photo=FSInputFile(image, filename="medoed"),
                                   caption=text, reply_markup= await kb.share_kb(key))
    await state.clear()

@user.callback_query(F.data.startswith("share_"))
async def share(callback: CallbackQuery):
    key = callback.data.split("_")[1]
    await callback.message.delete()
    if key == 'a':
        image, text = share_a[0], share_a[1]
        await callback.message.answer_photo(photo=FSInputFile(image, filename="Car"),
                                   caption=text, reply_markup=link_kb)
    if key == 'b':
        image, text = share_b[0], share_b[1]
        await callback.message.answer_photo(photo=FSInputFile(image, filename="Car"),
                                   caption=text, reply_markup=link_kb)
    if key == 'c':
        image, text = share_c[0], share_c[1]
        await callback.message.answer_photo(photo=FSInputFile(image, filename="Car"),
                                   caption=text, reply_markup=link_kb)
    if key == 'd':
        image, text = share_d[0], share_d[1]
        await callback.message.answer_photo(photo=FSInputFile(image, filename="Car"),
                                   caption=text, reply_markup=link_kb)
