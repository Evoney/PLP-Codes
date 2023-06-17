class Gato:
    def __init__(self, nome, forca, defesa, energia):
        self.nome = nome
        self.forca = forca
        self.defesa = defesa
        self.energia = energia

    def atacar(self, gato):
        gato.defender(self.forca)

    def defender(self, dano):
        dano_amortecido = dano - self.defesa
        
        if dano_amortecido < 0:
            dano_amortecido = 0
        
        self.energia -= dano_amortecido
        
        if self.energia < 0:
            self.energia = 0
            
        print("Energia de {}: {}".format(self.nome, self.energia))
				
        if self.energia == 0:
            print("{} fugiu!".format(self.nome))

gato_atacante = Gato(**eval(input()))
numero_gatos = int(input())

gatos = []

for _ in range(numero_gatos):
    dados_gato = eval(input())
    gato = Gato(**dados_gato)
    gatos.append(gato)

print("{} esta atacando!".format(gato_atacante.nome))

for gato in gatos:
    gato_atacante.atacar(gato)
