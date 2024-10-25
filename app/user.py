from aiogram import Router, F
from aiogram.types import Message, CallbackQuery, InputFile
from aiogram.filters import CommandStart, Command
from aiogram.fsm.context import FSMContext

from app.quiz_module import answer_render
from app.states import Victory_State
import app.keyboards as kb
from config import question1_text, question2_text

user = Router()


@user.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Добро пожаловать в неофициальный бот "Московского Зоопарка"')
    await message.answer('Бот Призван Помочь вам с выбором животного для опеки по программе "Опекунство в Московском зоопарке"', reply_markup=kb.menu)

@user.message(F.text =='Что такое Опекунство?')
async def text_prems(message: Message):
    await message.answer('Возьмите животное под опеку! Участие в программе «Клуб друзей зоопарка» — это помощь в содержании наших обитателей, а также ваш личный вклад в дело сохранения биоразнообразия Земли и развитие нашего зоопарка.\n\nОсновная задача Московского зоопарка с самого начала его существования это — сохранение биоразнообразия планеты. Когда вы берете под опеку животное, вы помогаете нам в этом благородном деле.\n\nПри нынешних темпах развития цивилизации к 2050 году с лица Земли могут исчезнуть около 10 000 биологических видов. Московский зоопарк вместе с другими зоопарками мира делает все возможное, чтобы сохранить их. Традиция опекать животных в Московском зоопарке возникло с момента его создания в 1864г. Такая практика есть и в других зоопарках по всему миру.\n\nВ настоящее время опекуны объединились в неформальное сообщество — Клуб друзей Московского зоопарка. Программа «Клуб друзей» дает возможность опекунам ощутить свою причастность к делу сохранения природы, участвовать в жизни Московского зоопарка и его обитателей, видеть конкретные результаты своей деятельности. Опекать – значит помогать любимым животным. Можно взять под крыло любого обитателя Московского зоопарка, в том числе и того, кто живет за городом – в Центре воспроизводства редких видов животных под Волоколамском. Там живут и размножаются виды, которых нет в городской части зоопарка: величественные журавли стерхи, забавные дрофы, исчезнувшая в природе лошадь Пржевальского, изящные антилопы бонго и многие другие. Можете съездить на экскурсию в Центр и познакомиться с обитателями.', reply_markup=kb.menu)

@user.message(F.text =='Преимущества статуса опекуна')
async def text_prems(message: Message):
    await message.answer('Преимущества статуса опекуна:\n·Сертификат опеки, подтверждающий Ваш статус опекуна животного\n·Табличка на вольере с именем опекуна данного животного\n·Карта друга Московского зоопарка, дающая множество преимуществ', reply_markup=kb.menu) 
    
@user.message(F.text =='Пройти Викторину')
async def start_user(message: Message, state: FSMContext):
        await message.answer('Так быстро? Ладно!\n Вам нужно будет отвечать на вопросы при помощи встроенной клавиатуры ( вы можете найти её справа в строке ввода)\nПерейдите туда и начинайте', reply_markup=kb.start_quiz_button)
        await state.set_state(Victory_State.start)
        
@user.message(Victory_State.start)
async def question1(message: Message, state: FSMContext):
    await message.answer(question1_text, reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_1)

@user.message(Victory_State.question_1)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_1 = message.text)
    await message.answer(question2_text, reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_2)

@user.message(Victory_State.question_2)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_2 = message.text)
    await message.answer('3 из 10\nКак вы относитесь к общению с другими людьми?\nA) Предпочитаю глубокие и спокойные беседы.\nB) Люблю общаться и заводить новые знакомства.\nC) Ценю дружеские связи и активное взаимодействие.\nD) Общаюсь, когда это необходимо, но ценю личное пространство.', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_3)
    
@user.message(Victory_State.question_3)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_3 = message.text)
    await message.answer('4 из 10\nКак вы воспринимаете трудности?\nA) Стараюсь найти мирное решение.\nB) Применяю решительные меры для преодоления.\nC) Использую свою ловкость и смекалку.\nD) Подхожу к проблемам с осторожностью и расчетом.', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_4)
    
@user.message(Victory_State.question_4)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_4 = message.text)
    await message.answer("5 из 10\nКак вы относитесь к свободе и независимости?\nA) Ценю стабильность и комфорт.\nB) Свобода — это возможность для приключений.\nC) Независимость важна для самовыражения.\nD) Свобода — это возможность действовать по своему усмотрению.", reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_5)
    
@user.message(Victory_State.question_5)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_5 = message.text)
    await message.answer('6 из 10\nКак вы видите свою роль в группе или команде?\nA) Спокойный наблюдатель, который поддерживает других.\nB) Лидер, который вдохновляет и ведет за собой.\nC) Активный участник, который приносит идеи.\nD) Стратег, который помогает находить решения.', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_6)
    
@user.message(Victory_State.question_6)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_6 = message.text)
    await message.answer('7 из 10\nКак вы относитесь к риску?\nA) Предпочитаю избегать рисков и действовать осторожно.\nB) Готов(а) принимать риски ради новых возможностей.\nC) Оцениваю риски и принимаю взвешенные решения.\nD) Считаю, что риск — это часть жизни.', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_7)
    
@user.message(Victory_State.question_7)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_7 = message.text)
    await message.answer('8 из 10\nКак вы воспринимаете успех?\nA) Успех — это гармония и спокойствие.\nB) Успех — это достижения и новые горизонты.\nC) Успех — это признание и уважение.\nD) Успех — это постоянное развитие и самосовершенствование.', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_8)
    
@user.message(Victory_State.question_8)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_8 = message.text)
    await message.answer('9 из 10\nКак вы относитесь к обучению и саморазвитию?\nA) Считаю это важной частью жизни.\nB) Люблю изучать новые темы и навыки.\nC) Участвую в курсах и семинарах.\nD) Предпочитаю учиться на практике.', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_9)
    
@user.message(Victory_State.question_9)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_9 = message.text)
    await message.answer('Крайний вопрос!\nКак вы видите свою связь с природой?\nA) Я чувствую себя частью природы и ценю её.\nB) Я стремлюсь исследовать и открывать новое.\nC) Я нахожу вдохновение в её красоте.\nD) Я уважаю природу и стараюсь жить в гармонии с ней.', reply_markup=kb.answers_keyboard)
    await state.set_state(Victory_State.question_10)
    
@user.message(Victory_State.question_10)
async def question1(message: Message, state: FSMContext):
    await state.update_data(question_10 = message.text)
    await message.answer('Анализ Данных...')
    data = await state.get_data()
    Message = await answer_render(data)
    await message.delete()
    await message.answer(Message)