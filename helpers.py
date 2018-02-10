# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 15:52:40 2018

@author: VedMedk0
"""
import telebot
import config
from telebot import types


class Frbot(telebot.TeleBot):
    def __init__(self, token):
        telebot.TeleBot.__init__(self,token)

    #команда старт
    @Frbot.message_handler(commands=['start'])
    def handle_start(self, message):
         self.send_message(message.chat.id, config.START_MSG)
         
         
    @self.message_handler(commands=['help'])
    def handle_help(self,message):
         self.send_message(message.chat.id, config.HELP_MSG)
         
    #получить свой айди
    @self.message_handler(commands=['myid'])
    def handle_myid(self,message):
         self.send_message(message.chat.id, str(message.from_user.id))
         
    @self.message_handler(commands=['talktoved'])
    def talktoved(self,message):
         self.send_message(config.ID_vedmedk0, 'hello ved')

