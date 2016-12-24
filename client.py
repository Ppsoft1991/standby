#!/usr/bin/python3
#coding = UTF-8

#################################
#           notyeat             #
#                               #
#################################

import socket
host = '172.24.0.24'    #设置服务器的IP
port = 4445             #设置服务器的PORT

def comm_whoami():
    user = b'whoami'
    client.sendall(user)
    whoami_response = client.recv(1024)
    whoami_response = str(whoami_response, encoding='utf8').strip('\n')
    return whoami_response


def comm_pwd():
    pwd = b'pwd'
    client.sendall(pwd)
    pwd_response = client.recv(1024)
    pwd_response = str(pwd_response,encoding='utf8').strip('\n')
    return pwd_response

def com_issue():
    issue = b'cat /etc/issue'
    client.sendall(issue)
    issue_response = client.recv(1024)
    issue_response = str(issue_response,encoding='utf8')
    issue_response = issue_response.split(" ")[0]
    return issue_response

client = socket.socket(2,socket.SOCK_STREAM)
client.connect((host,port))

def command_p():
    whoami = comm_whoami()
    pwd = comm_pwd()
    issue = com_issue()
    if whoami == 'root':
        permission = ' #'
    else:
        permission = ' $'
    comm = '\033[0;31m┌─['+'\033[01;31m'+whoami+'\033[01;33m@'+'\033[01;96m'+issue+'\033[0;31m─['+'\033[0;32m'+pwd+'\033[0;31m]\n'+'└──╼'+'\033[01;33m'+permission+'\033[0m'
    return comm


while True:
    comm = command_p()
    command = input(comm + ' ')
    if str(command) == 'exit':
        client.sendall(b'exit')
        client.close()
        break
    command = bytes(command, encoding='utf8')
    client.sendall(command)
    response = client.recv(1024)
    response = str(response, encoding='utf8')
    print(response)
client.close()

