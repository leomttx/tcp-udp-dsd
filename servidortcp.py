import base64, sys, datetime, threading
from servidores import ServidorTCP, ServidorUDP

def nomeDeUmaNovaImagem(nome_do_cliente):
    agora = datetime.datetime.now()
    return str(nome_do_cliente + " ({}h{}m{}s).png".format(agora.hour, agora.minute, agora.second))

def receberBase64PorPartes(self):
    receptor_do_base64 = b''
    while True:
        fragmento = self.receberBase64()
        if not fragmento:
            break
        receptor_do_base64 += fragmento
    base64_completo = receptor_do_base64
    return base64_completo

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Uso: python3 servidortcp.py <maquina> <tamanho_da_fila>")
        sys.exit(1)


MAQUINA = sys.argv[1]
FILA = sys.argv[2]

servidor = ServidorTCP("ipv4", MAQUINA, 1234, 2048, FILA)
log = ServidorUDP("ipv4", MAQUINA, 4321)
threading.Thread(target = log.receberClientes).start()

while True:
    log.enviarBytesPorBroadcast("Humpf, coff, cof")
    servidor.aceitarConexao()
    log.enviarBytesPorBroadcast("Novo three-way handshake!")
    nome_do_cliente = servidor.receberDados()
    log.enviarBytesPorBroadcast(f"Nome: {nome_do_cliente}.")
    base64_recebido = receberBase64PorPartes(servidor)
    log.enviarBytesPorBroadcast("Novos bytes em formato base64 recebidos...")
    string_do_base64 = base64.b64decode(base64_recebido)
    log.enviarBytesPorBroadcast("Bytes em formato base64 decodificados!")
    resultado = open('imagens/' + nomeDeUmaNovaImagem(nome_do_cliente), 'wb')
    log.enviarBytesPorBroadcast("Tentando criar nova imagem...")
    log.enviarBytesPorBroadcast("Escrevendo dados decodificados na imagem...")
    resultado.write(string_do_base64)
    log.enviarBytesPorBroadcast("Imagem gerada!")