# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 22:25:18 2017

@author: VedMedk0
"""

import config
import sqlighter
import helpers
bot = helpers.Frbot(config.token)
DB=sqlighter.SQLighter(config.database_name)

if __name__ == '__main__':
     bot.polling(none_stop=True)