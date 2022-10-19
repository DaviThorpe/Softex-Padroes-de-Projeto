# Aplique o padrão de projeto decorator para criar um sanduíche de frango assado com pepperoni e queijo mussarela ralado. 
# O projeto deve seguir os seguintes critérios:
# - deve imprimir no console: Sanduíche de Frango, Pepperoni, QueijoMussarelaRalado custa $7,49.
# - o sanduíche de frango assado custa $4,50.
# - o ingrediente adicional pepperoni custa $0,99.
# - o ingrediente adicional queijo mussarela ralado custa $2,00.
# - crie as classes necessárias: FrangoAssado, Pepperoni e QueijoMussarelaRalado.

# Inicio do código 

def QueijoMussarelaRalado(funcao):
    def wrapper():
        funcao()
        print ('O ingrediente adicional queijo mussarela ralado custa $2,00')
    return wrapper

def Pepperoni(funcao):
    def wrapper():
        funcao()
        print ('O ingrediente adicional pepperoni custa $0,99')
    return wrapper

def FrangoAssado(funcao):
    def wrapper():
        funcao()
        print ('O sanduiche de Frango Assado custa $4,50')
    return wrapper

@QueijoMussarelaRalado
@Pepperoni
@FrangoAssado
def sanduiche():

    print ('O sanduíche de Frango, Pepperoni, QueijoMussarelaRalado custa $7,49')

sanduiche()
