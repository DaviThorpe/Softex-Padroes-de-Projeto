# Crie um adaptador que permita que um objeto do tipo Pato seja usado como se fosse um objeto do tipo Galinha.
# Siga o exemplo apresentado no Hipertexto 4 e crie as classes AdaptadorPato e AdaptadorPatoDemo para demonstrar o uso da classe AdaptadorPato.

# Inicio do código

#interface Pato
class Pato:
    def fazqua(self):
        pass

class PatoSelvagem(Pato):
    def fazqua(self):
        print('É um pato selvagem')

class SomPato:
    def som(self, som_pato):
        som_pato.fazqua()

#interface galinha
class Galinha:
    def fazco(self):
        pass

class GalinhaCarijo:
    def som(self, som_galinha):
        print('É uma galinha carijó')
        som_galinha.fazco()

#adaptador
class AdaptadorPato(Galinha):
    def __init__(self, som_pato):
        self.som_pato = som_pato 
    
    def provide_eletricy(self):
        self.som_pato.fazqua()

def AdaptadorPatoDemo():
    som_pato = PatoSelvagem()
    galinha_carijo = GalinhaCarijo()
    adaptador = AdaptadorPato(som_pato)
    galinha_carijo.som(adaptador)

AdaptadorPatoDemo()
