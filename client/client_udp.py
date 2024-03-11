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


def common_handler():
    while True:
        data, request_address = client_socket.recvfrom(1024)
        payload_str = data.decode("utf-8")
        response_payload = from_str(payload_str)
        print(response_payload)
        if response_payload is not None and response_payload.command == constants.keep_alive_server_message:
            content = eval(response_payload.payload)
            with open("connections.json", "w") as f:
                json.dump(content, f)
        elif response_payload is not None and response_payload.command == constants.download_file_message:
            file_name = response_payload.payload
            with open(file_name, "rb") as download_file:
                total_send_data = b""
                data = download_file.read(1024*1024*100)
                while data:
                    total_send_data += data
                    data = download_file.read(1024*1024*100)
                print(str(len(total_send_data)))
                client_socket.sendto(total_send_data, request_address)
        else:
            print(f"Error - unhandled message {payload_str}")


def keep_alive():
    while True:
        command = CommandPayload(constants.keep_alive_client_message, ++uuid_index)
        client_socket.sendto(command.toResponse().encode("utf-8"), server_address)
        time.sleep(5)


client_socket.bind(client_address)
keep_alive_thread = threading.Thread(target=keep_alive, name='keep-alive-thread')
common_IO_thread = threading.Thread(target=common_handler, name='common_IO_thread')
common_IO_thread.start()
keep_alive_thread.start()
keep_alive_thread.join()
common_IO_thread.join()
