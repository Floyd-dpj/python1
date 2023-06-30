import socket
socket_client = socket.socket()
socket_client.connect(("localhost", 8888))
while 1:
    msg = input("请输入要给服务器端发送的消息：")
    socket_client.send(msg.encode("UTF-8"))
    if msg == 'exit':
        break


    data = socket_client.recv(1024)       #阻塞语句
    print(f"服务端回复的消息是：{data.decode('UTF-8')}")

socket_client.close()





