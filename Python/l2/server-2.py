# Сервер

from socket import socket, AF_INET, SOCK_STREAM
import json
import time
import select
#import log_config


def response_200(message):
    """
    Ответ с кодом 200
    >>> response_200("Hello!")
    '{"response": 200, "alert": "Hello!"}'
    >>>
    :param message: необязательное сообщение
    :return:
    """
    result = {
        "response": 200,
        "alert": message
    }
    return json.dumps(result)

def new_listen_socket(address):
	sock = socket(AF_INET, SOCK_STREAM)
	sock.bind(address)
	sock.listen(5)
	sock.settimeout(0.2) # Таймаут для операций с сокетом
	# Таймаут необходим, чтобы не ждать появления данных в сокете
	return sock
	
def mainloop():
	''' Основной цикл обработки запросов клиентов
	'''
	address = ('', 8888)
	clients = []
	sock = new_listen_socket(address)
	
	while True:
		try:
			conn, addr = sock.accept() # Проверка подключений
		except OSError as e:
			pass # timeout вышел
		else:
			print("Получен запрос на соединение с %s" % str(addr))
			clients.append(conn)
		finally:
			# Проверить наличие событий ввода-вывода без таймаута
			w = []
			try:
				r, w, e = select.select([], clients, [], 0)
			except Exception as e:
				# Исключение произойдёт, если какой-то клиент отключится
				pass # Ничего не делать, если какой-то клиент отключился

			# Обойти список клиентов, читающих из сокета
			for s_client in w:
				timestr = time.ctime(time.time()) + "\n"
				try:
					s_client.send(timestr.encode('ascii'))
				except:
					# Удаляем клиента, который отключился
					clients.remove(s_client)
print('Сервер запущен!')

mainloop()

