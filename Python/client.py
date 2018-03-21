# Клиент

from socket import *
import datetime
import json


def create_request_presence(timestamp=None):
    """
    Сообщение о присутствии пользователя
    >>> create_request_presence("2018-03-16 19:03:54.438645")
    '{"action": "presence", "time": "2018-03-16 19:03:54.438645"}'
    >>>
    :param timestamp: Метка времени
    :return:
    """
    if not timestamp:
        timestamp = str(datetime.datetime.now())
    result = {
        "action": "presence",
        "time": timestamp
    }
    return json.dumps(result)


if __name__=="__main__":
	s = socket()
	s.connect(('localhost', 8888))
	request_presence = create_request_presence()
	s.send(request_presence.encode("utf-8"))
	server_response = s.recv(1024)
	print(server_response.decode("utf-8"))
	s.close()
	import doctest
	doctest.testmod()