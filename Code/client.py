import socket


class Client:
    def __init__(self):
        self.HOST='127.0.0.1'
        self.PORT=5555
        self.sock=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.connect((self.HOST,self.PORT))
        
    def close(self):
        self.sock.close()
        
    def send(self,info):
        self.sock.sendall(bytearray(info,'utf-8'))
        
    def receive(self):
        data = self.sock.recv(2048)
        data = data.decode("utf-8")
        return data
        
        