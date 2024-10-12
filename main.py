import telebot
from telebot import types


botTimeWeb = telebot.TeleBot('')


@botTimeWeb.message_handler(commands=['start'])
def startBot(message):
    first_mess = (f"<b>{message.from_user.first_name} {message.from_user.last_name}</b>, Приветствуем Вас в рядах работников ООО C3 Экологика!\n"
                  f"Мы - молодая, амбициозная, дружная компания. Мы растём и развиваемся. Добро пожаловать к нам!")

    markup = types.InlineKeyboardMarkup()
    button_labor_relations = types.InlineKeyboardButton(text='Всё, о том, что касается трудовых отношений', callback_data='labor_relations')
    markup.add(button_labor_relations)

    button_work_office = types.InlineKeyboardButton(text='Всё, о том, что касается работы в офисе', callback_data='work_office')
    markup.add(button_work_office)

    button_work_construction = types.InlineKeyboardButton(text='Всё, о том, что касается работы на стройке', callback_data='work_construction')
    markup.add(button_work_construction)

    button_sales_office = types.InlineKeyboardButton(text='Всё, что касается работы в офисе продаж', callback_data='sales_office')
    markup.add(button_sales_office)

    botTimeWeb.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@botTimeWeb.callback_query_handler(func=lambda call:True)
def response(function_call):
    if function_call.message:
        if function_call.data == "labor_relations":
            second_mess = ("Подача заявления на увольнение не менее, чем за 14 дней \n \n"
                           "Подача заявления на ежегодный отпуск не менее, чем за неделю до даты наступления отпуска \n \n"
                           "Подача заявления без сохранения заработной платы не позднее дня наступления отпуска \n \n"
                           "Остались вопросы? Звони 88005553535 \n"
                           "Пиши - example@example.com")
            markup = types.InlineKeyboardMarkup()
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)

        if function_call.data == ("work_office"):
            second_mess = ("Для входа в офис наш офис-менеджер Наталья выдаст Вам пропуск. \n"
                           "Если нужны канцелярские принадлежности тоже к Наталье. \n \n"
                           "На нашей уютной кухне есть чайник, кофемашина, холодильник. Еду мы принимаем только на кухне. \n \n"
                           "В офисе запрещено курить.\n \n"
                           "Строгого дресс-кода у нас нет. Но придерживаемся стиля. \n"
                           "Casual - практично, комфотно, удобно. \n \n"
                           "Все доступы в компьютер, программы и сети будут предоставлены в первый рабочий день.\n \n"
                           "Остались вопросы? Звони 88005553535 \n"
                           "Пиши - example@example.com"
                            )
            markup = types.InlineKeyboardMarkup()
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)

        if function_call.data == "work_construction":
            second_mess = "Упс... Мы работаем и скоро наполним информацией"
            markup = types.InlineKeyboardMarkup()
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)

        if function_call.data == "sales_office":
            second_mess = "Упс... Мы работаем и скоро наполним информацией"
            markup = types.InlineKeyboardMarkup()
            botTimeWeb.send_message(function_call.message.chat.id, second_mess, reply_markup=markup)
            botTimeWeb.answer_callback_query(function_call.id)


botTimeWeb.infinity_polling()