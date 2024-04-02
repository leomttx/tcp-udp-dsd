import sys, random, base64
from clientes import *

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Uso: python3 {sys.argv[0]} <seu-nome> <endereco-ip>")
        sys.exit(1)


NOME = sys.argv[1]
ENDERECO_IP = sys.argv[2]

eh_log = random.choice([True, False])

if eh_log:
    clienteudp = ClienteUDP("ipv4", "localhost", 4321)
    clienteudp.receberMensagensEmBroadcast()
else:
    clientetcp = ClienteTCP("ipv4", ENDERECO_IP, 1234, 2048)
    clientetcp.conectarAoServidor()
    clientetcp.enviarDados(NOME)
    imagem = open('entrada.png', 'rb')
    string_binaria_da_imagem = imagem.read()
    base64_da_string = base64.b64encode(string_binaria_da_imagem)
    clientetcp.enviarBase64PorPartes(base64_da_string, clientetcp.buffer)
    clientetcp.encerrarConexao()