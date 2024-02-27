import socket
import json
from common.CommandPayload import CommandPayload
import common.constants as constants
from server.connect_maintain import Connect_Maintain


class base_handler:
    def __init__(self, _socket: socket, _payload: str, _address: tuple):
        self.m_socket = _socket
        self.m_payload = _payload
        self.m_address = _address

    def handle(self):
        pass


connections = Connect_Maintain()


class keep_alive_handler(base_handler):
    def handle(self):
        connections.keep_alive(self.m_address, self.m_payload)
        response_payload = json.dumps(connections.connections)
        command_payload = CommandPayload(constants.keep_alive_server_message, response_payload)
        self.m_socket.sendto(command_payload.toResponse().encode("utf-8"), self.m_address)
