import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_address = ("0.0.0.0", 31999)
server_address = ("127.0.0.1", 31888)

client_socket.bind(client_address)

client_socket.sendto("hello world".encode("utf-8"), server_address)
