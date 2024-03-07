import utils
import socket

class ServidorTCP():
    def loop(self):
        while True:
            print("[🎧 servidor TCP em modo de escuta no endereço %s]" % str(self.maquina + ":" + str(self.porta)))
            socket_cliente, endereco_cliente = self.socket_servidor.accept()

    def habilitarModoDeEscuta(self, tamanho_da_fila = 5):
        self.socket_servidor.listen(tamanho_da_fila)

    def configurarSocketParaEscutarNoEndereco(self, maquina, porta):
        endereco = (maquina, porta)
        self.socket_servidor.bind(endereco)
    
    def instanciarSocket(self, familia):
        familia_de_sockets = utils.getFamilia(familia)
        instancia = socket.socket(familia_de_sockets, socket.SOCK_STREAM)
        return instancia

    def __init__(self, familia, maquina, porta):
        self.familia = familia
        self.maquina = maquina
        self.porta = porta
        self.socket_servidor = self.instanciarSocket(self.familia)
        self.socket_servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.configurarSocketParaEscutarNoEndereco(self.maquina, self.porta)
        self.habilitarModoDeEscuta(5)
        self.loop()

        
s = ServidorTCP("IPV4", 'localhost', 8082)
print(s)