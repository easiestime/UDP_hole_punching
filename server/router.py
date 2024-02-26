
import socket
import common.constants as constants
from command_handlers.base_handler import keep_alive_handler
class router:
    def __init__(self, socket_instance):
        self._socket = socket_instance

    def commonResponse(self, data: str, client_address):
        command = data.splitlines()[0]
        if command == constants.keep_alive_client_message:
            handler = keep_alive_handler(self._socket, None, client_address)
            handler.handle()
            # self._socket.sendto(constants.keep_alive_server_message.encode('utf-8'), client_address)
