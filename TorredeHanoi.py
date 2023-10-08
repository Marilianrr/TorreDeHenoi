class TorreHanoi:
    def __init__(self, num_discos):
        self.num_discos = num_discos
        self.pino_inicial = Pilha()
        self.pino_intermediario = Pilha()
        self.pino_destino = Pilha()
        self.movimentos = 0

        for disco in range(num_discos, 0, -1):
            self.pino_inicial.push(disco)

    def resolver_hanoi(self, n, origem, destino, intermediario):
        if n == 1:
            disco = origem.pop()
            destino.push(disco)
            self.movimentos += 1
            self.mostrar_pinos()
            input("Pressione [ENTER] para continuar...")
        else:
            self.resolver_hanoi(n - 1, origem, intermediario, destino)
            self.resolver_hanoi(1, origem, destino, intermediario)
            self.resolver_hanoi(n - 1, intermediario, destino, origem)

    def mostrar_pinos(self):
        print(f"Posição Atual: {self.movimentos} passos")
        print(f"Pino Inicial: {self.pino_inicial.pilha}")
        print(f"Pino Intermediário: {self.pino_intermediario.pilha}")
        print(f"Pino Destino: {self.pino_destino.pilha}")
        print("\n")

    def executar(self, passos_entre_visualizacoes=1):
        print("Resolvendo a Torre de Hanói com", self.num_discos, "discos.")
        self.mostrar_pinos()

        self.resolver_hanoi(self.num_discos, self.pino_inicial, self.pino_destino, self.pino_intermediario)

        print("Posição Final:", self.movimentos, "passos")

        input("Pressione [ENTER] para encerrar...")

class Pilha:
    def __init__(self):
        self.pilha = []

    def push(self, dado):
        self.pilha.append(dado)

    def pop(self):
        if not self.pilha_esta_vazia():
            return self.pilha.pop()
        else:
            raise Exception("A pilha está vazia")

    def pilha_esta_vazia(self):
        return len(self.pilha) == 0

if __name__ == "__main__":
    num_discos = int(input("Digite o número de discos: "))
    passos_entre_visualizacoes = int(input("Número de movimentações entre visualizações: "))

    torre_hanoi = TorreHanoi(num_discos)
    torre_hanoi.executar(passos_entre_visualizacoes)
