import socket
print("helloworld")
serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind參數是一個tuple 放主機名，埠號
serverSocket.bind((socket.gethostname(), 1234, ))

#最多等待5個連線
serverSocket.listen(5)
while True:
    conn, addr = serverSocket.accept()
    print('connect from', addr)

    while True:

        #讀取1024byte
        data = conn.recv(2048)
        if not data:
            break
        print(data)
    #conn.send(data)

    conn.close()

serverSocket.close()