# -*- coding: utf-8 -*-
import telebot
import os
import random

bot_token='879109360:AAEFoDnD9_sTPjtmTGDW1U3u6FTatjndkmo'
bot = telebot.TeleBot(token=bot_token)


@bot.message_handler(commands=['start'])
def handle_start(message):
        user_markup=telebot.types.ReplyKeyboardMarkup(True,True)
        user_markup.row('Спорт', "Здоров'я",'Музон')
        user_markup.row('Методична література','Спорт цитати')
        bot.send_message(message.from_user.id,'Ласкаво просимо', reply_markup=user_markup )
keyboard1 = telebot.types.ReplyKeyboardMarkup(True,True)
keyboard1.row('Привіт','До побачення')

def send_msg(telegram_id, msg):
    try:
        bot.send_message(telegram_id, msg)
    except (ConnectionAbortedError, ConnectionResetError, ConnectionRefusedError, ConnectionError):
        print("ConnectionError - Sending again after 5 seconds!!!")
        bot.send_message(telegram_id, msg)


@bot.message_handler(content_types=['text'])
def handle_text (message):
    if message.text.lower() == 'привіт':
            bot.send_message(message.chat.id, 'Привіт друг')
    elif message.text.lower() == 'пока':
            bot.send_message(message.chat.id, 'до побачення')
    elif message.text == "Муз":
        bot.send_message(message.chat.id,'https://www.youtube.com/watch?v=LZS021qMt1c&feature=emb_logo')
    elif message.text == "Новини":
            bot.send_message(message.chat.id, "https://www.youtube.com/channel/UC9ERgt9yce0uh82-0ssID7w")
    elif message.text == "футбол":
            bot.send_message(message.chat.id, "https://www.youtube.com/channel/UCTY4zQ2wDTZk91XeKXWUk7Q")
            bot.send_message(message.chat.id, "https://www.youtube.com/user/FootballTVUA")
    elif message.text.lower() == 'я тебе люблю':
            bot.send_sticker(message.chat.id, 'CAADAgADoQkAAnlc4gmoJtwuBU70BRYE')
    elif message.text.lower() == 'мясо':
            bot.send_photo(message.chat.id, 'https://imbt.ga/0BQi681yJX')

    # -*- Меню -*-
    elif message.text == "Методична література":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Історія фізичної культури', 'Теорія і методика фізичного виховання',)
        user_markup.row('Організація і методика спортивно-туристичної роботи', 'Педагогіка',)
        user_markup.row('Туризм неповносправних', 'Фізичне виховання', '/start')
        bot.send_message(message.from_user.id, "Методична література кафедри  фізичної культури, спорту та здоров'я Луцького національно технічного університету", reply_markup=user_markup)

    elif message.text == "Здоров'я":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Вправи для хребта', "Тренування на всі групи м'язів в домашніх умовах", )
        user_markup.row("Системи пасивних тренувань для зміцнення м’язів спини і хребта", 'Вправи для очей', )
        user_markup.row('Вправи для сидячої роботи', '/start')
        bot.send_message(message.from_user.id, 'Фізична культура і здоров’я тісно пов’язані між собою, адже стан навколишнього середовища, шалений ритм життя і стресові ситуації послаблюють організм людини. Ось чому є важливим зміцнення нашого організму всіма можливими способами: фізичними заняттями, збалансованим харчуванням і т.п.', reply_markup=user_markup)

    elif message.text == "Спорт":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Футбол', 'Волейбол', )
        user_markup.row('Баскетбол', 'Хокей', )
        user_markup.row('Олімпійські ігри', '/start')
        bot.send_message(message.from_user.id,  "Спорт — організована за певними правилами діяльність людей, що полягає в зіставленні їхніх фізичних та інтелектуальних здібностей.", reply_markup=user_markup)




    # -*- Спорт-*-
    elif message.text == "Футбол":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Чемпіонат', 'Рейтинг', )
        user_markup.row('Онлайн транслація', 'Правила гри у футбол', )
        user_markup.row('Спорт', '/start')
        bot.send_message(message.from_user.id, " Футбол - це командний вид спорту, який грається між двома командами по одинадцять гравців зі сферичним м'ячем. Близько 250 мільйонів чоловіків і жінок із більш ніж 200 країн грають у футбол, що робить його найпопулярнішим в світі видом спорту. Футбол є олімпійським видом спорту.", reply_markup=user_markup)

    elif message.text == "Волейбол":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Чемпіонат волейбол', 'Рейтинг волейбол','Правила гри волейбол')
        user_markup.row('Спорт', '/start')
        bot.send_message(message.from_user.id, " Волейбо́л-спортивна гра з м'ячем, у якій дві команди змагаються на спеціальному майданчику, розділеному сіткою.",reply_markup=user_markup)

    elif message.text == "Баскетбол":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Чемпіонат баскетбол', 'Рейтинг баскетбол', 'Правила гри баскетбол')
        user_markup.row('Спорт', '/start')
        bot.send_message(message.from_user.id,"Баскетбол - спортивна командна гра з м'ячем, в якій м'яч закидають руками в кошик суперника.",reply_markup=user_markup)


    elif message.text == "Хокей":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Чемпіонат з хокею', 'Рейтинг збірних з хокею', 'Правила гри в хокей')
        user_markup.row('Спорт', '/start')
        bot.send_message(message.from_user.id,"Баскетбол - спортивна командна гра з м'ячем, в якій м'яч закидають руками в кошик суперника.",reply_markup=user_markup)


    elif message.text == "Олімпійські ігри":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Літні Олімпійські ігри', 'Зимові олімпійські ігри')
        user_markup.row('Олімпійські види спорту')
        user_markup.row('Спорт', '/start')
        bot.send_message(message.from_user.id,"Міжнародні спортивні змагання, які проводяться кожні два роки під переглядом Олімпійських ігор називаються олімпійськими. "
                                              "Переможці змагань отримують довічне звання олімпійського чемпіона.",reply_markup=user_markup)

    elif message.text == "Олімпійські види спорту":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Літні види спорту', 'Зимові види спорту', )
        user_markup.row('Олімпійські ігри', '/start')
        bot.send_message(message.from_user.id, 'Види спорту в програмі літніх та зимових Олімпіад', reply_markup=user_markup)


    # -*- Здоров'я-*-
    if message.text == "Системи пасивних тренувань для зміцнення м’язів спини і хребта":
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Йога', 'Пілатес')
        user_markup.row('Хаду', 'Калланетика','Стретчинг' )
        user_markup.row("Здоров'я", '/start')
        bot.send_message(message.from_user.id, 'Існує безліч пасивних тренувань, спрямованих на загальне оздоровлення нашого тіла, а, особливо, спини. Відмінна риса пасивної гімнастики в тому, що для вправ не потрібні додаткові обважнювачі. Для звичайних занять в спортзалі потрібен певний навик або постійний контроль тренера, оскільки неправильна техніка виконання може завдати непоправної шкоди вашому хребту. У пасивних системах м’язи качаються за рахунок їх усвідомленого напруження, хребет не страждає від необхідності брати на себе навантаження, а, навпаки, витягується, скручується і стає більш рухливим.', reply_markup=user_markup)

    # -*- Спорт-*-
    # -*- Футбол-*-
    if message.text == "Чемпіонат":
        bot.send_message(message.chat.id, 'Чемпіонат України')
        bot.send_message(message.chat.id,'https://terrikon.com/football/ukraine/championship')
    elif message.text == "Рейтинг":
        bot.send_message(message.chat.id,'Рейтинг УЄФА')
        bot.send_message(message.chat.id, 'https://ru.uefa.com/memberassociations/uefarankings')
    elif message.text == "Онлайн транслація":
        bot.send_message(message.chat.id,'Онлайн транслація футбольних матчів')
        bot.send_message(message.chat.id, 'https://myfootball.top/')
    elif message.text == "Правила гри у футбол":
        bot.send_message(message.chat.id,'Футбольні правила — правила гри у футбол, за якими проходять футбольні змагання.')
        bot.send_message(message.chat.id, 'https://uk.wikipedia.org/wiki/%D0%9F%D1%80%D0%B0%D0%B2%D0%B8%D0%BB%D0%B0_%D0%B3%D1%80%D0%B8_%D1%83_%D1%84%D1%83%D1%82%D0%B1%D0%BE%D0%BB')

    # -*- Волейбол -*-
    if message.text == "Чемпіонат волейбол":
        bot.send_message(message.chat.id, 'Чемпіонат України')
        bot.send_message(message.chat.id,'https://www.volleyball.ua/')

    elif message.text == "Правила гри волейбол":
        bot.send_message(message.chat.id, 'Характеристика гри')
        directory = "C:/Users/Dima/PycharmProjects/SportBot/files/спорт/Волейбол"
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
               document = open(directory + '/' + file, 'rb')
               bot.send_chat_action(message.from_user.id, 'upload_document')
               bot.send_document(message.from_user.id, document)
               document.close()

    elif message.text == "Рейтинг волейбол":
        bot.send_message(message.chat.id, 'Світовий рейтинг збірних з волейболу. Жінки.')
        bot.send_message(message.chat.id,'https://allvolley.ru/mirovoj-rejting-sbornyx-po-volejbolu-zhenshhiny.html')
        bot.send_message(message.chat.id, 'Світовий рейтинг волейбольних збірних. Чоловіки.')
        bot.send_message(message.chat.id, 'https://allvolley.ru/rejting-muzhchiny.html')


    # -*- Баскетбол -*-
    if message.text == "Чемпіонат баскетбол":
        bot.send_message(message.chat.id, 'ФБУ Суперлига')
        bot.send_message(message.chat.id,'https://www.volleyball.ua/')

    if message.text == "Рейтинг баскетбол":
        bot.send_message(message.chat.id, 'Кращі клуби світу 2019')
        bot.send_message(message.chat.id,'https://www.sports.ru/basketball/club/')

    elif message.text == "Правила гри баскетбол":
        bot.send_message(message.chat.id, 'Характеристика гри')
        directory = "C:/Users/Dima/PycharmProjects/SportBot/files/спорт/Баскетбол"
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
               document = open(directory + '/' + file, 'rb')
               bot.send_chat_action(message.from_user.id, 'upload_document')
               bot.send_document(message.from_user.id, document)
               document.close()

        # -*- Хокей -*-
    if message.text == "Чемпіонат з хокею":
        bot.send_message(message.chat.id, 'Українська хокейна ліга - організація, що займається проведенням і освітленням чемпіонату України з хокею.')
        bot.send_message(message.chat.id, 'https://www.myscore.com.ua/hockey/ukraine/uhl/standings/')

    elif message.text == "Рейтинг збірних з хокею":
        bot.send_message(message.chat.id, 'Міжнародна федерація хокею на льоду (International Ice Hockey Federation, IIHF) становить світовий рейтинг національних збірних з хокею (IIHF World Ranking) починаючи з 2003 року. Місця в рейтингу розраховуються на основі результатів виступів збірних на останніх чотирьох Чемпіонатах світу і останній зимовій Олімпіаді.')
        bot.send_message(message.chat.id, 'https://pribalt.info/hokkei/reiting-sbornyh-po-hokkeyu')

    elif message.text == "Правила гри в хокей":
        bot.send_message(message.chat.id, 'Характеристика гри')
        directory = "C:/Users/Dima/PycharmProjects/SportBot/files/спорт/Хокей"
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()

    # -*- Олімпійські ігри -*-
    if message.text == "Літні Олімпійські ігри":
        directory = 'C:/Users/Dima/PycharmProjects/SportBot/files/Олімпійські ігри/Літні олімпійські ігри'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            img = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()

    if message.text == "Зимові олімпійські ігри":
        directory = 'C:/Users/Dima/PycharmProjects/SportBot/files/Олімпійські ігри/Зимові олімпійські ігри'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            img = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()

    if message.text == "Літні види спорту":
        directory = 'C:/Users/Dima/PycharmProjects/SportBot/files/Олімпійські ігри/Види спорту/Літні види спорту'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            img = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()

    if message.text == "Зимові види спорту":
        directory = 'C:/Users/Dima/PycharmProjects/SportBot/files/Олімпійські ігри/Види спорту/Зимові види спорту'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            img = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()

    # -*- ТЗдоров'я-*-
    # -*- Тренування на всі групи м'язів в домашніх умовах-*-
    if message.text == "Тренування на всі групи м'язів в домашніх умовах":
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=LF1hsGsYYH4')
        directory = "C:/Users/Dima/PycharmProjects/SportBot/files/Здоров'я\Комплекс вправ на всі групи м’язів в домашніх умовах"
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
               document = open(directory + '/' + file, 'rb')
               bot.send_chat_action(message.from_user.id, 'upload_document')
               bot.send_document(message.from_user.id, document)
               document.close()

    # -*- Вправи для сидячої роботи-*-
    if message.text.lower() == 'вправи для сидячої роботи':
        directory = "C:/Users/Dima/PycharmProjects/SportBot/files/Здоров'я/Вправи для сидячої роботи"
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
               document = open(directory + '/' + file, 'rb')
               bot.send_chat_action(message.from_user.id, 'upload_document')
               bot.send_document(message.from_user.id, document)
               document.close()





    # -*- Вправи для очей-*-
    if message.text.lower() == 'вправи для очей':
        directory = "C:/Users/Dima/PycharmProjects/SportBot/files/Здоров'я/Зір"
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
               document = open(directory + '/' + file, 'rb')
               bot.send_chat_action(message.from_user.id, 'upload_document')
               bot.send_document(message.from_user.id, document)
               document.close()




    # -*- Вправи для хребта-*-
    if message.text.lower() == 'вправи для хребта':
        directory = "C:/Users/Dima/PycharmProjects/SportBot/files/Здоров'я/Хребет"
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
               document = open(directory + '/' + file, 'rb')
               bot.send_chat_action(message.from_user.id, 'upload_document')
               bot.send_document(message.from_user.id, document)
               document.close()





    # -*- Системи пасивних тренувань для зміцнення м’язів спини і хребта-*-
    if message.text.lower() == 'йога':
        directory = "C:/Users/Dima/PycharmProjects/SportBot/files/Здоров'я/Системи пасивних тренувань для зміцнення м’язів спини і хребта/Йога"
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
               document = open(directory + '/' + file, 'rb')
               bot.send_chat_action(message.from_user.id, 'upload_document')
               bot.send_document(message.from_user.id, document)
               document.close()

    elif message.text.lower() == 'пілатес':
        directory = "C:/Users/Dima/PycharmProjects/SportBot/files/Здоров'я/Системи пасивних тренувань для зміцнення м’язів спини і хребта/Пілатес"
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()

    elif message.text.lower() == 'хаду':
        directory = "C:/Users/Dima/PycharmProjects/SportBot/files/Здоров'я/Системи пасивних тренувань для зміцнення м’язів спини і хребта/Хаду"
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()

    elif message.text.lower() == 'калланетика':
        directory = "C:/Users/Dima/PycharmProjects/SportBot/files/Здоров'я/Системи пасивних тренувань для зміцнення м’язів спини і хребта/Калланетика"
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()

    elif message.text.lower() == 'стретчинг':
        directory = "C:/Users/Dima/PycharmProjects/SportBot/files/Здоров'я/Системи пасивних тренувань для зміцнення м’язів спини і хребта/Стретчинг"
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()



    # -*- Методична література-*-



    if message.text.lower() == 'історія фізичної культури':
        directory = 'C:/Users/Dima/PycharmProjects/SportBot/files/Методична література/Історія фізичної культури'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()

    elif message.text.lower() == 'організація і методика спортивно-туристичної роботи':
        directory = 'C:/Users/Dima/PycharmProjects/SportBot/files/Методична література/Організація і методика спортивно-туристичної роботи'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()

    elif message.text.lower() == 'педагогіка':
        directory = 'C:/Users/Dima/PycharmProjects/SportBot/files/Методична література/Педагогіка'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()

    elif message.text.lower() == 'теорія і методика фізичного виховання':
        directory = 'C:/Users/Dima/PycharmProjects/SportBot/files/Методична література/Теорія і методика фізичного виховання'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()

    elif message.text.lower() == 'туризм неповносправних':
        directory = 'C:/Users/Dima/PycharmProjects/SportBot/files/Методична література/Туризм неповносправних'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()

    elif message.text.lower() == 'фізичне виховання':
        directory = 'C:/Users/Dima/PycharmProjects/SportBot/files/Методична література/Фізичне виховання'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()

    # -*- Цитати-*-

    if message.text.lower() == 'спорт цитати':
        directory = 'C:/Users/Dima/PycharmProjects/SportBot/files/Цитати'
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        img = open(directory + '/' + random_file,'rb')
        bot.send_chat_action(message.from_user.id, 'upload_photo')
        bot.send_photo(message.from_user.id, img)
        img.close()


    # -*- Аудио -*-

    elif message.text.lower() == 'музон':
        directory = 'C:/Users/Dima/PycharmProjects/SportBot/files/audio'
        bot.send_message(message.chat.id, 'Музика для спорту')
        all_files_in_directory = os.listdir(directory)
        random_file = random.choice(all_files_in_directory)
        audio =  open(directory + '/' + random_file,'rb')
        bot.send_chat_action(message.from_user.id, 'upload_audio')
        bot.send_audio(message.from_user.id, audio)
        audio.close()




    # -*- Інше-*-

    if message.text.lower() == 'фото':
        directory = 'C:/Users/Dima/PycharmProjects/SportBot/files/photo'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            img = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_photo')
            bot.send_photo(message.from_user.id, img)
            img.close()

    elif message.text.lower() == 'відео':
        video = open("C:/Users/Dima/PycharmProjects/SportBot/files/video/1.mp4",'rb')
        bot.send_chat_action(message.from_user.id, 'upload_video')
        bot.send_video(message.from_user.id, video)
        video.close()
    elif message.text.lower() == 'документ':
        directory = 'C:/Users/Dima/PycharmProjects/SportBot/files/documents'
        all_files_in_directory = os.listdir(directory)
        print(all_files_in_directory)
        for file in all_files_in_directory:
            document = open(directory + '/' + file, 'rb')
            bot.send_chat_action(message.from_user.id, 'upload_document')
            bot.send_document(message.from_user.id, document)
            document.close()
    elif message.text == 'карта':
        bot.send_chat_action(message.from_user.id, 'find_location')
        bot.send_location(message.from_user.id, 50.787543, 25.112122)


bot.polling(none_stop=True, interval=0 )
