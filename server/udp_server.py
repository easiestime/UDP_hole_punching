import socket
import router
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
server_address = ("0.0.0.0", 31888)
server_socket.bind(server_address)

request_router = router.router(server_socket)

print("UDP server started")



while True:
    data, client_address = server_socket.recvfrom(1024)
    # 打印接收到的数据和客户端地址
    print(f"接收到来自 {client_address} 的数据: {data.decode('utf-8')}")
    request_router.commonResponse(data.decode('utf-8'), client_address)
    # # 可选：向客户端发送响应数据
    # response = "已收到数据"
    # server_socket.sendto(response.encode('utf-8'), client_address)