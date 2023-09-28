import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

def jogar():
    while True:
        jogada = input("Escolha entre pedra, papel ou tesoura (ou 'sair' para sair): ").lower()
        if jogada == 'sair':
            break
        
        resultado = proxy.jogar_jokenpo(jogada)
        print(resultado)

if __name__ == "__main__":
    jogar()
