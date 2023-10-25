class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

class Filhos(Pessoa):
    def __init__(self, nome, idade, escola):
        super().__init__(nome, idade)
        self.escola = escola

    def resumo(self):
        print("Resumo do Filho:")
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Escola:", self.escola)

class Pai(Pessoa):
    def __init__(self, nome, idade, profissao):
        super().__init__(nome, idade)
        self.profissao = profissao

    def resumo(self):
        print("Resumo do Pai:")
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Profissão:", self.profissao)

class Mae(Pessoa):
    def __init__(self, nome, idade, estado_civil):
        super().__init__(nome, idade)
        self.estado_civil = estado_civil

    def resumo(self):
        print("Resumo da Mãe:")
        print("Nome:", self.nome)
        print("Idade:", self.idade)
        print("Estado Civil:", self.estado_civil)

if __name__ == '__main__':
    pai = Pai("Pai", 41, "Engenheiro")
    mae = Mae("Mãe", 36, "Casada")
    filho = Filhos("Filho", 11, "Escola Primária")

    pai.resumo()
    print()
    mae.resumo()
    print()
    filho.resumo()
