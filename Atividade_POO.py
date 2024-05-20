class Pessoa:
    def __init__(self, nome, peso, idade):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.comendo = False
        self.dormindo = False
        self.falando = False

    def comer(self, alimento):
        if self.dormindo:
            print(f"{self.nome} não pode comer pois está dormindo.")
        elif self.falando:
            print(f"{self.nome} não pode comer pois está falando.")
        else:
            print(f"{self.nome} está comendo {alimento}.")
            self.comendo = True

    def parar_comer(self):
        if self.comendo:
            print(f"{self.nome} parou de comer.")
            self.comendo = False
        else:
            print(f"{self.nome} não está comendo.")

    def falar(self):
        if self.falando:
            print(f"{self.nome} já está falando.")
        elif self.comendo:
            print(f"{self.nome} não pode falar pois está comendo.")
        elif self.dormindo:
            print(f"{self.nome} não pode falar pois está dormindo.")
        else:
            print(f"{self.nome} está falando.")
            self.falando = True

    def parar_falar(self):
        if self.falando:
            print(f"{self.nome} parou de falar.")
            self.falando = False
        else:
            print(f"{self.nome} não está falando.")

    def dormir(self):
        if self.comendo:
            print(f"{self.nome} não pode dormir pois está comendo.")
        elif self.falando:
            print(f"{self.nome} não pode dormir pois está falando.")
        else:
            print(f"{self.nome} está dormindo.")
            self.dormindo = True

    def parar_de_dormir(self):
        if self.dormindo:
            print(f"{self.nome} parou de dormir.")
            self.dormindo = False
        else:
            print(f"{self.nome} não está dormindo.")
