#Реализовать декоратор @log, фиксирующий обращение к декорируемой функции: выводит в лог имя функции и её #аргументы
#Реализовать настройку логера в отдельном модуле log_config.py

import logging
import sys
import datetime

# Определить формат сообщений
#format = logging.Formatter('%(levelname)-10s %(asctime)s %(message)s')
format = logging.Formatter('%(
# Создать обработчик, который выводит сообщения с
# уровнем CRITICAL в поток stderr
crit_hand = logging.StreamHandler(sys.stderr)
crit_hand.setLevel(logging.CRITICAL)
crit_hand.setFormatter(format)
# Создать обработчик, который выводит сообщения в файл
applog_hand = logging.FileHandler('app.log')
applog_hand.setFormatter(format)
