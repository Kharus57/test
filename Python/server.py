# Сервер

from socket import *
import json


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


if __name__=="__main__":
    s = socket()
    s.bind(('', 8888))
    s.listen(5)

    while True:
        client, addr = s.accept()
        print("Получен запрос на соединение от %s" % str(addr))
        client_request = client.recv(1024)
        print("Получено сообщение: " + client_request.decode("utf-8"))
        request = json.loads(client_request.decode("utf-8"))
        if "action" in request:
            if request["action"] == "presence":
                response = response_200("Nice to meet")
                client.send(response.encode("utf-8"))
        client.close()