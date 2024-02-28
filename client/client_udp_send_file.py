import json
import socket
import common.constants as constants
from common.CommandPayload import CommandPayload, from_str
import time
import threading
import uuid

client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_address = ("0.0.0.0", 31991)

server_address = ("0.0.0.0", 31888)
uuid_index = 1
device_uuid = uuid.uuid4()

connection_info = {}
lock = threading.Lock()


def keep_alive():
    while True:
        command = CommandPayload(constants.keep_alive_client_message, str(++uuid_index))
        client_socket.sendto(command.toResponse().encode("utf-8"), server_address)
        receive_data, _ = client_socket.recvfrom(1024)
        response_payload = from_str(receive_data.decode("utf-8"))
        content = eval(response_payload.payload)
        lock.acquire()
        connection_info["data"] = content
        lock.release()
        time.sleep(5)

client_socket.bind(client_address)

keep_alive_thread = threading.Thread(target=keep_alive, name='keep-alive-thread')
keep_alive_thread.start()

while True:
    data, client_address = client_socket.recvfrom(1024)
    # 打印接收到的数据和客户端地址
    print(f"接收到来自 {client_address} 的数据: {data.decode('utf-8')}")
    # # 可选：向客户端发送响应数据
    # response = "已收到数据"
    # server_socket.sendto(response.encode('utf-8'), client_address)
