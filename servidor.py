import base64, sys, datetime, threading
from protocolos.servidores import ServidorTCP, ServidorUDP
from utils import nomeDeUmaNovaImagem

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print(f"Uso: python3 {sys.argv[0]} <maquina> <tamanho_da_fila>")
        sys.exit(1)


MAQUINA = sys.argv[1]
FILA = sys.argv[2]

servidor = ServidorTCP("ipv4", MAQUINA, 1234, 2048, FILA)
log = ServidorUDP("ipv4", MAQUINA, 4321)
threading.Thread(target = log.receberClientes).start()
log.enviarBytesPorBroadcast("Servidor iniciado!")

while True:
    servidor.aceitarConexao()
    log.enviarBytesPorBroadcast("Novo three-way handshake!")
    nome_do_cliente = servidor.receberDados()
    log.enviarBytesPorBroadcast(f"Nome: {nome_do_cliente}.")
    base64_recebido = servidor.receberBase64PorPartes()
    log.enviarBytesPorBroadcast("Novos bytes em formato base64 recebidos...")
    string_do_base64 = base64.b64decode(base64_recebido)
    log.enviarBytesPorBroadcast("Bytes em formato base64 decodificados!")
    resultado = open('imagens/' + nomeDeUmaNovaImagem(nome_do_cliente), 'wb')
    log.enviarBytesPorBroadcast("Tentando criar nova imagem...")
    log.enviarBytesPorBroadcast("Escrevendo dados decodificados na imagem...")
    resultado.write(string_do_base64)
    log.enviarBytesPorBroadcast("Imagem gerada!")