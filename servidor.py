import random
from xmlrpc.server import SimpleXMLRPCServer

opcoes = {"pedra": 0, "papel": 1, "tesoura": 2}

opcoes_reversas = {v: k for k, v in opcoes.items()}

def vencedor(jogador, pc):
    if jogador == pc:
        return "Empate"
    elif (jogador == 0) & (pc == 1) | (jogador == 1) & (pc == 2) | (jogador == 2) & (pc == 0):
        return "Computador"    
    else:
        return "Jogador"

def jogar_jokenpo(jogador):
    jogador = opcoes.get(jogador, -1)
    if jogador == -1:
        return "Escolha inválida! Digite: pedra, papel ou tesoura."
    
    pc = random.randint(0, 2)
    jg_vencedor = vencedor(jogador, pc)
    
    return f"\nJogador escolheu: {opcoes_reversas[jogador]}\nComputador escolheu: {opcoes_reversas[pc]}\nVencedor: {jg_vencedor}\n"

server = SimpleXMLRPCServer(("localhost", 8000))
server.register_function(jogar_jokenpo, "jogar_jokenpo")

print("Servidor RPC está funcionando na porta 8000...")

try:
    server.serve_forever()
finally:
    server.server_close()
