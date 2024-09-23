from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

from app.states import Victory_State
import app.keyboards as kb

quiz = Router()

@quiz.message(Victory_State.start)
async def question1(message: Message, state: FSMContext):
    await message.answer('Не будем тянуть!\nКак вы предпочитаете проводить время на природе?\n\nВарианты Ответов:\nA) Наблюдаю за окружающим миром и наслаждаюсь спокойствием.\nБ) Исследую новые места и занимаюсь активными видами спорта.\nВ) Участвую в приключениях и люблю быть в движении.\nГ) Остаюсь в тени, наблюдая за тем, что происходит вокруг.\n !Напоминаю, что отвечать нужно при помощи встроенной клавиатуры!', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_1)

@quiz.message(Victory_State.question_1)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_1 = message.text)
    await message.answer('Не будем тянуть!\nКак вы предпочитаете проводить время на природе?\n\nВарианты Ответов:\nA) Наблюдаю за окружающим миром и наслаждаюсь спокойствием.\nБ) Исследую новые места и занимаюсь активными видами спорта.\nВ) Участвую в приключениях и люблю быть в движении.\nГ) Остаюсь в тени, наблюдая за тем, что происходит вокруг.\n !Напоминаю, что отвечать нужно при помощи встроенной клавиатуры!', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_2)

@quiz.message(Victory_State.question_2)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_2 = message.text)
    await message.answer('Не будем тянуть!\nКак вы предпочитаете проводить время на природе?\n\nВарианты Ответов:\nA) Наблюдаю за окружающим миром и наслаждаюсь спокойствием.\nБ) Исследую новые места и занимаюсь активными видами спорта.\nВ) Участвую в приключениях и люблю быть в движении.\nГ) Остаюсь в тени, наблюдая за тем, что происходит вокруг.\n !Напоминаю, что отвечать нужно при помощи встроенной клавиатуры!', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_3)
    
@quiz.message(Victory_State.question_3)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_3 = message.text)
    await message.answer('Не будем тянуть!\nКак вы предпочитаете проводить время на природе?\n\nВарианты Ответов:\nA) Наблюдаю за окружающим миром и наслаждаюсь спокойствием.\nБ) Исследую новые места и занимаюсь активными видами спорта.\nВ) Участвую в приключениях и люблю быть в движении.\nГ) Остаюсь в тени, наблюдая за тем, что происходит вокруг.\n !Напоминаю, что отвечать нужно при помощи встроенной клавиатуры!', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_4)
    
@quiz.message(Victory_State.question_4)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_4 = message.text)
    await message.answer('Не будем тянуть!\nКак вы предпочитаете проводить время на природе?\n\nВарианты Ответов:\nA) Наблюдаю за окружающим миром и наслаждаюсь спокойствием.\nБ) Исследую новые места и занимаюсь активными видами спорта.\nВ) Участвую в приключениях и люблю быть в движении.\nГ) Остаюсь в тени, наблюдая за тем, что происходит вокруг.\n !Напоминаю, что отвечать нужно при помощи встроенной клавиатуры!', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_5)
    
@quiz.message(Victory_State.question_5)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_5 = message.text)
    await message.answer('Не будем тянуть!\nКак вы предпочитаете проводить время на природе?\n\nВарианты Ответов:\nA) Наблюдаю за окружающим миром и наслаждаюсь спокойствием.\nБ) Исследую новые места и занимаюсь активными видами спорта.\nВ) Участвую в приключениях и люблю быть в движении.\nГ) Остаюсь в тени, наблюдая за тем, что происходит вокруг.\n !Напоминаю, что отвечать нужно при помощи встроенной клавиатуры!', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_6)
    
@quiz.message(Victory_State.question_6)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_6 = message.text)
    await message.answer('Не будем тянуть!\nКак вы предпочитаете проводить время на природе?\n\nВарианты Ответов:\nA) Наблюдаю за окружающим миром и наслаждаюсь спокойствием.\nБ) Исследую новые места и занимаюсь активными видами спорта.\nВ) Участвую в приключениях и люблю быть в движении.\nГ) Остаюсь в тени, наблюдая за тем, что происходит вокруг.\n !Напоминаю, что отвечать нужно при помощи встроенной клавиатуры!', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_7)
    
@quiz.message(Victory_State.question_7)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_7 = message.text)
    await message.answer('Не будем тянуть!\nКак вы предпочитаете проводить время на природе?\n\nВарианты Ответов:\nA) Наблюдаю за окружающим миром и наслаждаюсь спокойствием.\nБ) Исследую новые места и занимаюсь активными видами спорта.\nВ) Участвую в приключениях и люблю быть в движении.\nГ) Остаюсь в тени, наблюдая за тем, что происходит вокруг.\n !Напоминаю, что отвечать нужно при помощи встроенной клавиатуры!', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_8)
    
@quiz.message(Victory_State.question_8)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_8 = message.text)
    await message.answer('Не будем тянуть!\nКак вы предпочитаете проводить время на природе?\n\nВарианты Ответов:\nA) Наблюдаю за окружающим миром и наслаждаюсь спокойствием.\nБ) Исследую новые места и занимаюсь активными видами спорта.\nВ) Участвую в приключениях и люблю быть в движении.\nГ) Остаюсь в тени, наблюдая за тем, что происходит вокруг.\n !Напоминаю, что отвечать нужно при помощи встроенной клавиатуры!', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_9)
    
@quiz.message(Victory_State.question_9)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_9 = message.text)
    await message.answer('Не будем тянуть!\nКак вы предпочитаете проводить время на природе?\n\nВарианты Ответов:\nA) Наблюдаю за окружающим миром и наслаждаюсь спокойствием.\nБ) Исследую новые места и занимаюсь активными видами спорта.\nВ) Участвую в приключениях и люблю быть в движении.\nГ) Остаюсь в тени, наблюдая за тем, что происходит вокруг.\n !Напоминаю, что отвечать нужно при помощи встроенной клавиатуры!', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_10)
    
@quiz.message(Victory_State.question_10)
async def question1(message: Message, state: FSMContext):
	await state.update_data(question_10 = message.text)
	data = await state.get_data()
	a,b,v,g = 0,0,0,0
	for i in data:
		if data[i] == 'А':
			a += 1
		if data[i] == 'Б':
			b += 1
		if data[i] == 'В':
			v += 1
		if data[i] == 'Г':
			g += 1
	variables = {'a': a, 'b': b, 'v': v, 'g': g}
	max_key = max(variables, key=variables.get)
	if max_key == a:
		await message.answer('Ваше тотемное животное — Южноафриканский жираф. Вы спокойны, уравновешены и цените гармонию в жизни.')
	if max_key == b:
		await message.answer('Ваше тотемное животное — Пума. Вы энергичны, любите приключения и стремитесь к новым вызовам.')
	if max_key == v:
		await message.answer('Ваше тотемное животное — Снежный барс. Вы открыты, дружелюбны и цените активное взаимодействие с окружающими.')
	if max_key == g:
		await message.answer('Ваше тотемное животное — Медоед. Вы независимы, целеустремленны и стремитесь к самосовершенствованию.')
	await state.clear()
	
     
        
    
    
    
