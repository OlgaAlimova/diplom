from aiogram import types, Dispatcher

def get_main_menu():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = ["Финансовый советник", "Университет", "Криптоакадемия", "Внебиржевые акции"]
    keyboard.add(*buttons)
    return keyboard

def get_back_to_menu_button():
    keyboard = types.InlineKeyboardMarkup()
    back_button = types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back_to_menu")
    keyboard.add(back_button)
    return keyboard

async def send_welcome(message: types.Message):
    keyboard = get_main_menu()
    await message.reply("Добро пожаловать! Я ваш финансовый консультант. Чем могу помочь?", reply_markup=keyboard)

async def send_advisor_info(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("Записаться на консультацию", callback_data="advisor_signup"),
        types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back_to_menu")
    )
    await message.reply("Финансовый советник: Ольга Алимова. Запишитесь на консультацию.", reply_markup=keyboard)

async def send_university_info(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("Подробнее об университете", callback_data="university_more_info"),
        types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back_to_menu")
    )
    await message.reply("Обучение в Университете управления финансами: 5 лет, профессия финансового советника.", reply_markup=keyboard)

async def send_crypto_info(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("Подробнее о криптоакадемии", callback_data="crypto_more_info"),
        types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back_to_menu")
    )
    await message.reply("Криптоакадемия SoulTeam: Обучение современным технологиям и криптовалютам.", reply_markup=keyboard)

async def send_otc_info(message: types.Message):
    keyboard = types.InlineKeyboardMarkup()
    keyboard.add(
        types.InlineKeyboardButton("Подробнее о внебиржевых акциях", callback_data="otc_more_info"),
        types.InlineKeyboardButton("Вернуться в главное меню", callback_data="back_to_menu")
    )
    await message.reply("Инвестиции в внебиржевые акции: Получайте доход ежемесячно без необходимости глубокого изучения.", reply_markup=keyboard)

async def handle_callback(callback_query: types.CallbackQuery):
    if callback_query.data == "back_to_menu":
        keyboard = get_main_menu()
        await callback_query.message.edit_text("Добро пожаловать! Я ваш финансовый консультант. Чем могу помочь?", reply_markup=keyboard)
    elif callback_query.data == "advisor_signup":
        await callback_query.message.edit_text("Чтобы записаться на консультацию, свяжитесь с нашим финансовым советником Ольгой Алимовой через email: olga@example.com", reply_markup=get_back_to_menu_button())
    elif callback_query.data == "university_more_info":
        await callback_query.message.edit_text("Для получения дополнительной информации об университете, посетите наш сайт: www.university.com", reply_markup=get_back_to_menu_button())
    elif callback_query.data == "crypto_more_info":
        await callback_query.message.edit_text("Для получения дополнительной информации о криптоакадемии, посетите наш сайт: www.cryptoacademy.com", reply_markup=get_back_to_menu_button())
    elif callback_query.data == "otc_more_info":
        await callback_query.message.edit_text("Для получения дополнительной информации о внебиржевых акциях, свяжитесь с нами через email: otc@example.com", reply_markup=get_back_to_menu_button())

def register_handlers(dp: Dispatcher):
    dp.register_message_handler(send_welcome, commands=['start'])
    dp.register_message_handler(send_advisor_info, lambda message: message.text == "Финансовый советник")
    dp.register_message_handler(send_university_info, lambda message: message.text == "Университет")
    dp.register_message_handler(send_crypto_info, lambda message: message.text == "Криптоакадемия")
    dp.register_message_handler(send_otc_info, lambda message: message.text == "Внебиржевые акции")
    dp.register_callback_query_handler(handle_callback, lambda c: c.data.startswith("back_to_menu") or c.data.endswith("_more_info") or c.data == "advisor_signup")
