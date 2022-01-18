import sys

print(sys.path)
from variables import *
print(dir())
import json
from socket import *


def get_message(client):
    encoded_response = client.recv(MAX_PACKAGE_LENGHT)
    if isinstance(encoded_response, bytes):
        json_response = encoded_response.decode(ENCODING)
        response = json.loads(json_response)
        if isinstance(response, dict):
            return response
        raise ValueError
    raise ValueError


def send_message(sock, message):
    js_message = json.dumps(message)
    encoded_message = js_message.encode(ENCODING)
    sock.send(encoded_message)
