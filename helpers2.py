# -*- coding: utf-8 -*-
"""
Created on Sat Feb 10 22:10:49 2018

@author: VedMedk0
"""
import helpers
bot=helpers.bot1

@bot.message_handler(commands=['myid'])
def handle_myid(message):
    bot.send_message(message.chat.id, str(message.from_user.id))
         
@bot.message_handler(commands=['talktoved'])
def talktoved(message):
    bot.send_message(config.ID_vedmedk0, 'hello ved')