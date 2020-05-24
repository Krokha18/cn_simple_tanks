import socket
import pickle #для работы с потоком байтов


class Network:
    def __init__(self):
        self.client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM) #две константы
        self.server = "192.168.1.140" #мой IP
        self.port = 5555
        self.addr = (self.server, self.port) #пара host-port
        self.p = self.connect()  #обьект - поток байтов
        

    def get_player(self):
        return self.p
    #выполнить соединение клиент-сервер, вернуть полученные данные с сокета, 2048 - размер буфера
    def connect(self):
        try:
            self.client.connect(self.addr)
            return pickle.loads(self.client.recv(2048))
        except:
            pass

    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return 0
        except socket.error as e:
            print(e)

    def receive(self):
        try:
            return pickle.loads(self.client.recv(2048))
        except socket.error as e:
            print(e)

