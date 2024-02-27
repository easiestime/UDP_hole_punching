import json
import socket
import common.constants as constants
from common.CommandPayload import CommandPayload, from_str
import time
import threading
import uuid

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_address = ("0.0.0.0", 31999)

server_address = ("0.0.0.0", 31888)
uuid_index = 0
device_uuid = uuid.uuid4()

connection_info = {}
lock = threading.Lock()


def keep_alive():
    while True:
        command = CommandPayload(constants.keep_alive_client_message, ++uuid_index)
        client_socket.sendto(command.toResponse().encode("utf-8"), server_address)
        data, _ = client_socket.recvfrom(1024)
        response_payload = from_str(data.decode("utf-8"))
        content = eval(response_payload.payload)
        lock.acquire()
        connection_info = content
        lock.release()
        time.sleep(5)

client_socket.bind(client_address)

keep_alive_thread = threading.Thread(target=keep_alive, name='keep-alive-thread')
keep_alive_thread.start()




keep_alive_thread.join()
