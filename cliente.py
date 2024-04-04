import sys, random, base64
from protocolos.clientes import *

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Uso: python3 {sys.argv[0]} <seu-nome> <endereco-ip>")
        sys.exit(1)


NOME = sys.argv[1]
ENDERECO_IP = sys.argv[2]

eh_log = random.choice([True, False])

if eh_log:
    input("Seu programa está configurado para ser um log com UDP. Pressione ENTER para continuar...")
    clienteudp = ClienteUDP("ipv4", "localhost", 4321)
    clienteudp.receberMensagensEmBroadcast()
else:
    input("Seu programa está configurado para ser um cliente com TCP. Antes de continuar, certifique-se de ter baixado a imagem. Pressione ENTER...")
    clientetcp = ClienteTCP("ipv4", ENDERECO_IP, 1234, 2048)
    clientetcp.conectarAoServidor()
    clientetcp.enviarDados(NOME)
    imagem = open('entrada.png', 'rb')
    string_binaria_da_imagem = imagem.read()
    base64_da_string = base64.b64encode(string_binaria_da_imagem)
    clientetcp.enviarBase64PorPartes(base64_da_string, clientetcp.buffer)
    clientetcp.encerrarConexao()