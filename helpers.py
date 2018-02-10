# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 15:52:40 2018

@author: VedMedk0
"""
import telebot
import config
bot1 = telebot.TeleBot(config.token)
#команда старт
@bot1.message_handler(commands=['start'])
def handle_start(message):
    bot1.send_message(message.chat.id, config.START_MSG)
         
         
@bot1.message_handler(commands=['help'])
def handle_help(message):
    bot1.send_message(message.chat.id, config.HELP_MSG)


