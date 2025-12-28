import telebot
from telebot import types
from dotenv import load_dotenv
import os
import pytz

load_dotenv()

bot = telebot.TeleBot(os.getenv('TOKEN'))

from datetime import datetime
import bisect


солка1 = ["05:40","05:55","06:05","06:15","06:25","06:34","06:42","06:49","06:58","07:03","07:11","07:18","07:23","07:28",
          "07:33","07:37","07:42","07:47","07:52","07:57","08:01","08:05","08:10","08:14","08:20","08:25","08:30","08:34",
          "08:40","08:45","08:49","08:54","08:58","09:03","09:07","09:11","09:13","09:19","09:20","09:28","09:30","09:38",
          "09:40","09:48","09:50","09:58","09:59","10:03","10:08","10:16","10:17","10:26","10:29","10:33","10:38","10:39",
          "10:49","10:57","11:00","11:02","11:08","11:09","11:17","11:18","11:26","11:28","11:36","11:38","11:46","11:53",
          "11:58","12:02","12:07","12:15","12:23","12:27","12:33","12:37","12:42","12:46","12:51","12:55","13:01","13:05",
          "13:09","13:14","13:18","13:23","13:28","13:33","13:39","13:44","13:48","13:53","13:57","14:02","14:07","14:12",
          "14:17","14:21","14:24","14:25","14:30","14:34","14:40","14:43","14:45","14:50","14:54","15:00","15:03","15:04",
          "15:09","15:12","15:13","15:18","15:22","15:23","15:27","15:31","15:33","15:37","15:42","15:44","15:46","15:50",
          "15:55","16:00","16:06","16:10","16:15","16:20","16:25","16:30","16:33","16:34","16:39","16:43","16:48","16:52",
          "16:56","17:03","17:11","17:16","17:19","17:20","17:27","17:29","17:35","17:40","17:45","17:53","17:54","17:58",
          "18:03","18:09","18:18","18:21","18:29","18:31","18:37","18:46","18:55","19:01","19:04","19:15","19:27","19:28",
          "19:38","19:51","19:57","20:06","20:14","20:22","20:29","20:37","20:44","20:50","20:59","21:07","21:15","21:22",
          "21:30","21:37","21:45","21:47","21:57","22:00","22:15","22:19","22:32","22:36","22:40","22:55","22:56","23:16",
          "23:25","23:43"]


колектор1 = ["06:17","06:31","06:42","06:52","06:58","07:02","07:11","07:17","07:19","07:26","07:31","07:34","07:40",
             "07:43","07:55","08:00","08:05","08:10","08:14","08:19","08:24","08:29","08:34","08:38","08:42","08:47",
             "08:51","08:57","09:01","09:07","09:11","09:17","09:22","09:26","09:31","09:35","09:40","09:44","09:50",
             "09:56","10:15","10:27","10:35","10:45","10:53","11:03","11:10","11:16","11:26","11:34","11:39","11:46",
             "11:54","12:05","12:23","12:30","12:35","12:39","12:44","12:52","13:00","13:04","13:10","13:14","13:19",
             "13:23","13:28","13:32","13:38","13:42","13:46","13:51","13:55","14:00","14:05","14:10","14:16","14:21",
             "14:25","14:30","14:34","14:39","14:44","14:49","14:54","14:58","15:02","15:07","15:11","15:17","15:22",
             "15:26","15:31","15:37","15:41","15:46","15:50","15:55","16:00","16:04","16:10","16:14","16:19","16:23",
             "16:27","16:32","16:37","16:43","16:47","16:52","16:56","17:02","17:07","17:11","17:16","17:20","17:25",
             "17:30","17:40","17:48","17:56","18:04","18:22","18:31","18:46","18:55","19:08","19:29","19:38","19:52",
             "20:04","20:30","20:34","20:43","20:51","20:59","21:06","21:14","21:21","21:27","21:37","21:46","21:52",
             "21:59","22:07","22:14","22:22","22:34","22:52","23:10","23:29","23:49"]


вок9 = ["05:50","06:30","06:46","07:24","07:48","08:16","08:47","09:49","10:09","11:08","11:36","12:04","12:34","13:07",
        "13:36","14:35","15:03","15:32","16:03","16:30","17:02","17:42","18:00","18:36","20:27","21:25"]

корост9 = ["05:53", "06:33", "06:49", "07:27", "07:51", "08:19", "08:50", "09:52", "10:11", "11:11", "11:39", "12:07",
           "12:37", "13:10", "13:39", "14:38", "15:06", "15:35", "16:06", "16:33", "17:05", "17:45", "18:03", "18:39",
           "20:30", "21:28"]

полит9 = ["06:01","06:41","06:57","07:35","07:59","08:27","08:58","10:00","10:19","11:19","11:47","12:15","12:45","13:18",
          "13:47","14:46","15:14","15:43","16:14","16:41","17:13","17:53","18:11","18:47","20:38","21:36"]

краев9 = ["06:18","06:59","07:17","07:50","08:16","08:47","09:18","10:17","10:37","11:36","12:04","12:36","13:05","13:35",
          "14:04","15:03","15:33","16:03","16:34","17:03","17:29","18:09","18:28","19:04","20:55","21:53"]

полит_9 = ["06:33","07:13","07:32","08:04","08:31","09:02","09:33","10:32","10:52","11:51","12:19","12:51","13:20","13:50",
           "14:19","15:18","15:48","16:18","16:49","17:18","17:44","18:24","18:43","19:19","21:10","22:08"]

корост_9 = ["06:41","07:20","07:40","08:12","08:39","09:10","09:41","10:40","11:00","12:00","12:27","12:59","13:28","13:58",
            "14:27","15:26","15:56","16:26","16:57","17:26","17:54","18:32","18:51","19:27","21:18","22:16"]






солка22 = ["6:25", "6:50", "7:15", "7:40", "8:05", "8:30", "8:55", "9:20", "9:45", "10:55", "11:45", "12:10", "12:35",
           "13:00", "13:25", "13:50", "14:15", "14:40", "15:05", "15:55", "16:45", "17:10", "17:35", "18:00", "18:45",
           "19:05", "19:55", "20:45", "21:35", "22:25"]

предм22 = ["6:40", "7:05", "7:30", "7:55", "8:20", "8:45", "9:10", "9:35", "10:00", "11:10", "12:00", "12:25", "12:50",
           "13:15", "13:40", "14:05", "14:30", "14:55", "15:20", "16:10", "17:00", "17:25", "17:50", "18:15", "19:00",
           "19:20", "20:10", "21:00", "21:50", "22:40"]

вок22 =   ["5:35", "6:00", "6:25", "6:50", "7:15", "7:40", "8:05", "8:30", "8:55", "9:20", "9:45", "11:20", "11:45",
           "12:10", "12:35", "13:00", "13:25", "13:50", "14:15", "14:40", "15:30", "16:20", "16:45", "17:10", "17:35",
           "18:00", "18:25", "19:10", "19:30", "20:20", "21:10", "22:00", "22:50"]

полит22 = ["5:45", "6:10", "6:35", "7:00", "7:25", "7:50", "8:15", "8:40", "9:05", "9:30", "9:55", "11:30", "11:55",
           "12:20", "12:45", "13:10", "13:35", "14:00", "14:25", "14:50", "15:40", "16:30", "16:55", "17:20", "17:45",
           "18:10", "18:35", "19:20", "19:40", "20:30", "21:20", "22:10", "23:00"]

пос22_1 =   ["6:00", "6:25", "6:50", "7:15", "7:40", "8:05", "8:30", "8:55", "9:20", "9:45", "10:10", "11:45", "12:10",
             "12:35", "13:00", "13:25", "13:50", "14:15", "14:40", "15:05", "15:55", "16:45", "17:10", "17:35", "18:00",
             "18:25", "18:50", "19:35", "19:55", "20:45", "21:35", "22:25"]

полит22_1 = ["6:10", "6:35", "7:00", "7:25", "7:50", "8:15", "8:40", "9:05", "9:30", "9:55", "10:20", "11:55", "12:20",
             "12:45", "13:10", "13:35", "14:00", "14:25", "14:50", "15:15", "16:05", "16:55", "17:20", "17:45", "18:10",
             "18:35", "19:00", "19:45", "20:05", "20:55", "21:45", "22:35"]

вок22_1 =   ["6:20", "6:45", "7:10", "7:35", "8:00", "8:25", "8:50", "9:15", "10:25", "11:15", "11:40", "12:05", "12:30",
             "12:55", "13:20", "13:45", "14:10", "14:35", "15:00", "15:25", "16:15", "17:05","17:30", "17:55", "18:20",
             "18:45", "19:10", "20:15", "21:05", "21:55"]

предм22_1 = ["6:30", "6:55", "7:20", "7:45", "8:10", "8:35", "9:00", "9:25", "10:35", "11:25", "11:50", "12:15", "12:40",
             "13:05", "13:30", "13:55", "14:20", "14:45", "15:10", "15:35", "16:25", "17:15", "17:40", "18:05", "18:30",
             "18:55", "19:20", "20:25", "21:15", "22:05"]



солка20 = ["6:26", "6:46", "7:06", "7:30", "7:50", "8:08", "8:40", "9:00", "9:18", "9:32", "10:40", "11:00", "11:20",
           "11:44", "12:04", "12:26", "12:46", "13:10", "13:26", "13:46", "14:10", "14:29", "14:49", "15:15", "15:37",
           "16:08", "16:20", "16:42", "17:08", "17:33", "18:00", "18:32", "19:00", "19:28", "20:00", "20:29", "21:00"]

предм20 = ["06:41", "07:01", "07:21", "07:45", "08:05", "08:21", "08:55", "09:15", "09:31", "09:47", "10:55", "11:15",
           "11:35", "11:59", "12:19", "12:41", "13:01", "13:25", "13:41", "14:01", "14:25", "14:44", "15:04", "15:30",
           "15:51", "16:23", "16:35", "16:57", "17:23", "17:48", "18:15", "18:47", "19:15", "19:43", "20:15", "20:44",
           "21:15"]

сосно20_1 = ["6:58", "7:17", "7:38", "8:02", "8:22", "8:48", "9:12", "9:30", "9:48", "10:10", "11:12", "11:32", "11:56",
             "12:15", "12:35", "12:56", "13:16", "13:40", "13:57", "14:18", "14:42", "15:06", "15:22", "15:47", "16:10",
             "16:38", "16:52", "17:17", "17:50", "18:03", "18:30", "19:03", "19:30", "19:59", "20:30", "21:00", "21:30"]

предм20_1 = ["07:13", "07:33", "07:53", "08:17", "08:37", "09:01", "09:27", "09:45", "10:01", "10:25", "11:17", "11:47",
             "12:11", "12:30", "12:50", "13:11", "13:31", "13:55", "14:12", "14:33", "14:57", "15:21", "15:37", "16:02",
             "16:25", "16:53", "17:07", "17:32", "18:05", "18:17", "18:45", "19:18", "19:45", "20:14", "20:45", "21:15",
             "21:45"]


солка21вых = ["6:17", "6:40", "7:05", "7:20", "7:40", "7:53", "8:10", "8:27", "8:40", "8:55", "9:07", "9:30", "9:45", "10:02",
"10:20", "10:37", "11:08", "11:32", "11:49", "12:15", "12:25", "12:40", "12:55", "13:15", "13:33", "13:52", "14:07", "14:21",
"14:34", "14:53", "15:05", "15:30", "15:50", "16:15", "16:34", "16:52", "17:11", "17:31", "17:41", "17:55", "18:12", "18:28",
"18:52", "19:20", "19:55", "20:35", "21:40"]

мелька21вых = ["6:30", "6:50", "7:05", "7:20", "7:35", "7:55", "8:15", "8:27", "8:42", "8:57", "9:20", "9:45", "10:02", "10:21",
"10:45", "11:00", "11:20", "11:46", "12:00", "12:20", "12:30", "12:40", "13:02", "13:25", "13:45", "14:02", "14:22", "14:42",
"15:00", "15:16", "15:25", "15:44", "16:05", "16:20", "16:40", "17:01", "17:14", "17:26", "18:20", "18:50", "19:04",
"19:45", "20:10", "20:47", "21:23"]

солка21 = ["6:20", "6:40", "6:50", "7:00", "7:10", "7:20", "7:30", "7:39", "7:50", "8:00", "8:10", "8:21", "8:31", "8:40",
"8:48", "8:58", "9:07", "9:15", "9:23", "9:33", "9:43", "9:53", "10:05", "10:20", "10:33", "10:47", "11:02", "11:20", "11:32",
"11:40", "11:50", "12:04", "12:15", "12:24", "12:34", "12:43", "12:53", "13:05", "13:22", "13:33", "13:44", "14:00", "14:10",
"14:22", "14:34", "14:44", "14:54", "15:03", "15:13", "15:21", "15:30", "15:40", "15:51", "15:58", "16:05", "16:15", "16:25",
"16:34", "16:43", "16:51", "17:01", "17:11", "17:20", "17:31", "17:39", "17:48", "17:56", "18:03", "18:14", "18:30", "18:43",
"18:55", "19:20", "19:42", "20:17", "21:05", "22:04"]

мелька21 = ["6:20", "6:40", "6:50", "7:00", "7:10", "7:20", "7:30", "7:40", "7:50", "8:00", "8:07", "8:17", "8:24", "8:34",
"8:43", "8:53", "9:03", "9:13", "9:23", "9:33", "9:43", "9:53", "10:03", "10:15", "10:29", "10:44", "10:59", "11:10", "11:23",
"11:34", "11:44", "11:52", "12:02", "12:11", "12:20", "12:32", "12:40", "12:50", "13:01", "13:11", "13:25", "13:34", "13:43",
"13:53", "14:02", "14:11", "14:21", "14:31", "14:40", "14:49", "15:04", "15:15", "15:25", "15:34", "15:46", "15:55", "16:02",
"16:11", "16:20", "16:30", "16:42", "16:52", "17:00", "17:07", "17:15", "17:24", "17:33", "17:41", "17:51", "18:05", "18:20", "18:35",
"18:53", "19:07", "19:18", "19:30", "19:45", "20:10", "20:32", "21:10", "21:56"]


@bot.message_handler(commands=['menu'])
def menu(message):
    mess = (f'Приветствую вас , <b>{message.from_user.first_name}</b> 👋 . Тут вы можете найти все расписание города,'
            f'района, а так же пригородное и междугородное расписание. Используйте кнопу меню, чтобы найти нужный вам маршрут')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button1)
    bot.reply_to(message, mess, reply_markup=keyboard, parse_mode='html')

@bot.message_handler(func=lambda message: message.text == '🚍 Меню 🚍')
def menu(message):
    mess = ('⬇️ Выберите пункт ⬇️')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('📜 Расписание')
    button2 = types.KeyboardButton('🚌 Ближайший автобус')
    button3 = types.KeyboardButton('Как доехать до остановки ❓')
    keyboard.row(button1, button2).add(button3)
    bot.reply_to(message, mess, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == '📜 Расписание')
def raspisanie(message):
    mess = ('⬇️ Выберите категорию маршрутов ⬇️')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("🟢Городские")
    button2 = types.KeyboardButton("🟢Пригородные")
    button3 = types.KeyboardButton("🟢Междугородные")
    button4 = types.KeyboardButton("🟢Иланск")
    button5 = types.KeyboardButton("🟢Красноярск-восток")
    button6 = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button2).add(button3, button4).add(button5, button6)
    bot.reply_to(message, mess, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == '🟢Городские')
def gorodskie(message):
    mess = ('⬇️ Выберите маршрут ⬇️')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("1️⃣")
    button2 = types.KeyboardButton("3️⃣")
    button3a = types.KeyboardButton("3️⃣а")
    button3 = types.KeyboardButton("5️⃣")
    button4 = types.KeyboardButton("8️⃣")
    button5 = types.KeyboardButton("9️⃣")
    button6 = types.KeyboardButton("1️⃣0️⃣")
    button7 = types.KeyboardButton("1️⃣3️⃣")
    button8 = types.KeyboardButton("1️⃣️️5️⃣")
    button9 = types.KeyboardButton("1️⃣7️⃣")
    button10 = types.KeyboardButton("1️⃣9️⃣")
    button11 = types.KeyboardButton("2️⃣0️⃣")
    button12 = types.KeyboardButton("2️⃣1️⃣")
    button13 = types.KeyboardButton("2️⃣2️⃣")
    button14 = types.KeyboardButton("2️⃣3️⃣")
    button15 = types.KeyboardButton("2️⃣4️⃣")
    button16 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button103u = types.KeyboardButton("1️⃣0️⃣3️⃣у")
    button17 = types.KeyboardButton("1️⃣0️⃣4️⃣")
    button18 = types.KeyboardButton("1️⃣0️⃣️5️⃣")
    button19 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button20 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button21 = types.KeyboardButton("1️⃣2️⃣2️⃣")
    button22 = types.KeyboardButton("📜 Расписание")
    button23 = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button1, button2, button3a, button3, button4,  button5,  button6,  button7,  button8,  button9, button10,
                 button11, button12, button13,  button14,  button15,  button16,  button103u ,  button17, button18, button19, button20,
                 button21, button22,  button23)
    bot.reply_to(message, mess, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == '🚌 Ближайший автобус')
def bas(message):
    mess = ('⬇️ Выберите маршрут ⬇️')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("Ближайший 1")
    button9=  types.KeyboardButton("Ближайший 9")
    button20 = types.KeyboardButton("Ближайший 20")
    button21 = types.KeyboardButton("Ближайший 21")
    button22 = types.KeyboardButton("Ближайший 22")
    button = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button9).add(button20, button21).add(button22).add(button)
    bot.reply_to(message, mess, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == '↩️ Назад')
def назад(message):
    mess = ('⬇️ Выберите маршрут ⬇️')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("Ближайший 1")
    button9 = types.KeyboardButton("Ближайший 9")
    button20 = types.KeyboardButton("Ближайший 20")
    button21 = types.KeyboardButton("Ближайший 21")
    button22 = types.KeyboardButton("Ближайший 22")
    button = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button9).add(button20, button21).add(button22).add(button)
    bot.reply_to(message, mess, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Ближайший 1')
def ближайший_1(message):
    mess = ('⬇️ Выберите остановку ⬇️')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("Солнечный 1")
    button2 = types.KeyboardButton("Коллекторная")
    button3 = types.KeyboardButton("↩️ Назад")
    button4 = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button2).add(button3, button4)
    bot.reply_to(message, mess, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Ближайший 9')
def ближайший_9(message):
    mess = ('⬇️ Выберите остановку ⬇️')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("Вокзал 9")
    button2 = types.KeyboardButton("площадь коростелева 9")
    button3 = types.KeyboardButton("Политехнический 9")
    button4 = types.KeyboardButton("ул. краевая")
    button5 = types.KeyboardButton("↩️ Назад")
    button6 = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button2).add(button3, button4).add(button5, button6)
    bot.reply_to(message, mess, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Ближайший 20')
def ближайший_21(message):
    mess = ('⬇️ Выберите остановку ⬇️')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("Солнечный 20")
    button2 = types.KeyboardButton("Предмостная 20")
    button3 = types.KeyboardButton("Сосновый 20")
    button4 = types.KeyboardButton("↩️ Назад")
    button5 = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button2, ).add(button3, button4).add(button5)
    bot.reply_to(message, mess, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Ближайший 21')
def ближайший_21(message):
    mess = ('⬇️ Выберите остановку ⬇️')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("Солнечный 21")
    button2 = types.KeyboardButton("Мелькомбинат 21")
    button3 = types.KeyboardButton("↩️ Назад")
    button4 = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button2).add(button3, button4)
    bot.reply_to(message, mess, reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text == 'Ближайший 22')
def ближайший_22(message):
    mess = ('⬇️ Выберите остановку ⬇️')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("Солнечный 22")
    button2 = types.KeyboardButton("Предмостная 22")
    button3 = types.KeyboardButton("Вокзал 22")
    button4 = types.KeyboardButton("Политехнический 22")
    button5 = types.KeyboardButton("Строителей 22")
    button6 = types.KeyboardButton("↩️ Назад")
    button7 = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button2).add(button3, button4).add(button5, button6).add(button7)
    bot.reply_to(message, mess, reply_markup=keyboard)


stops = [
    "Солнечный", "МЖК", "Северо - западный", "Ремзавод", "Стадион текстильщик",
    "Драм театр (порт - артур)", "Восход", "Предмостная", "Золотой ключик (набережная)",
    "Лицей 1", "Магазин геолог", "Школа 15", "Нефтебаза", "Туб.санаторий", "Сосновый",
    "семиполатинский лзу (красэко)", "Ново - канский лпх", "Стрижевой", "дрсу - 3",
    "Подсобное", "Агроснаб", "Соленое", "Абанское кладбище", "Пед.колледж", "Стариково",
    "Черемушки", "дсу - 4", "ДОСААФ", "ЗЛМК", "ККЗ", "Анцирь", "Чечеул", "Зеленый Луг",
    "Новый Путь", "Строителей", "Школа 8", "Краевая (гавань)", "БХЗ", "Гор.больница",
    "Политехнический", "ГИБДД", "Автоколона 1261", "5 городок", "4 городок", "ПАТП",
    "Мелькомбинат", "Эйдемана", "Гор.сад", "Площадь Коростелева", "Ж/Д вокзал (автовокзал)",
    "Кинотеатр Космос", "Кинотеатр Север", "Детская больница (север)", "СИЗО", "Мясокомбинат",
    "Коллекторная ул.", "Кан", "Рассвет", "Бережки", "Левобережное", "Бражное",
    "Филимоново", "Сухая речка"
]

def create_stop_keyboard():
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    for stop in stops:
        keyboard.add(types.KeyboardButton(stop))
    keyboard.add(types.KeyboardButton("🚍 Меню 🚍"))
    return keyboard

@bot.message_handler(func=lambda message: message.text.lower() == 'как доехать до остановки ❓')
def handle_stop_request(message):
    bot.reply_to(message,"Выберите нужную остановку из списка ниже:", reply_markup=create_stop_keyboard())
    
@bot.message_handler(func=lambda message: message.text.lower() == 'солнечный')
def солнечный(message):
    mess = (f'Доехать до остановки "солнечный" можно на маршрутах: 1, 10, 17, 20, 21, 22, 23, 103, 103у, 104, 118,  '
            f'119. Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть где находится на карте '
            f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("1️⃣")
    button2 = types.KeyboardButton("1️⃣0️⃣")
    button3 = types.KeyboardButton("1️⃣7️⃣")
    button4 = types.KeyboardButton("2️⃣0️⃣")
    button5 = types.KeyboardButton("2️⃣1️⃣")
    button6 = types.KeyboardButton("2️⃣2️⃣")
    button7 = types.KeyboardButton("2️⃣3️⃣")
    button8 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button9 = types.KeyboardButton("1️⃣0️⃣4️⃣")
    button10 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button11= types.KeyboardButton("1️⃣1️⃣9️⃣")
    button12 = types.KeyboardButton("Как доехать до остановки ❓")
    button13 = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button2).add(button3, button4).add(button5, button6).add(button7,
                 button8).add(button9, button10).add(button11).add(button12, button13)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDssv8jS", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'мжк')
def mjk(message):
    mess = (f'Доехать до остановки "МЖК" можно на маршрутах: 1, 10 , 17, 20, 21, 22, 23, 103, 103у, 104, 118,  '
            f'119.  '
            f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
            f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("1️⃣")
    button4a = types.KeyboardButton("")
    button10 = types.KeyboardButton("1️⃣0️⃣")
    button17 = types.KeyboardButton("1️⃣7️⃣")
    button20 = types.KeyboardButton("2️⃣0️⃣")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button22 = types.KeyboardButton("2️⃣2️⃣")
    button23 = types.KeyboardButton("2️⃣3️⃣")
    button25 = types.KeyboardButton("")
    button103 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button103u = types.KeyboardButton("1️⃣0️⃣3️⃣у")
    button104 = types.KeyboardButton("1️⃣0️⃣4️⃣")
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button4a).add(button10, button17).add(button20, button21)
    keyboard.add(button22, button23).add(button25, button103).add(button103u, button104)
    keyboard.add(button118, button119).add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTBN4W", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'северо - западный')
def severo_zapadniy(message):
    mess = (f'Доехать до остановки "Северо‑Западный" можно на маршрутах: 1, 10, 17, 20, 21, 22, 23, 103, 103у, 104, 118, 119. '
            f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
            f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("1️⃣")
    button4a = types.KeyboardButton("")
    button10 = types.KeyboardButton("1️⃣0️⃣")
    button17 = types.KeyboardButton("1️⃣7️⃣")
    button20 = types.KeyboardButton("2️⃣0️⃣")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button22 = types.KeyboardButton("2️⃣2️⃣")
    button23 = types.KeyboardButton("2️⃣3️⃣")
    button25 = types.KeyboardButton("")
    button103 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button103u = types.KeyboardButton("1️⃣0️⃣3️⃣у")
    button104 = types.KeyboardButton("1️⃣0️⃣4️⃣")
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button4a).add(button10, button17).add(button20, button21)
    keyboard.add(button22, button23).add(button25, button103).add(button103u, button104)
    keyboard.add(button118, button119).add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTFY4b", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'ремзавод')
def remzavod(message):
    mess = (f'Доехать до остановки "Ремзавод" можно на маршрутах: 1, 10, 15, 17, 19, 20, 21, 22, 23, 103, 103у, 104, 118, 119, 122. '
            f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
            f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("1️⃣")
    button4 = types.KeyboardButton("")
    button4a = types.KeyboardButton("")
    button6 = types.KeyboardButton("")
    button10 = types.KeyboardButton("1️⃣0️⃣")
    button14 = types.KeyboardButton("")
    button15 = types.KeyboardButton("1️⃣5️⃣")
    button17 = types.KeyboardButton("1️⃣7️⃣")
    button19 = types.KeyboardButton("1️⃣9️⃣")
    button20 = types.KeyboardButton("2️⃣0️⃣")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button22 = types.KeyboardButton("2️⃣2️⃣")
    button23 = types.KeyboardButton("2️⃣3️⃣")
    button25 = types.KeyboardButton("")
    button103 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button103u = types.KeyboardButton("1️⃣0️⃣3️⃣у")
    button104 = types.KeyboardButton("1️⃣0️⃣4️⃣")
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button122 = types.KeyboardButton("1️⃣2️⃣2️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button4).add(button4a, button6).add(button10, button14)
    keyboard.add(button15, button17).add(button19, button20).add(button21, button22)
    keyboard.add(button23, button25).add(button103, button103u).add(button104, button118)
    keyboard.add(button119, button122).add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTJD1x", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'стадион текстильщик')
def stadion_tekstilschik(message):
    mess = (f'Доехать до остановки "стадион текстильщик" можно на маршрутах: 1, 10, 15, 17, 19, 20, 21, 22, 23, 103, 103у, 104, 118, 119, 122. '
            f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
            f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("1️⃣")
    button4 = types.KeyboardButton("")
    button4a = types.KeyboardButton("")
    button6 = types.KeyboardButton("")
    button10 = types.KeyboardButton("1️⃣0️⃣")
    button14 = types.KeyboardButton("")
    button15 = types.KeyboardButton("1️⃣5️⃣")
    button17 = types.KeyboardButton("1️⃣7️⃣")
    button19 = types.KeyboardButton("1️⃣9️⃣")
    button20 = types.KeyboardButton("2️⃣0️⃣")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button22 = types.KeyboardButton("2️⃣2️⃣")
    button23 = types.KeyboardButton("2️⃣3️⃣")
    button25 = types.KeyboardButton("")
    button103 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button103u = types.KeyboardButton("1️⃣0️⃣3️⃣у")
    button104 = types.KeyboardButton("1️⃣0️⃣4️⃣")
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button122 = types.KeyboardButton("1️⃣2️⃣2️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button4).add(button4a, button6).add(button10, button14)
    keyboard.add(button15, button17).add(button19, button20).add(button21, button22)
    keyboard.add(button23, button25).add(button103, button103u).add(button104, button118)
    keyboard.add(button119, button122).add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTNNyC", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'драм театр (порт - артур)')
def dram_teatr(message):
    mess = (f'Доехать до остановки "драм театр" можно на маршрутах: 1, 10, 15, 17, 19, 20, 21, 22, 23, 103, 103у, 104, 118, 119, 122. '
            f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
            f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("1️⃣")
    button4 = types.KeyboardButton("")
    button4a = types.KeyboardButton("")
    button6 = types.KeyboardButton("")
    button10 = types.KeyboardButton("1️⃣0️⃣")
    button14 = types.KeyboardButton("")
    button15 = types.KeyboardButton("1️⃣5️⃣")
    button17 = types.KeyboardButton("1️⃣7️⃣")
    button19 = types.KeyboardButton("1️⃣9️⃣")
    button20 = types.KeyboardButton("2️⃣0️⃣")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button22 = types.KeyboardButton("2️⃣2️⃣")
    button23 = types.KeyboardButton("2️⃣3️⃣")
    button25 = types.KeyboardButton("")
    button103 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button103u = types.KeyboardButton("1️⃣0️⃣3️⃣у")
    button104 = types.KeyboardButton("1️⃣0️⃣4️⃣")
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button122 = types.KeyboardButton("1️⃣2️⃣2️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button4).add(button4a, button6).add(button10, button14)
    keyboard.add(button15, button17).add(button19, button20).add(button21, button22)
    keyboard.add(button23, button25).add(button103, button103u).add(button104, button118)
    keyboard.add(button119, button122).add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTRJyj", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'восход')
def voshod(message):
    mess = (f'Доехать до остановки "восход" можно на маршрутах: 1, 10, 15, 17, 19, 20, 21, 22, 23, 103, 103у, 104, 118, 119, 122. '
           f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("1️⃣")
    button4 = types.KeyboardButton("")
    button4a = types.KeyboardButton("")
    button6 = types.KeyboardButton("")
    button10 = types.KeyboardButton("1️⃣0️⃣")
    button14 = types.KeyboardButton("")
    button15 = types.KeyboardButton("1️⃣5️⃣")
    button17 = types.KeyboardButton("1️⃣7️⃣")
    button19 = types.KeyboardButton("1️⃣9️⃣")
    button20 = types.KeyboardButton("2️⃣0️⃣")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button22 = types.KeyboardButton("2️⃣2️⃣")
    button23 = types.KeyboardButton("2️⃣3️⃣")
    button25 = types.KeyboardButton("")
    button103 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button103u = types.KeyboardButton("1️⃣0️⃣3️⃣у")
    button104 = types.KeyboardButton("1️⃣0️⃣4️⃣")
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button122 = types.KeyboardButton("1️⃣2️⃣2️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button4).add(button4a, button6).add(button10, button14)
    keyboard.add(button15, button17).add(button19, button20).add(button21, button22)
    keyboard.add(button23, button25).add(button103, button103u).add(button104, button118)
    keyboard.add(button119, button122).add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTR0p-", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'предмостная')
def predmostnaya(message):
    mess = (f'Доехать до остановки "предмостная" можно на маршрутах: 1, 3, 10, 13, 15, 17, 19, 20, 21,'
           f' 22, 23, 24, 103, 103у, 104, 118, 119, 122. '
           f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("1️⃣")
    button3 = types.KeyboardButton("3️⃣")
    button4 = types.KeyboardButton("")
    button4a = types.KeyboardButton("")
    button6 = types.KeyboardButton("")
    button10 = types.KeyboardButton("1️⃣0️⃣")
    button13 = types.KeyboardButton("1️⃣3️⃣")
    button14 = types.KeyboardButton("")
    button15 = types.KeyboardButton("1️⃣5️⃣")
    button17 = types.KeyboardButton("1️⃣7️⃣")
    button19 = types.KeyboardButton("1️⃣9️⃣")
    button20 = types.KeyboardButton("2️⃣0️⃣")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button22 = types.KeyboardButton("2️⃣2️⃣")
    button23 = types.KeyboardButton("2️⃣3️⃣")
    button24 = types.KeyboardButton("2️⃣4️⃣")
    button25 = types.KeyboardButton("")
    button103 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button103u = types.KeyboardButton("1️⃣0️⃣3️⃣у")
    button104 = types.KeyboardButton("1️⃣0️⃣4️⃣")
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button122 = types.KeyboardButton("1️⃣2️⃣2️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button3).add(button4, button4a).add(button6, button10)
    keyboard.add(button13, button14).add(button15, button17).add(button19, button20)
    keyboard.add(button21, button22).add(button23, button24).add(button25, button103)
    keyboard.add(button103u, button104).add(button118, button119).add(button122, button_schedule)
    keyboard.add(button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTZGO0", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'золотой ключик (набережная)')
def zolotoy_klyuchik(message):
    mess = (f'Доехать до остановки "золотой ключик" можно на маршрутах: 3, 13, 20, 24. '
           f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button3 = types.KeyboardButton("3️⃣")
    button13 = types.KeyboardButton("1️⃣3️⃣")
    button20 = types.KeyboardButton("2️⃣0️⃣")
    button24 = types.KeyboardButton("2️⃣4️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button3, button13).add(button20, button24)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsT6XjJ", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'лицей 1')
def litsey_1(message):
    mess = (f'Доехать до остановки "лицей 1" можно на маршрутах: 3, 13, 20, 24. '
           f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button3 = types.KeyboardButton("3️⃣")
    button13 = types.KeyboardButton("1️⃣3️⃣")
    button20 = types.KeyboardButton("2️⃣0️⃣")
    button24 = types.KeyboardButton("2️⃣4️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button3, button13).add(button20, button24)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTb4nB", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'магазин геолог')
def magazin_geolog(message):
    mess = (f'Доехать до остановки "магазин геолог" можно на маршрутах: 3, 13, 20, 24. '
           f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button3 = types.KeyboardButton("3️⃣")
    button13 = types.KeyboardButton("1️⃣3️⃣")
    button20 = types.KeyboardButton("2️⃣0️⃣")
    button24 = types.KeyboardButton("2️⃣4️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button3, button13).add(button20, button24)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTfEJO", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'школа 15')
def shkola_15(message):
    mess = (f'Доехать до остановки "школа 15" можно на маршрутах: 3, 13, 20, 24. '
           f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button3 = types.KeyboardButton("3️⃣")
    button13 = types.KeyboardButton("1️⃣3️⃣")
    button20 = types.KeyboardButton("2️⃣0️⃣")
    button24 = types.KeyboardButton("2️⃣4️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button3, button13).add(button20, button24)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTnEzy", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'нефтебаза')
def neftebaza(message):
    mess = (f'Доехать до остановки "нефтебаза" можно на маршрутах: 3, 20. '
           f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button3 = types.KeyboardButton("3️⃣")
    button20 = types.KeyboardButton("2️⃣0️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button3, button20)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTnHKj", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'туб.санаторий')
def tub_sanatoriy(message):
    mess = (f'Доехать до остановки "туб.санаторий" можно на маршрутах: 3, 20. '
           f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button3 = types.KeyboardButton("3️⃣")
    button20 = types.KeyboardButton("2️⃣0️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button3, button20)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTrBiq", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'сосновый')
def sosnovyy(message):
    mess = (f'Доехать до остановки "сосновый" можно на маршрутах: 3, 20. '
           f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button3 = types.KeyboardButton("3️⃣")
    button20 = types.KeyboardButton("2️⃣0️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button3, button20)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTrKMn", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'семиполатинский лзу (красэко)')
def semipolatinskiy_lzu(message):
    mess = (f'Доехать до остановки "семиполатинский ЛЗУ" можно на маршруте: 13. '
           f'Чтобы посмотреть его расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button13 = types.KeyboardButton("1️⃣3️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button13)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTr2lt", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'ново - канский лпх')
def novo_kanskiy_lpkh(message):
    mess = (f'Доехать до остановки "Ново-Канский ЛПХ" можно на маршруте: 13. '
           f'Чтобы посмотреть его расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button13 = types.KeyboardButton("1️⃣3️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button13)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTvZ5r", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'стрижевой')
def strizhevoy(message):
    mess = (f'Доехать до остановки "стрижевой" можно на маршруте: 13. '
           f'Чтобы посмотреть его расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button13 = types.KeyboardButton("1️⃣3️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button13)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTv8yT", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'дрсу - 3')
def drsu_3(message):
    mess = (f'Доехать до остановки "ДРСУ-3" можно на маршруте: 13. '
           f'Чтобы посмотреть его расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button13 = types.KeyboardButton("1️⃣3️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button13)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTvXLy", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'подсобное')
def podsobnoe(message):
    mess = (f'Доехать до остановки "подсобное" можно на маршруте: 13. '
           f'Чтобы посмотреть его расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button13 = types.KeyboardButton("1️⃣3️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button13)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsTzQNq", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'агроснаб')
def agrosnab(message):
    mess = (f'Доехать до остановки "агроснаб" можно на маршруте: 24. '
           f'Чтобы посмотреть его расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button24 = types.KeyboardButton("2️⃣4️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button24)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspIJZr", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'соленое')
def solenoe(message):
    mess = (f'Доехать до остановки "соленое" можно на маршруте: 24. '
           f'Чтобы посмотреть его расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button24 = types.KeyboardButton("2️⃣4️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button24)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsteY1c", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'абанское кладбище')
def abanskoe_kladbische(message):
    mess = (f'Доехать до остановки "абанское кладбище" можно на маршруте: 19. '
           f'Чтобы посмотреть его расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button19 = types.KeyboardButton("1️⃣9️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button19)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsteVig", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'пед.колледж')
def ped_kolledzh(message):
    mess = (f'Доехать до остановки "Пед.колледж" можно на маршрутах: 15, 122. '
           f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button4 = types.KeyboardButton("")
    button6 = types.KeyboardButton("")
    button14 = types.KeyboardButton("")
    button15 = types.KeyboardButton("1️⃣5️⃣")
    button25 = types.KeyboardButton("")
    button122 = types.KeyboardButton("1️⃣2️⃣2️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button4, button6).add(button14, button15).add(button25, button122)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspQTPx", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'стариково')
def starikovo(message):
    mess = (f'Доехать до остановки "стариково" можно на маршрутах: 4, 25. '
           f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button4 = types.KeyboardButton("4️⃣")
    button25 = types.KeyboardButton("2️⃣5️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button4, button25)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspUCyH", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'черемушки')
def cheremushki(message):
    mess = (f'Доехать до остановки "черемушки" можно на маршрутах: 14, 25. '
           f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
           f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button14 = types.KeyboardButton("1️⃣4️⃣")
    button25 = types.KeyboardButton("2️⃣5️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button14, button25)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspYMN8", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'дсу - 4')
def dsu_4(message):
    mess = (f'Доехать до остановки "ДСУ-4" можно на маршрутах: 15, 122. '
            f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
            f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button6 = types.KeyboardButton("")
    button15 = types.KeyboardButton("1️⃣5️⃣")
    button122 = types.KeyboardButton("1️⃣2️⃣2️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button6, button15).add(button122)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsp4LJe", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'досааф')
def dosaaf(message):
    mess = (f'Доехать до остановки "ДОСААФ" можно на маршрутах: 15, 122. '
            f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
            f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button6 = types.KeyboardButton("")
    button15 = types.KeyboardButton("1️⃣5️⃣")
    button122 = types.KeyboardButton("1️⃣2️⃣2️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button6, button15).add(button122)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspiAIQ", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'злмк')
def zlmk(message):
    mess = (f'Доехать до остановки "ЗЛМК" можно на маршрутах: 15, 122. '
            f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
            f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button6 = types.KeyboardButton("")
    button15 = types.KeyboardButton("1️⃣5️⃣")
    button122 = types.KeyboardButton("1️⃣2️⃣2️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button6, button15).add(button122)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspiZjw", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'ккз')
def kkz(message):
    mess = (f'Доехать до остановки "ККЗ" можно на маршрутах: 15, 122. '
            f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
            f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button6 = types.KeyboardButton("")
    button15 = types.KeyboardButton("1️⃣5️⃣")
    button122 = types.KeyboardButton("1️⃣2️⃣2️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button6, button15).add(button122)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspiXoS", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'анцирь')
def ancir(message):
    mess = (f'Доехать до остановки "Анцирь" можно на маршруте: 122. '
            f'Чтобы посмотреть его расписание, нажмите кнопку с номером маршрута ниже. Чтобы посмотреть, где находится на карте '
            f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button122 = types.KeyboardButton("1️⃣2️⃣2️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button122)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspmL8R", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'чечеул')
def checheul(message):
    mess = (f'Доехать до остановки "Чечеул" можно на маршрутах: 105, 118. '
            f'Чтобы посмотреть их расписание, нажмите нужную кнопку в меню ниже. Чтобы посмотреть, где находится на карте '
            f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button105 = types.KeyboardButton("1️⃣0️⃣5️⃣")
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button105, button118)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspqOit", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'зеленый луг')
def zelenyj_lug(message):
    mess = (f'Доехать до остановки "Зеленый Луг" можно на маршруте: 118. '
            f'Чтобы посмотреть его расписание, нажмите кнопку с номером маршрута ниже. Чтобы посмотреть, где находится на карте '
            f'данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button118)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspuUPh", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'новый путь')
def novy_put(message):
    mess = (f'Доехать до остановки "Новый Путь" можно на маршруте: 118. '
            f'Чтобы посмотреть его расписание, нажмите кнопку с номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button118)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspyI90", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'строителей')
def stroiteley(message):
    mess = (f'Доехать до остановки "Строителей" можно на маршруте: 22. '
            f'Чтобы посмотреть его расписание, нажмите кнопку с номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button22 = types.KeyboardButton("2️⃣2️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button22)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspyOkX", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'школа 8')
def shkola_8(message):
    mess = (f'Доехать до остановки "Школа 8" можно на маршруте: 9. '
            f'Чтобы посмотреть его расписание, нажмите кнопку с номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button9 = types.KeyboardButton("9️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button9)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsp5CP6", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'краевая (гавань)')
def kraevaya(message):
    mess = (f'Доехать до остановки "Краевая" можно на маршруте: 9. '
            f'Чтобы посмотреть его расписание, нажмите кнопку с номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button9 = types.KeyboardButton("9️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button9)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspBAkO", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'бхз')
def bhz(message):
    mess = (f'Доехать до остановки "БХЗ" можно на маршрутах: 5, 9, 22, 118. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button5 = types.KeyboardButton("5️⃣")
    button9 = types.KeyboardButton("9️⃣")
    button22 = types.KeyboardButton("2️⃣2️⃣")
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button5, button9, button22, button118)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspVNmL", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'гор.больница')
def gor_bolnica(message):
    mess = (f'Доехать до остановки "Гор.больница" можно на маршруте: 17. '
            f'Чтобы посмотреть его расписание, нажмите кнопку с номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button17 = types.KeyboardButton("1️⃣7️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button17)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspV4mu", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'политехнический')
def politehnicheskiy(message):
    mess = (f'Доехать до остановки "Политехнический" можно на маршрутах: 5, 8, 9, 17, 21, 22, 104, 105, 118. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button4 = types.KeyboardButton("")
    button4a = types.KeyboardButton("")
    button5 = types.KeyboardButton("5️⃣")
    button8 = types.KeyboardButton("8️⃣")
    button9 = types.KeyboardButton("9️⃣")
    button17 = types.KeyboardButton("1️⃣7️⃣")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button22 = types.KeyboardButton("2️⃣2️⃣")
    button104 = types.KeyboardButton("1️⃣0️⃣4️⃣")
    button105 = types.KeyboardButton("1️⃣0️⃣5️⃣")
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button4, button4a, button5, button8, button9, button17, button21, button22, button104, button105, button118)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspVIKi", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'гибдд')
def gibdd(message):
    mess = (f'Доехать до остановки "ГИБДД" можно на маршрутах: 21, 105. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button4 = types.KeyboardButton("")
    button4a = types.KeyboardButton("")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button105 = types.KeyboardButton("1️⃣0️⃣5️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button4, button4a, button21, button105)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspR-n2", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'автоколона 1261')
def avtokolona_1261(message):
    mess = (f'Доехать до остановки "Автоколона 1261" можно на маршруте: 8. '
            f'Чтобы посмотреть его расписание, нажмите кнопку с номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button8 = types.KeyboardButton("8️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button8)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspZ0mb", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == '5 городок')
def pyatyy_gorodok(message):
    mess = (f'Доехать до остановки "5 городок" можно на маршруте: 8. '
            f'Чтобы посмотреть его расписание, нажмите кнопку с номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button8 = types.KeyboardButton("8️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button8)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsp68jm", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == '4 городок')
def chetvertyy_gorodok(message):
    mess = (f'Доехать до остановки "4 городок" можно на маршрутах: 105. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button4 = types.KeyboardButton("")
    button4a = types.KeyboardButton("")
    button105 = types.KeyboardButton("1️⃣0️⃣5️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button4, button4a, button105)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspbYo2", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'патп')
def patp(message):
    mess = (f'Доехать до остановки "ПАТП" можно на маршрутах: 8, 21. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button8 = types.KeyboardButton("8️⃣")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button8, button21)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspbT6W", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'мелькомбинат')
def melkombinat(message):
    mess = (f'Доехать до остановки "Мелькомбинат" можно на маршрутах: 8, 21. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button8 = types.KeyboardButton("8️⃣")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button8, button21)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspfYNt", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'эйдемана')
def eydemana(message):
    mess = (f'Доехать до остановки "Эйдемана" можно на маршрутах: 5, 8, 9, 17, 21, 22, 104, 105, 118. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button4 = types.KeyboardButton("")
    button4a = types.KeyboardButton("")
    button5 = types.KeyboardButton("5️⃣")
    button8 = types.KeyboardButton("8️⃣")
    button9 = types.KeyboardButton("9️⃣")
    button17 = types.KeyboardButton("1️⃣7️⃣")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button22 = types.KeyboardButton("2️⃣2️⃣")
    button104 = types.KeyboardButton("1️⃣0️⃣4️⃣")
    button105 = types.KeyboardButton("1️⃣0️⃣5️⃣")
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button4, button4a, button5, button8, button9, button17, button21, button22, button104, button105, button118)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspfWJ8", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'гор.сад')
def gor_sad(message):
    mess = (f'Доехать до остановки "Гор.сад" можно на маршрутах: 3а, 5, 8, 9, 10, 17, 21, 22, 104, 105, 118, 119. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button3a = types.KeyboardButton("3️⃣а")
    button4 = types.KeyboardButton("")
    button4a = types.KeyboardButton("")
    button5 = types.KeyboardButton("5️⃣")
    button8 = types.KeyboardButton("8️⃣")
    button9 = types.KeyboardButton("9️⃣")
    button10 = types.KeyboardButton("1️⃣0️⃣")
    button17 = types.KeyboardButton("1️⃣7️⃣")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button22 = types.KeyboardButton("2️⃣2️⃣")
    button104 = types.KeyboardButton("1️⃣0️⃣4️⃣")
    button105 = types.KeyboardButton("1️⃣0️⃣5️⃣")
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button3a, button4, button4a, button5, button8, button9, button10, button17, button21, button22, button104, button105, button118, button119)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspjNKL", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'площадь коростелева')
def ploshchad_korosteleva(message):
    mess = (f'Доехать до остановки "Площадь Коростелева" можно на маршрутах: 1, 3, 3а, 5, 8, 9, 10, 13,  '
            f'15, 17, 19, 21, 22, 23, 24, 103, 103у, 105, 118, 119, 122. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("1️⃣")
    button3 = types.KeyboardButton("3️⃣")
    button3a = types.KeyboardButton("3️⃣а")
    button4 = types.KeyboardButton("")
    button5 = types.KeyboardButton("5️⃣")
    button4a = types.KeyboardButton("")
    button6 = types.KeyboardButton("")
    button8 = types.KeyboardButton("8️⃣")
    button9 = types.KeyboardButton("9️⃣")
    button10 = types.KeyboardButton("1️⃣0️⃣")
    button13 = types.KeyboardButton("1️⃣3️⃣")
    button14 = types.KeyboardButton("")
    button15 = types.KeyboardButton("1️⃣5️⃣")
    button17 = types.KeyboardButton("1️⃣7️⃣")
    button19 = types.KeyboardButton("1️⃣9️⃣")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button22 = types.KeyboardButton("2️⃣2️⃣")
    button23 = types.KeyboardButton("2️⃣3️⃣")
    button24 = types.KeyboardButton("2️⃣4️⃣")
    button25 = types.KeyboardButton("")
    button103 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button103u = types.KeyboardButton("1️⃣0️⃣3️⃣у")
    button105 = types.KeyboardButton("1️⃣0️⃣5️⃣")
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button122 = types.KeyboardButton("1️⃣2️⃣2️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button1, button3, button3a, button4,  button5,  button4a, button6, button8, button9, button10, button13, button14, button15, button17, button19, button21, button22, button23, button24, button25, button103, button103u, button105, button118, button119, button122)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspn2jd", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'ж/д вокзал (автовокзал)')
def zh_d_vokzal(message):
    mess = (f'Доехать до остановки "Ж/д вокзал" можно на маршрутах: 3, 3а, 5, 8, 9, 10, 13,  '
            f'15, 19, 21, 22, 24, 103, 103у, 104, 105, 118, 119, 122. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button3 = types.KeyboardButton("3️⃣")
    button3a = types.KeyboardButton("3️⃣а")
    button4 = types.KeyboardButton("")
    button4a = types.KeyboardButton("")
    button5 = types.KeyboardButton("5️⃣")
    button6 = types.KeyboardButton("")
    button8 = types.KeyboardButton("8️⃣")
    button9 = types.KeyboardButton("9️⃣")
    button10 = types.KeyboardButton("1️⃣0️⃣")
    button13 = types.KeyboardButton("1️⃣3️⃣")
    button14 = types.KeyboardButton("")
    button15 = types.KeyboardButton("1️⃣5️⃣")
    button19 = types.KeyboardButton("1️⃣9️⃣")
    button21 = types.KeyboardButton("2️⃣1️⃣")
    button22 = types.KeyboardButton("2️⃣2️⃣")
    button24 = types.KeyboardButton("2️⃣4️⃣")
    button25 = types.KeyboardButton("")
    button103 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button103u = types.KeyboardButton("1️⃣0️⃣3️⃣у")
    button104 = types.KeyboardButton("1️⃣0️⃣4️⃣")
    button105 = types.KeyboardButton("1️⃣0️⃣5️⃣")
    button118 = types.KeyboardButton("1️⃣1️⃣8️⃣")
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button122 = types.KeyboardButton("1️⃣2️⃣2️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button3, button3a, button4, button4a)
    keyboard.row(button5, button6, button8, button9)
    keyboard.row(button10, button13, button14, button15)
    keyboard.row(button19, button21, button22, button24)
    keyboard.row(button25, button103, button103u, button104)
    keyboard.row(button105, button118, button119, button122)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDspzL~M", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'кинотеатр космос')
def kinoteatr_kosmos(message):
    mess = (f'Доехать до остановки "Кинотеатр Космос" можно на маршрутах: 1, 5, 10, 23, 103, 103у, 119. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("1️⃣")
    button5 = types.KeyboardButton("5️⃣")
    button10 = types.KeyboardButton("1️⃣0️⃣")
    button14 = types.KeyboardButton("")
    button23 = types.KeyboardButton("2️⃣3️⃣")
    button103 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button103u = types.KeyboardButton("1️⃣0️⃣3️⃣у")
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.row(button1, button5, button10)
    keyboard.row(button23, button103, button103u, button119 )
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDsp7SZO", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'кинотеатр север')
def kinoteatr_sever(message):
    mess = (f'Доехать до остановки "Кинотеатр Север" можно на маршрутах: 1, 23. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("1️⃣")
    button23 = types.KeyboardButton("2️⃣3️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button1, button23)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDstAM2e", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'детская больница (север)')
def detskaya_bolnica(message):
    mess = (f'Доехать до остановки "Детская больница" можно на маршрутах: 10, 103, 103у, 119. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button10 = types.KeyboardButton("1️⃣0️⃣")
    button103 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button103u = types.KeyboardButton("1️⃣0️⃣3️⃣у")
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button10, button103, button103u, button119)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDstAS-~", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'сизо')
def sizo(message):
    mess = (f'Доехать до остановки "СИЗО" можно на маршрутах: 5, 23. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button5 = types.KeyboardButton("5️⃣")
    button23 = types.KeyboardButton("2️⃣3️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button5, button23)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDstEUPb", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'мясокомбинат')
def myasokombinat(message):
    mess = (f'Доехать до остановки "Мясокомбинат" можно на маршрутах: 5, 23. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button5 = types.KeyboardButton("5️⃣")
    button23 = types.KeyboardButton("2️⃣3️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button5, button23)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDstEG-Q", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'коллекторная ул.')
def kollektornaya_ul(message):
    mess = (f'Доехать до остановки "Коллекторная ул." можно на маршрутах: 1, 10, 119. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button1 = types.KeyboardButton("1️⃣")
    button10 = types.KeyboardButton("1️⃣0️⃣")
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button1, button10, button119)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDstIYyL", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'кан')
def kan(message):
    mess = (f'Доехать до остановки "Кан" можно на маршрутах: 5, 23. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button5 = types.KeyboardButton("5️⃣")
    button23 = types.KeyboardButton("2️⃣3️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button5, button23)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDstID35", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'рассвет')
def rassvet(message):
    mess = (f'Доехать до остановки "Рассвет" можно на маршрутах: 10, 119. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button10 = types.KeyboardButton("1️⃣0️⃣")
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button10, button119)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDstMY0r", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'бережки')
def berezhki(message):
    mess = (f'Доехать до остановки "Бережки" можно на маршруте: 119. '
            f'Чтобы посмотреть его расписание, нажмите кнопку с номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button119)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDstM621", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'левобережное')
def levoberezhnoe(message):
    mess = (f'Доехать до остановки "Левобережное" можно на маршруте: 119. '
            f'Чтобы посмотреть его расписание, нажмите кнопку с номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button119 = types.KeyboardButton("1️⃣1️⃣9️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button119)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDstMXjv", reply_markup=keyboard)


@bot.message_handler(func=lambda message: message.text.lower() == 'бражное')
def brazhnoe(message):
    mess = (f'Доехать до остановки "Бражное" можно на маршруте: 104. '
            f'Чтобы посмотреть его расписание, нажмите кнопку с номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button104 = types.KeyboardButton("1️⃣0️⃣4️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button104)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDstQNJB", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'филимоново')
def filimonovo(message):
    mess = (f'Доехать до остановки "Филимоново" можно на маршрутах: 103, 103у. '
            f'Чтобы посмотреть их расписание, нажмите кнопку с нужным номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button103 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button103u = types.KeyboardButton("1️⃣0️⃣3️⃣у")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button103, button103u)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDstUENB", reply_markup=keyboard)

@bot.message_handler(func=lambda message: message.text.lower() == 'сухая речка')
def suhaya_rechka(message):
    mess = (f'Доехать до остановки "Сухая речка" можно на маршруте: 103. '
            f'Чтобы посмотреть его расписание, нажмите кнопку с номером маршрута ниже. '
            f'Чтобы посмотреть, где находится на карте данная остановка, нажмите на геометку:')
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, selective=True)
    button103 = types.KeyboardButton("1️⃣0️⃣3️⃣")
    button_schedule = types.KeyboardButton("Как доехать до остановки ❓")
    button_menu = types.KeyboardButton("🚍 Меню 🚍")
    keyboard.add(button103)
    keyboard.add(button_schedule, button_menu)
    bot.reply_to(message, mess + "\nhttps://yandex.ru/maps/-/CDstUH0L", reply_markup=keyboard)


@bot.message_handler(content_types=["text"])
def send_message(message):
    tz = pytz.timezone('Etc/GMT-7')

    date_now = datetime.now(tz)
    now = date_now.strftime("%H:%M")
    time = datetime.strptime(now, "%H:%M")

    time1с = [datetime.strptime(temp, "%H:%M") for temp in солка1]

    ind = bisect.bisect_right(time1с, time)
    if ind < len(солка1):
        солнечный1 = f"Ближайший 1 в {солка1[ind]}"
    else:
        солнечный1 = "нет ближайшего времени"

    time1к = [datetime.strptime(temp, "%H:%M") for temp in колектор1]

    ind = bisect.bisect_right(time1к, time)
    if ind < len(колектор1):
        коллекторная1 = f"Ближайший 1 в {колектор1[ind]}"
    else:
        коллекторная1 = "нет ближайшего времени"


    if message.text.lower() == ('солнечный 1'):
        bot.reply_to(message, солнечный1)
    if message.text.lower() == ('коллекторная'):
        bot.reply_to(message, коллекторная1)



    date_now = datetime.now(tz)
    now = date_now.strftime("%H:%M")
    time = datetime.strptime(now, "%H:%M")

    time9в = [datetime.strptime(temp, "%H:%M") for temp in вок9]

    ind = bisect.bisect_right(time9в, time)
    if ind < len(вок9):
        вокзал9 = f"Ближайший 9 в {вок9[ind]}"
    else:
        вокзал9 = "нет ближайшего времени"

    date_now = datetime.now(tz)
    now = date_now.strftime("%H:%M")
    time = datetime.strptime(now, "%H:%M")

    time9к = [datetime.strptime(temp, "%H:%M") for temp in корост9]

    ind = bisect.bisect_right(time9к, time)
    if ind < len(корост9):
        коростелева9 = f"Ближайший 9 в {корост9[ind]} - направление вокзал - ул. Краевая"
    else:
        коростелева9 = "нет ближайшего времени"

    date_now = datetime.now(tz)
    now = date_now.strftime("%H:%M")
    time = datetime.strptime(now, "%H:%M")

    time9п = [datetime.strptime(temp, "%H:%M") for temp in полит9]

    ind = bisect.bisect_right(time9п, time)
    if ind < len(полит9):
        политех9 = f"Ближайший 9 в {полит9[ind]} - направление вокзал - ул. Краевая"
    else:
        политех9 = "нет ближайшего времени"

    date_now = datetime.now(tz)
    now = date_now.strftime("%H:%M")
    time = datetime.strptime(now, "%H:%M")

    time9кра = [datetime.strptime(temp, "%H:%M") for temp in краев9]

    ind = bisect.bisect_right(time9кра, time)
    if ind < len(краев9):
        краевая9 = f"Ближайший 9 в {краев9[ind]}"
    else:
        краевая9 = "нет ближайшего времени"

    date_now = datetime.now(tz)
    now = date_now.strftime("%H:%M")
    time = datetime.strptime(now, "%H:%M")

    time9_1п = [datetime.strptime(temp, "%H:%M") for temp in полит_9]

    ind = bisect.bisect_right(time9_1п, time)
    if ind < len(полит_9):
        политех9_1 = f"Ближайший 9 в {полит_9[ind]} - направление ул. Краевая - вокзал"
    else:
        политех9_1 = "нет ближайшего времени"

    date_now = datetime.now(tz)
    now = date_now.strftime("%H:%M")
    time = datetime.strptime(now, "%H:%M")

    time9_1к = [datetime.strptime(temp, "%H:%M") for temp in корост_9]

    ind = bisect.bisect_right(time9_1к, time)
    if ind < len(корост_9):
        коростелева9_1 = f"Ближайший 9 в {корост_9[ind]} - направление ул. Краевая - вокзал"
    else:
        коростелева9_1 = "нет ближайшего времени"



    if message.text.lower() == ('вокзал 9'):
        bot.reply_to(message, вокзал9)
    if message.text.lower() == ('площадь коростелева 9'):
        bot.reply_to(message, коростелева9)
    if message.text.lower() == ('площадь коростелева 9'):
        bot.reply_to(message, коростелева9_1)
    if message.text.lower() == ('политехнический 9'):
        bot.reply_to(message, политех9)
    if message.text.lower() == ('политехнический 9'):
        bot.reply_to(message, политех9_1)
    if message.text.lower() == ('ул. краевая'):
        bot.reply_to(message, краевая9)



    date_now = datetime.now(tz)
    now = date_now.strftime("%H:%M")
    time = datetime.strptime(now, "%H:%M")

    time22с = [datetime.strptime(temp, "%H:%M") for temp in солка22]

    ind = bisect.bisect_right(time22с, time)
    if ind < len(солка22):
         солнечный22 = f"Ближайший 22 в {солка22[ind]}"
    else:
         солнечный22 = "нет ближайшего времени"


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



    if message.text.lower() == ('ближайший 22'):
        mess = (f'Выберите остановку и напишите ее так же как написано тут: солнечный 22, предмостная 22, вокзал 22,'
                f' политехнический, строителей')
        bot.reply_to(message, mess, parse_mode='html')
    if message.text.lower() == ('солнечный 22'):
        bot.reply_to(message, солнечный22)
    if message.text.lower() == ('предмостная 22'):
        bot.reply_to(message, канпер22)
    if message.text.lower() == ('предмостная 22'):
        bot.reply_to(message, канпер22_1)
    if message.text.lower() == ('вокзал 22'):
        bot.reply_to(message, вокзал22)
    if message.text.lower() == ('вокзал 22'):
        bot.reply_to(message, вокзал22_1)
    if message.text.lower() == ('политехнический 22'):
        bot.reply_to(message, политех22)
    if message.text.lower() == ('политехнический 22'):
        bot.reply_to(message, политех22_1)
    if message.text.lower() == ('строителей 22'):
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
    if message.text.lower() == ('сосновый 20'):
        bot.reply_to(message, сосновый20_1)
    if message.text.lower() == ('предмостная 20'):
        bot.reply_to(message, канпер20_1)


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
    if message.text.lower() == ('мелькомбинат 21'):
        bot.reply_to(message, мелькомбинат21)
    if message.text.lower() == ('мелькомбинат 21'):
        bot.reply_to(message, мелькомбинат21вых)


    if message.text.lower() == ('дачные'):
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('4.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('4.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text.lower() == ('дачные'):
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('4а.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('4а.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text.lower() == ('дачные'):
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('5.1дачные.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('5.2дачные.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text.lower() == ('дачные'):
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('6.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('6.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text.lower() == ('дачные'):
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('10.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('10.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text.lower() == ('дачные'):
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('14.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('14.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text.lower() == ('дачные'):
        bot.send_photo(message.chat.id, open('23.jpg', 'rb'), reply_to_message_id=message.message_id)

    if message.text.lower() == ('дачные'):
        bot.send_photo(message.chat.id, open('25.jpg', 'rb'), reply_to_message_id=message.message_id)


    if message.text == "1️⃣":
        bot.send_photo(message.chat.id, open('1.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "3️⃣":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('3.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('3.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)

    if message.text == "3️⃣а":
        text = f"Смотреть пометку ВЭС"
        bot.send_photo(message.chat.id, open('3.2.jpg', 'rb'), caption=text, parse_mode="HTML", reply_to_message_id=message.message_id)

    if message.text == "":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('4.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('4.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text.lower() == "":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('4а.1.jpg', 'rb')),
                                              telebot.types.InputMediaPhoto(open('4а.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "5️⃣":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('5.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('5.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('6.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('6.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)

    if message.text == "8️⃣":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('8.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('8.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "9️⃣":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('9.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('9.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "1️⃣0️⃣":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('10.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('10.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)

    if message.text == "1️⃣3️⃣":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('13.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('13.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('13.3.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('14.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('14.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "1️⃣️️5️⃣":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('15.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('15.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('15.3.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('15.4.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "1️⃣7️⃣":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('17.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('17.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('17.3.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('17.4.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('17.5.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('17.6.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('17.7.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('17.8.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "1️⃣9️⃣":
        bot.send_photo(message.chat.id, open('19.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "2️⃣0️⃣":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('20.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('20.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('20.3.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('20.4.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('20.5.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)

    if message.text == "2️⃣1️⃣":
        bot.send_photo(message.chat.id, open('21.1.jpg', 'rb'),reply_to_message_id=message.message_id)
    if message.text == "2️⃣1️⃣":
        text = f"Графики выходного дня"
        bot.send_photo(message.chat.id, open('21.2.jpg', 'rb'), caption=text, parse_mode="HTML", reply_to_message_id=message.message_id)

    if message.text == "2️⃣2️⃣":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('22.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('22.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('22.3.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('22.4.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "2️⃣3️⃣":
        bot.send_photo(message.chat.id, open('23.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "2️⃣4️⃣":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('24.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('24.2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text == "":
        bot.send_photo(message.chat.id, open('25.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "1️⃣0️⃣3️⃣":
        bot.send_photo(message.chat.id, open('103.1.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "1️⃣0️⃣3️⃣у":
        bot.send_photo(message.chat.id, open('103.2.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "1️⃣0️⃣4️⃣":
        bot.send_photo(message.chat.id, open('104.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "1️⃣0️⃣️5️⃣":
        bot.send_photo(message.chat.id, open('105.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "1️⃣1️⃣8️⃣":
        bot.send_photo(message.chat.id, open('118.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "1️⃣1️⃣9️⃣":
        bot.send_photo(message.chat.id, open('119.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text == "1️⃣2️⃣2️⃣":
        bot.send_photo(message.chat.id, open('122.jpg', 'rb'), reply_to_message_id=message.message_id)
    if message.text.lower() == "🟢пригородные":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('141.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('141.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('141.3.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('141.4.jpg', 'rb'),
                                                                                  caption='Маршрут Канск- Иланский')],
                                               reply_to_message_id=message.message_id)
    if message.text.lower() == "🟢пригородные":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('пригород1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('пригород2.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text.lower() == "🟢междугородные":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('межгород1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('межгород2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('межгород3.jpg', 'rb'))],
                                               reply_to_message_id=message.message_id)
    if message.text.lower() == "🟢иланск":
        bot.send_media_group(message.chat.id, [telebot.types.InputMediaPhoto(open('иланск1.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('иланск1.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('иланск1.3.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('иланск2.1.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('иланск2.2.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('иланск3.jpg', 'rb')),
                                               telebot.types.InputMediaPhoto(open('иланск129.jpg', 'rb'),
                                                                                  caption='Маршруты по городу')],
                                               reply_to_message_id=message.message_id)

    if message.text.lower() == "🟢иланск":
        text = f"Маршруты Иланск - Красноярск"
        bot.send_photo(message.chat.id, open('иланск красноярск.jpg', 'rb'), caption=text, parse_mode="HTML",
                                                                             reply_to_message_id=message.message_id)

    if message.text.lower() == "🟢красноярск-восток":
        bot.send_photo(message.chat.id, open('красноярск-восток.png', 'rb'), reply_to_message_id=message.message_id)




bot.polling(none_stop=True)