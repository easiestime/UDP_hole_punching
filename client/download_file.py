import socket
from common.CommandPayload import CommandPayload
import common.constants as constants

server_address = ('127.0.0.1', 31999)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# 发送数据到服务器
command = CommandPayload(constants.download_file_message, "test.text")
client_socket.sendto(command.toResponse().encode(), server_address)
# 接收服务器的响应数据
data, server_address = client_socket.recvfrom(1024*1024*1024*8)
print(str(len(data)))
# print(f"从服务器收到的响应: {data.decode()}")
with open("test_download.text", "wb") as f:
    f.write(data)
# 关闭套接字
client_socket.close()
