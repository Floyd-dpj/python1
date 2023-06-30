import socket
socket_server = socket.socket()
socket_server.bind(("localhost", 8888))

socket_server.listen(1)
conn, address = socket_server.accept()
print(f"接收到了客户端调度链接：{address}")


while True:
    data: str  = conn.recv(1024).decode("UTF-8")
    print("\n")
    print(f"客户端发来的信息是：{data}" )

    msg = input("请输入你想要和客户端回复的消息：")
    if msg == 'exit':
        break
    conn.send(msg.encode("UTF-8"))

conn.close()

socket_server.close()
