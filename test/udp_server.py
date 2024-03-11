#
# import socket
#
#
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
# client_address = ("0.0.0.0", 31999)
#
# client_socket.bind(client_address)
#
# while True:
#     data, request_address = client_socket.recvfrom(1024)

import zlib, os, math

udp_buffer_size = 1024*50
file_big_buffer = 1024*1024*1024

with open("OpenRPA.msi", 'rb') as file:
    data = b""
    data_cursor = file.read(file_big_buffer)
    file_size = os.path.getsize("OpenRPA.msi")
    while data_cursor:
        data += data_cursor
        data_cursor = file.read(file_big_buffer)
    loop_times = math.floor(len(data) / udp_buffer_size) + 1
    for i in range(0, loop_times):
        start_pos = i*udp_buffer_size
        stop_pos = (i+1)*udp_buffer_size
        if stop_pos > file_size:
            stop_pos = file_size
        send_data = data[start_pos:stop_pos]
        print(len(send_data))


