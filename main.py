import telebot
import config


bot = telebot.TeleBot(token=config.TOKEN)

from datetime import datetime
import bisect

солка22 = ["6:28", "6:46", "7:14", "7:24", "7:35", "8:01", "8:23", "8:44", "9:01", "9:23", "9:37", "10:11", "10:41",
           "11:16", "11:27", "12:00", "12:20", "12:48", "13:00", "13:14", "13:37", "14:04", "14:38", "14:48", "15:35",
           "16:00", "16:20", "16:40", "16:55", "17:15", "17:45", "18:08", "18:20", "18:41", "19:16", "19:35", "20:23",
           "21:10", "22:10"]

тика22 =  ["6:35", "6:53", "7:21", "7:31", "7:42", "8:08", "8:30", "8:51", "9:08", "9:30", "9:44", "10:18", "10:48",
           "11:23", "11:34", "12:07", "12:27", "12:55", "13:07", "13:21", "13:44", "14:11", "14:45", "14:55", "15:42",
           "16:07", "16:27", "16:47", "17:02", "17:22", "17:52", "18:15", "18:27", "18:48", "19:23", "19:42", "20:30",
           "21:17", "22:17"]

предм22 = ["6:42", "7:00", "7:28", "7:38", "7:49", "8:15", "8:37", "8:58", "9:15", "9:37", "9:51", "10:25", "10:55",
           "11:30", "11:41", "12:14", "12:34", "13:02", "13:14", "13:28", "13:51", "14:18", "14:52", "15:02", "15:49",
           "16:14", "16:34", "16:54", "17:09", "17:29", "17:59", "18:22", "18:34", "18:55", "19:30", "19:49", "20:37",
           "21:24", "22:24"]

вок22 =   ["6:51", "7:09", "7:37", "7:47", "7:58", "8:24", "8:46", "9:07", "9:24", "9:46", "10:00", "10:34", "11:04",
           "11:39", "11:50", "12:23", "12:43", "13:11", "13:23", "13:37", "14:00", "14:27", "15:01", "15:11", "15:58",
           "16:23", "16:43", "17:03", "17:18", "17:38", "18:08", "18:31", "18:43", "19:04", "19:39", "19:58", "20:46",
           "21:33", "22:33"]

полит22 = ["7:00", "7:18", "7:46", "7:56", "8:07", "8:33", "8:55", "9:16", "9:33", "9:55", "10:09", "10:43", "11:13",
           "11:48", "11:59", "12:32", "12:52", "13:20", "13:32", "13:46", "14:09", "14:36", "15:10", "15:20", "16:07",
           "16:32", "16:52", "17:12", "17:27", "17:47", "18:17", "18:40", "18:52", "19:13", "19:48", "20:07", "20:55",
           "21:42", "22:42"]

пос22_1 =   ["6:00", "6:20", "6:48", "7:12", "7:34", "8:00", "8:12", "8:36", "8:50", "9:24", "9:48", "10:18", "10:42",
             "11:12", "11:36", "12:00", "12:10", "12:30", "12:50", "13:14", "13:48", "14:03", "14:48", "15:12", "15:32",
             "15:47", "16:02", "16:24", "17:00", "17:16", "17:36", "17:50", "18:30", "18:48", "19:26", "20:23", "21:23"]

полит22_1 = ["6:10", "6:30", "6:58", "7:22", "7:44", "8:10", "8:22", "8:46", "9:00", "9:34", "9:58", "10:28", "10:52",
             "11:22", "11:46", "12:10", "12:20", "12:40", "13:00", "13:24", "13:58", "14:13", "14:58", "15:22", "15:42",
             "15:57", "16:12", "16:34", "17:10", "17:26", "17:46", "18:00", "18:40", "18:58", "19:36", "20:33", "21:33"]

вок22_1 =   ["6:19", "6:39", "7:07", "7:31", "7:53", "8:19", "8:31", "8:55", "9:09", "9:43", "10:07", "10:37", "11:01",
             "11:31", "11:55", "12:19", "12:29", "12:49", "13:09", "13:33", "14:07", "14:22", "15:07", "15:31", "15:51",
             "16:06", "16:21", "16:43", "17:19", "17:35", "17:55", "18:09", "18:49", "19:07", "19:45", "20:42", "21:42"]

предм22_1 = ["6:28", "6:48", "7:16", "7:40", "8:02", "8:28", "8:40", "9:04", "9:18", "9:52", "10:16", "10:46", "11:10",
             "11:40", "12:04", "12:28", "12:38", "12:58", "13:18", "13:42", "14:16", "14:31", "15:16", "15:40", "16:00",
             "16:15", "16:30", "16:52", "17:28", "17:44", "18:04", "18:18", "18:58", "19:16", "19:54", "20:51", "21:51"]

тика22_1 =  ["6:35", "6:55", "7:23", "7:47", "8:09", "8:35", "8:47", "9:11", "9:25", "9:59", "10:23", "10:53", "11:17",
             "11:47", "12:11", "12:35", "12:45", "13:05", "13:25", "13:49", "14:23", "14:38", "15:23", "15:47", "16:07",
             "16:22", "16:37", "16:59", "17:35", "17:51", "18:11", "18:25", "19:05", "19:23", "20:01", "20:58", "21:58"]

солка20 = ["6:26", "6:46", "7:13", "7:30", "7:50", "8:20", "8:40", "9:00", "9:40", "10:40", "11:00", "11:26", "12:04",
        "12:26", "12:46", "13:10", "13:35", "13:50", "14:10", "14:49", "15:15", "16:00", "16:20", "17:08", "17:20",
        "18:00", "18:20", "19:00", "19:30", "20:00", "21:00"]



предм20 = ["6:41", "7:01", "7:28", "7:45", "8:05", "8:35", "8:55", "9:15", "9:55", "10:55", "11:15", "11:41", "12:19",
        "12:41", "13:01", "13:25", "13:50", "14:05", "14:25", "15:04", "15:30", "16:15", "16:35", "17:23", "17:35",
        "18:15", "18:35", "19:15", "19:45", "20:15", "21:15"]



сосно20_1 = ["6:58", "7:17", "7:45", "8:02", "8:22", "8:52", "9:12", "9:30", "10:10", "11:12", "11:32", "11:56", "12:35",
        "13:00", "13:16", "13:40", "14:07", "14:22", "14:42", "15:22", "15:47", "16:32", "16:52", "17:40", "17:52",
        "18:30", "18:55", "19:30", "20:05", "20:30", "21:30"]



предм20_1 = ["7:13", "7:33", "8:00", "8:17", "8:37", "9:07", "9:27", "9:45", "10:25", "11:27", "11:47", "12:11", "12:50",
             "13:15", "13:31", "13:55", "14:22", "14:37", "14:57", "15:37", "16:02", "16:47", "17:07", "17:55", "18:07",
             "18:45", "19:10", "19:45", "20:20", "20:45", "21:45"]

вок25 = ["6:25", "7:55", "10:45", "12:15", "13:45", "16:45", "18:15"]

предм25 = ["6:33", "8:03", "10:53", "12:23", "13:53", "16:53", "18:23"]

солка25 = ["6:48", "8:18", "11:08", "12:38", "14:08", "17:08", "18:38"]

стариков25 = ["6:56", "8:26", "11:16", "12:46", "14:16", "17:16", "18:46"]

черем25_1 = ["7:10", "8:40", "11:30", "13:00", "14:30", "17:30", "19:00"]

стариков25_1 = ["7:22", "8:52", "11:42", "13:12", "14:42", "17:42", "19:12"]

солка25_1 = ["7:30", "9:00", "11:50", "13:20", "14:50", "17:50", "19:20"]

предм25_1 = ["7:45", "9:15", "12:05", "13:35", "15:05", "18:05", "19:35"]

солка21вых = ["6:17", "6:40", "7:05", "7:20", "7:40", "7:53", "8:10", "8:27", "8:40", "8:55", "9:07", "9:30", "9:45", "10:02",
"10:20", "10:37", "11:08", "11:32", "11:49", "12:15", "12:25", "12:40", "12:55", "13:15", "13:33", "13:52", "14:07", "14:21",
"14:34", "14:51", "15:05", "15:30", "15:50", "16:15", "16:34", "16:52", "17:11", "17:31", "17:41", "17:55", "18:12", "18:28",
"18:52", "19:20", "19:55", "20:35", "21:40"]

мелька21вых = ["6:30", "6:50", "7:05", "7:20", "7:35", "7:55", "8:15", "8:27", "8:42", "8:57", "9:20", "9:45", "10:02", "10:21",
"10:45", "11:00", "11:20", "11:46", "12:00", "12:20", "12:30", "12:40", "13:02", "13:25", "13:45", "14:02", "14:22", "14:42",
"15:00", "15:16", "15:26", "15:42", "16:05", "16:20", "16:40", "17:01", "17:14", "17:26", "17:40", "18:20", "18:50", "19:05",
"19:45", "20:10", "20:45", "21:23"]

солка21 = ["6:20", "6:42", "6:51", "7:00", "7:10", "7:20", "7:30", "7:39", "7:50", "8:00", "8:10", "8:21", "8:31", "8:40",
"8:48", "8:58", "9:07", "9:15", "9:23", "9:33", "9:43", "9:53", "10:05", "10:20", "10:33", "10:47", "11:02", "11:20",
"11:32", "11:41", "11:50", "12:04", "12:15", "12:24", "12:34", "12:43", "12:53", "13:05", "13:22", "13:33", "13:44", "14:00",
"14:10", "14:22", "14:34", "14:44", "14:54", "15:03", "15:13", "15:21", "15:30", "15:40", "15:51", "15:58", "16:05", "16:15",
"16:25", "16:34", "16:43", "16:51", "17:01", "17:11", "17:20", "17:31", "17:39", "17:48", "17:56", "18:03", "18:10", "18:19",
"18:30", "18:43", "18:55", "19:20", "19:42", "20:17", "21:05", "22:04"]

мелька21 = ["6:20", "6:40", "6:50", "7:00", "7:10", "7:20", "7:30", "7:40", "7:50", "8:00", "8:07", "8:17", "8:24", "8:34",
"8:43", "8:53", "9:03", "9:13", "9:23", "9:33", "9:43", "9:53", "10:03", "10:15", "10:29", "10:44", "10:59", "11:10", "11:23",
"11:34", "11:44", "11:52", "12:02", "12:11", "12:20", "12:32", "12:40", "12:50", "13:01", "13:11", "13:25", "13:34", "13:43",
"13:53", "14:02", "14:11", "14:21", "14:31", "14:40", "14:49", "15:04", "15:15", "15:25", "15:34", "15:46", "15:55", "16:02",
"16:11", "16:30", "16:42", "16:52", "17:00", "17:07", "17:15", "17:24", "17:33", "17:41", "17:51", "18:05", "18:20", "18:35",
"18:53", "19:07", "19:18", "19:30", "19:45", "20:10", "20:32", "21:10", "21:56"]


@bot.message_handler(commands=['start'])
def start(message):
    mess = (f'Приветствую вас, <b>{message.from_user.first_name}</b>, Вот все запросы расписания на которые я знаю '
            f'ответы: 1, 3, 4, 4а, 5, 6, 8, 9, 10...119, 122, Канск-Иланск, пригородные, междугородные, Иланск, '
            f'Иланск-Красноярск, Красноярск-Восток. Чтобы я вам ответил, пришлите мне цифру или название маршрута из '
            f'списка выше. Так же я пока что знаю ближайшее время маршрутов 20, 21, 22 и 25, а так же ближайшее время разом '
            f'всех этих маршрутов с остановки "солнечный". Чтобы узнать ближайшее время просто отправьте мне запрос '
            f'"ближайшее время № маршрута", либо "ближайший автобус солнечный", в ближайшем будущем админ меня доработает'
            f'и добавит в меня ближайшее время всех маршрутов города')
    bot.reply_to(message, mess, parse_mode='html')

@bot.message_handler(content_types=["text"])
def send_message(message):
    if message.text.lower() == ('справка'):
       mess = (f'Приветствую вас, <b>{message.from_user.first_name}</b>, Вот все запросы расписания на которые я знаю '
            f'ответы: 1, 3, 4, 4а, 5, 6, 8, 9, 10...119, 122, Канск-Иланск, пригородные, междугородные, Иланск, '
            f'Иланск-Красноярск, Красноярск-Восток. Чтобы я вам ответил, пришлите мне цифру или название маршрута из '
            f'списка выше. Так же я пока что знаю ближайшее время маршрутов 20, 21, 22 и 25, а так же ближайшее время разом '
            f'всех этих маршрутов с остановки "солнечный". Чтобы узнать ближайшее время просто отправьте мне запрос '
            f'"ближайшее время № маршрута", либо "ближайший автобус солнечный". В ближайшем будущем админ меня доработает '
            f' и добавит в меня ближайшее время всех маршрутов города')
       bot.reply_to(message, mess, parse_mode='html')

    date_now = datetime.now()
    now = date_now.strftime("%H:%M")
    time = datetime.strptime(now, "%H:%M")

    time22с = [datetime.strptime(temp, "%H:%M") for temp in солка22]

    ind = bisect.bisect_right(time22с, time)
    if ind < len(солка22):
         солнечный22 = f"Ближайший 22 в {солка22[ind]}"
    else:
         солнечный22 = "нет ближайшего времени"

    time22т = [datetime.strptime(temp, "%H:%M") for temp in тика22]

    ind = bisect.bisect_right(time22т, time)
    if ind < len(тика22):
         текстилка22 = f"Ближайший 22 в {тика22[ind]} - направление солнечный - п. Строителей"
    else:
         текстилка22 = "нет ближайшего времени"

    time22п = [datetime.strptime(temp, "%H:%M") for temp in предм22]

    ind = bisect.bisect_right(time22п, time)
    if ind < len(предм22):
         канпер22 = f"Ближайший 22 в {предм22[ind]} - направление солнечный - п. Строителей"
    else:
         канпер22 = "нет ближайшего времени"

    time22в = [datetime.strptime(temp, "%H:%M") for temp in вок22]

    ind = bisect.bisect_right(time22в, time)
    if ind < len(вок22):
         вокзал22 = f"Ближайший 22 в {вок22[ind]} - направление солнечный - п. Строителей"
    else:
         вокзал22 = "нет ближайшего времени"

    time22пол = [datetime.strptime(temp, "%H:%M") for temp in полит22]

    ind = bisect.bisect_right(time22пол, time)
    if ind < len(полит22):
         политех22 = f"Ближайший 22 в {полит22[ind]} - направление солнечный - п. Строителей"
    else:
         политех22 = "нет ближайшего времени"

    time22_1 = [datetime.strptime(temp, "%H:%M") for temp in пос22_1]

    ind = bisect.bisect_right(time22_1, time)
    if ind < len(пос22_1):
         поселок22_1 = f"Ближайший 22 в {пос22_1[ind]}"
    else:
         поселок22_1 = "нет ближайшего времени"

    time22_1пол = [datetime.strptime(temp, "%H:%M") for temp in полит22_1]

    ind = bisect.bisect_right(time22_1пол, time)
    if ind < len(полит22_1):
         политех22_1 = f"Ближайший 22 в {полит22_1[ind]} - направление п. Строителей - солнечный"
    else:
         политех22_1 = "нет ближайшего времени"

    time22_1в = [datetime.strptime(temp, "%H:%M") for temp in вок22_1]

    ind = bisect.bisect_right(time22_1в, time)
    if ind < len(вок22_1):
         вокзал22_1 = f"Ближайший 22 в {вок22_1[ind]} - направление п. Строителей - солнечный"
    else:
         вокзал22_1 = "нет ближайшего времени"

    time22_1п = [datetime.strptime(temp, "%H:%M") for temp in предм22_1]

    ind = bisect.bisect_right(time22_1п, time)
    if ind < len(предм22_1):
         канпер22_1 = f"Ближайший 22 в {предм22_1[ind]} - направление п. Строителей - солнечный"
    else:
         канпер22_1 = "нет ближайшего времени"

    time22_1т = [datetime.strptime(temp, "%H:%M") for temp in тика22_1]

    ind = bisect.bisect_right(time22_1т, time)
    if ind < len(тика22_1):
         текстилка22_1 = f"Ближайший 22 в {тика22_1[ind]} - направление п. Строителей - солнечный"
    else:
         текстилка22_1 = "нет ближайшего времени"

    if message.text.lower() == ('ближайший 22'):
        mess = (f'Выберите остановку и напишите ее так же как написано тут: солнечный 22, текстильщик, предмостная 22, вокзал 22,'
                f' политехнический, строителей')
        bot.reply_to(message, mess, parse_mode='html')
    if message.text.lower() == ('солнечный 22'):
        bot.reply_to(message, солнечный22)
    if message.text.lower() == ('текстильщик'):
        bot.reply_to(message, текстилка22)
    if message.text.lower() == ('текстильщик'):
        bot.reply_to(message, текстилка22_1)
    if message.text.lower() == ('предмостная 22'):
        bot.reply_to(message, канпер22)
    if message.text.lower() == ('предмостная 22'):
        bot.reply_to(message, канпер22_1)
    if message.text.lower() == ('вокзал 22'):
        bot.reply_to(message, вокзал22)
    if message.text.lower() == ('вокзал 22'):
        bot.reply_to(message, вокзал22_1)
    if message.text.lower() == ('политехнический'):
        bot.reply_to(message, политех22)
    if message.text.lower() == ('политехнический'):
        bot.reply_to(message, политех22_1)
    if message.text.lower() == ('строителей'):
        bot.reply_to(message, поселок22_1)

    date_now = datetime.now()
    now = date_now.strftime("%H:%M")
    time = datetime.strptime(now, "%H:%M")

    time20с = [datetime.strptime(temp, "%H:%M") for temp in солка20]

    ind = bisect.bisect_right(time20с, time)
    if ind < len(солка20):
         солнечный20 = f"Ближайший 20 в {солка20[ind]}"
    else:
         солнечный20 = "нет ближайшего времени"

    time20п = [datetime.strptime(temp, "%H:%M") for temp in предм20]

    ind = bisect.bisect_right(time20п, time)
    if ind < len(предм20):
         канпер20 = f"Ближайший 20 в {предм20[ind]} - направление солнечный - сосновый"
    else:
         канпер20 = "нет ближайшего времени"

    time20_1 = [datetime.strptime(temp, "%H:%M") for temp in сосно20_1]

    ind = bisect.bisect_right(time20_1, time)
    if ind < len(сосно20_1):
         сосновый20_1 = f"Ближайший 20 в {сосно20_1[ind]}"
    else:
         сосновый20_1 = "нет ближайшего времени"

    time20_1п = [datetime.strptime(temp, "%H:%M") for temp in предм20_1]

    ind = bisect.bisect_right(time20_1п, time)
    if ind < len(предм20_1):
         канпер20_1 = f"Ближайший 20 в {предм20_1[ind]} - направление сосновый - солнечный"
    else:
         канпер20_1 = "нет ближайшего времени"

    if message.text.lower() == ('ближайший 20'):
        mess = (f'Выберите остановку и напишите ее так же как написано тут: солнечный 20, предмостная 20, сосновый')
        bot.reply_to(message, mess, parse_mode='html')
    if message.text.lower() == ('солнечный 20'):
        bot.reply_to(message, солнечный20)
    if message.text.lower() == ('предмостная 20'):
        bot.reply_to(message, канпер20)
    if message.text.lower() == ('сосновый'):
        bot.reply_to(message, сосновый20_1)
    if message.text.lower() == ('предмостная 20'):
        bot.reply_to(message, канпер20_1)

    date_now = datetime.now()
    now = date_now.strftime("%H:%M")
    time = datetime.strptime(now, "%H:%M")

    time25в = [datetime.strptime(temp, "%H:%M") for temp in вок25]

    ind = bisect.bisect_right(time25в, time)
    if ind < len(вок25):
        вокзал25 = f"Ближайший 25 в {вок25[ind]}"
    else:
        вокзал25 = "нет ближайшего времени"

    time25п = [datetime.strptime(temp, "%H:%M") for temp in предм25]

    ind = bisect.bisect_right(time25п, time)
    if ind < len(предм25):
        канпер25 = f"Ближайший 25 в {предм25[ind]} - направление вокзал - черемушки"
    else:
        канпер25 = "нет ближайшего времени"

    time25с = [datetime.strptime(temp, "%H:%M") for temp in солка25]

    ind = bisect.bisect_right(time25с, time)
    if ind < len(солка25):
        солнечный25 = f"Ближайший 25 в {солка25[ind]}  - направление вокзал - черемушки"
    else:
        солнечный25 = "нет ближайшего времени"

    time25р = [datetime.strptime(temp, "%H:%M") for temp in стариков25]

    ind = bisect.bisect_right(time25р, time)
    if ind < len(стариков25):
        стариково25 = f"Ближайший 25 в {стариков25[ind]}  - направление вокзал - черемушки"
    else:
        стариково25 = "нет ближайшего времени"

    time25_1 = [datetime.strptime(temp, "%H:%M") for temp in черем25_1]

    ind = bisect.bisect_right(time25_1, time)
    if ind < len(черем25_1):
        черемушки25_1 = f"Ближайший 25 в {черем25_1[ind]}"
    else:
        черемушки25_1 = "нет ближайшего времени"

    time25_1р = [datetime.strptime(temp, "%H:%M") for temp in стариков25_1]

    ind = bisect.bisect_right(time25_1р, time)
    if ind < len(стариков25_1):
        стариково25_1 = f"Ближайший 25 в {стариков25_1[ind]}  - направление черемушки - вокзал"
    else:
        стариково25_1 = "нет ближайшего времени"

    time25_1с = [datetime.strptime(temp, "%H:%M") for temp in солка25_1]

    ind = bisect.bisect_right(time25_1с, time)
    if ind < len(солка25_1):
        солнечный25_1 = f"Ближайший 25 в {солка25_1[ind]}  - направление черемушки - вокзал"
    else:
        солнечный25_1 = "нет ближайшего времени"

    time25_1п = [datetime.strptime(temp, "%H:%M") for temp in предм25_1]

    ind = bisect.bisect_right(time25_1п, time)
    if ind < len(предм25_1):
        канпер25_1 = f"Ближайший 25 в {предм25_1[ind]} - направление черемушки - вокзал"
    else:
        канпер25_1 = "нет ближайшего времени"

    if message.text.lower() == ('ближайший 25'):
        mess = (f'Выберите остановку и напишите ее так же как написано тут: вокзал 25, предмостная 25, солнечный 25, '
                f'стариково, черёмушки')
        bot.reply_to(message, mess, parse_mode='html')
    if message.text.lower() == ('вокзал 25'):
        bot.reply_to(message, вокзал25)
    if message.text.lower() == ('предмостная 25'):
        bot.reply_to(message, канпер25)
    if message.text.lower() == ('предмостная 25'):
        bot.reply_to(message, канпер25_1)
    if message.text.lower() == ('солнечный 25'):
        bot.reply_to(message, солнечный25)
    if message.text.lower() == ('солнечный 25'):
        bot.reply_to(message, солнечный25_1)
    if message.text.lower() == ('стариково'):
        bot.reply_to(message, стариково25)
    if message.text.lower() == ('стариково'):
        bot.reply_to(message, стариково25_1)
    if message.text.lower() == ('черемушки'):
        bot.reply_to(message, черемушки25_1)
    if message.text.lower() == ('черёмушки'):
        bot.reply_to(message, черемушки25_1)

    date_now = datetime.now()
    now = date_now.strftime("%H:%M")
    time = datetime.strptime(now, "%H:%M")

    time21с = [datetime.strptime(temp, "%H:%M") for temp in солка21]

    ind = bisect.bisect_right(time21с, time)
    if ind < len(солка21):
        солнечный21 = f"Ближайший 21 в {солка21[ind]}"
    else:
        солнечный21 = "нет ближайшего времени"

    time21м = [datetime.strptime(temp, "%H:%M") for temp in мелька21]

    ind = bisect.bisect_right(time21м, time)
    if ind < len(мелька21):
        мелькомбинат21 = f"Ближайший 21 в {мелька21[ind]}"
    else:
        мелькомбинат21 = "нет ближайшего времени"

    time21_1с = [datetime.strptime(temp, "%H:%M") for temp in солка21вых]

    ind = bisect.bisect_right(time21_1с, time)
    if ind < len(солка21вых):
        солнечный21вых = f"Ближайший 21 в {солка21вых[ind]} - график выходного и праздничных дней"
    else:
        солнечный21вых = "нет ближайшего времени"

    time21_1м = [datetime.strptime(temp, "%H:%M") for temp in мелька21вых]

    ind = bisect.bisect_right(time21_1м, time)
    if ind < len(мелька21вых):
        мелькомбинат21вых = f"Ближайший 21 в {мелька21вых[ind]} - график выходного и праздничных дней"
    else:
        мелькомбинат21вых = "нет ближайшего времени"

    if message.text.lower() == ('ближайший 21'):
        mess = (f'Выберите остановку и напишите ее так же как написано тут: солнечный 21, мелькомбинат')
        bot.reply_to(message, mess, parse_mode='html')
    if message.text.lower() == ('солнечный 21'):
        bot.reply_to(message, солнечный21)
    if message.text.lower() == ('солнечный 21'):
        bot.reply_to(message, солнечный21вых)
    if message.text.lower() == ('мелькомбинат'):
        bot.reply_to(message, мелькомбинат21)
    if message.text.lower() == ('мелькомбинат'):
        bot.reply_to(message, мелькомбинат21вых)

    if message.text.lower() == ('ближайший автобус солнечный'):
        bot.reply_to(message, солнечный20)
    if message.text.lower() == ('ближайший автобус солнечный'):
        bot.reply_to(message, солнечный21)
    if message.text.lower() == ('ближайший автобус солнечный'):
        bot.reply_to(message, солнечный21вых)
    if message.text.lower() == ('ближайший автобус солнечный'):
        bot.reply_to(message, солнечный22)
    if message.text.lower() == ('ближайший автобус солнечный'):
        bot.reply_to(message, солнечный25)
    if message.text.lower() == ('ближайший автобус солнечный'):
        bot.reply_to(message, солнечный25_1)



    if message.text == "1":
        bot.send_photo(message.chat.id, open('1.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "3":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('3.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('3.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "4":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('4.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('4.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "4а":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('4а.1.jpg', 'rb')),
                                              telebot.types.InputMediaPhoto(open('4а.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "5":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('5.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('5.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "6":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('6.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('6.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)

    if message.text == "8":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('8.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('8.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "9":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('9.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('9.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "10":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('10.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('10.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)

    if message.text == "13":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('13.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('13.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('13.3.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "14":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('14.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('14.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('15.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('15.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('15.3.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('15.4.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "17":
        bot.send_photo(message.chat.id, open('17.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "19":
        bot.send_photo(message.chat.id, open('19.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "20":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('20.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('20.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('20.3.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('20.4.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)

    if message.text == "21":
        bot.send_photo(message.chat.id, open('21.1.jpg', 'rb'),reply_to_message_id=message.message_id)
    if message.text == "21":
        text = f"Графики выходного дня"
        bot.send_photo(message.chat.id, open('21.2.jpg', 'rb'), caption=text, parse_mode="HTML", reply_to_message_id=message.message_id)

    if message.text == "21":
        text1 = f"Графики выходного дня"
        bot.send_photo(message.chat.id, open('21.3.jpg', 'rb'), caption=text1, parse_mode="HTML", reply_to_message_id=message.message_id)

    if message.text == "22":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('22.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('22.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('22.3.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('22.4.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('22.5.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('22.6.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('22.7.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "23":
        bot.send_photo(message.chat.id, open('23.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "24":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('24.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('24.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "25":
        bot.send_photo(message.chat.id, open('25.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "103":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('103.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('103.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "104":
        bot.send_photo(message.chat.id, open('104.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "105":
        bot.send_photo(message.chat.id, open('105.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "118":
        bot.send_photo(message.chat.id, open('118.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "119":
        bot.send_photo(message.chat.id, open('119.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "122":
        bot.send_photo(message.chat.id, open('122.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text.lower() == "канск-иланск":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('141.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('141.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('141.3.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('141.4.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text.lower() == "пригородные":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('пригород1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('пригород2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text.lower() == "междугородные":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('межгород1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('межгород2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('межгород3.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text.lower() == "иланск":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('иланск1.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('иланск1.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('иланск1.3.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('иланск2.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('иланск2.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('иланск3.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('иланск129.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text.lower() == "иланск-красноярск":
        bot.send_photo(message.chat.id, open('иланск красноярск.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text.lower() == "красноярск-восток":
        bot.send_photo(message.chat.id, open('красноярсквосток.jpg', 'rb'), reply_to_message_id=message.message_id)




bot.polling(none_stop=True)
