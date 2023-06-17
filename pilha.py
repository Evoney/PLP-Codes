class Pilha:
    def __init__(self):
        self._elementos = []

    @property
    def topo(self):
        if self._elementos:
            return self._elementos.pop()
        else:
            return None

    @topo.setter
    def topo(self, valor):
            self._elementos.append(valor)

    @property
    def vazia(self):
        return len(self._elementos) == 0

def verifica_balanceamento(expressao):
    pilha = Pilha()

    for caractere in expressao:
        if caractere in "([{":
            pilha.topo = caractere
        elif caractere in ")]}":
            if pilha.vazia:
                return False
                
            topo = pilha.topo
            
            if (caractere == ")" and topo != "(") or (caractere == "]" and topo != "[") or (caractere == "}" and topo != "{"):
                return False

    return pilha.vazia

expr = input()

if verifica_balanceamento(expr):
	print("sim")
else:
	print("nao")
