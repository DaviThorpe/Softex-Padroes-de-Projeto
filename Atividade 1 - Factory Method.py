# Aplique o Factory Method para fabricar computadores, usando como base o exemplo visto de static e parametrizado no hipertexto.

# Considere que:
# - os produtos devem implementar uma interface comum;
# - o cliente deve utilizar apenas a fábrica para criar instâncias do tipo abstrato da interface;
# - todo computador deve ter, com getters, os atributos: ram, hdd, cpu e type;
# - há dois tipos de computadores: pc e server;
# - RAM e HD devem estar em GB;
# - CPU deve estar em GHz;
# - através do tipo informado, a fábrica decide qual tipo de computador irá instanciar;
# - quando o método .toString() for aplicado a um computador, ele deve imprimir seus atributos.

# Inicio do código

from abc import ABC, abstractclassmethod

class Fabrica :
    def criar_computador(self):
      pass
    def fabricar(self) :
      computador = self.criar_computador()
      result = (f"Computador: {computador.setup()}")

      return  result

class Fabricar_pc(Fabrica):
    def __init__(self, ram, hd, cpu):
      self.ram = ram
      self.hd = hd
      self.cpu = cpu
        	  
    def criar_computador(self):
     return Pc (str(self.ram), self.hd, self.cpu)

class Fabricar_server (Fabrica):
    def __init__(self, ram, hd, cpu):
      self.ram = ram
      self.hd = hd
      self.cpu = cpu

    def criar_computador(self):
     return Server(self.ram, self.hd, self.cpu)

#Criando a interface

class Computador (ABC) : 
      @abstractclassmethod
      def setup(self):
        pass
    
class Pc (Computador):
    def __init__ (self, ram, hd, cpu):
      self.ram = ram
      self.hd = hd
      self.cpu = cpu
      self.tipo = 'PC'
    def setup(self):
      result = (f"Configuração: memória RAM: {self.ram} GB, HD: {self.hd} GB, CPU: {self.cpu} GHZ")
      return result

class Server (Computador):
    def __init__ (self, ram, hd, cpu):
      self.ram = ram
      self.hd = hd
      self.cpu = cpu
      self.tipo = 'Server'
    def setup(self):
      result = (f"Configuração: memória RAM: {self.ram} GB, HD: {self.hd} GB, CPU: {self.cpu} GHZ")
      return result
	

def criando (fabrica: Fabrica):
	print(f"Computador fabricado pela {fabrica.__class__.__name__}.", f"{fabrica.fabricar()}")


def montagem():
	ram = int(input('Informe a quantidade de memória RAM em GB do computador: '))
	hd = int(input('Informe quantos GB terá o armazenamento do computador: '))
	cpu = float(input('Informe quantos GHz a CPU terá: '))
	type = input('Seu computador será utilizado como "PC" ou "Server")? ')


	if type == 'PC':
		criando(Fabricar_pc(ram, hd, cpu))
	elif type == 'Server':
		criando(Fabricar_server(ram, hd, cpu))

i = "1"
while i != '2':
  montagem()
  i = str(input('Para continuar a montagem digite "1", para interromper a montagem digite "2": '))
