# Considerando a solução apresentada no Hipertexto 5, aplique o padrão de projeto Strategy para criar uma simples calculadora. 
# Os requisitos para avaliar o projeto são:
# - implementar uma interface Strategy com o método abstrato execute(). Deve haver três classes concretas 
# que implementam a Strategy para realizar as operações de Soma, Subtração e Multiplicação de números inteiros;
# - o método execute() deve receber dois números inteiros como parâmetros e retornar o resultado também como número inteiro;
# - como input do usuário, a aplicação deve receber o primeiro valor, depois o segundo e, por último, a operação matemática que deve realizar;
# - no final, a aplicação deve definir qual Strategy será usada, com base na operação informada, e imprimir o resultado da operação.

# Inicio do código

from abc import ABC, abstractmethod

class Operacao(ABC):
    @abstractmethod
    def execute(self, n1, n2):
        pass

class Soma(Operacao):
    def execute(self, n1, n2):
        return n1 + n2
       

class Subtracao(Operacao):
    def execute(self, n1, n2):
        return n1 - n2

class Multiplicacao(Operacao):
    def execute(self, n1, n2):
        return n1 * n2

class Calculadora():
    def __init__(self):
        self._num1 = 0
        self._num2 = 0
        self._operador = None

# A partir dessa etapa não entendi muito bem, apenas segui os passos que vi em outro projeto

    @property
    def num1(self):
        return self._num1

    @property
    def num2(self):
        return self._num2

    @property
    def operador(self) -> Operacao:
        return self._operador

    @num1.setter
    def num1(self, novo_num):
        self._num1 = novo_num

    @num2.setter
    def num2(self, novo_num):
        self._num2 = novo_num

    @operador.setter
    def operador(self, operador: Operacao) -> None:
        self._operador = operador

    def __call__(self):
        return (self._operador.execute(self.num1, self.num2))


# Aqui já fiz sabendo o que estava fazendo, preciso de mais estudo para entender completamente a etapa anterior

def teste():
    Calculadora_object = Calculadora()

    Calculadora_object.num1 = int(input('Insira um numéro inteiro: '))
    Calculadora_object.num2 = int(input('Insira outro número inteiro: '))
    operador = input('Escolha entre os tres operadores. Para somar "+", para subtrair "-", para multiplicar "*": ')

    if operador == '+':  
        Calculadora_object.operador = Soma()
    elif operador == '-':
        Calculadora_object.operador = Subtracao()
    elif operador == '*':
        Calculadora_object.operador = Multiplicacao()
    else: 
        print ('Operador inválido')

    resultado = Calculadora_object()

    print (resultado)

teste()