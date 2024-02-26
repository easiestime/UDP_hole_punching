
import socket
class router:
    def __init__(self, socket_instance):
        self._socket = socket_instance
    def commonResponse(self, client_address):
        response = "已收到数据"
        self._socket.sendto(response.encode('utf-8'), client_address)