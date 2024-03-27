import base64, sys, datetime
from servidores import ServidorTCP

def nomeDeUmaNovaImagem():
    agora = datetime.datetime.now()
    return str("image-received-at-{}-{}-{}-{}-{}-{}.png".format(agora.year, agora.month, agora.day, agora.hour, agora.minute, agora.second))

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
    if len(sys.argv) != 6:
        print("Uso: python3 <familia_de_sockets> <maquina> <porta> <tamanho_do_buffer> <tamanho_da_fila>")
        sys.exit(1)


FAMILIA_DE_SOCKETS = sys.argv[1]
MAQUINA = sys.argv[2]
PORTA = sys.argv[3]
BUFFER = sys.argv[4]
FILA = sys.argv[5]

servidor = ServidorTCP(FAMILIA_DE_SOCKETS, MAQUINA, PORTA, BUFFER, FILA)
servidor.aceitarConexao()
base64_recebido = receberBase64PorPartes(servidor)
string_do_base64 = base64.b64decode(base64_recebido) 
resultado = open('imagens/' + nomeDeUmaNovaImagem(), 'wb')
resultado.write(string_do_base64)