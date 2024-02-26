import socket
import common.constants as constants
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_address = ("0.0.0.0", 31999)
server_address = ("0.0.0.0", 31888)

client_socket.bind(client_address)

client_socket.sendto(constants.keep_alive_client_message.encode("utf-8"), server_address)
data, client_address = client_socket.recvfrom(1024)
print(data.decode("utf-8"))
