# A palavra "class" é usada para criar uma classe. 
# Uma classe funciona como um molde para criar objetos
class Carro:

#"def" definir uma função ou método
# "__init__" é o método construtor da classe.
# Ele é executado automaticamente quando um objeto é criado

# "self" representa o própio objeto.
# É através do self que acessamos atributos e métodos do objeto

# "marca" , "modelo" , "ano" , e "velocidade"
# São Parãmentros recebidos pela classe.

   # método Contrutor
    def __init__ (self, marca, modelo, ano, velocidade=0):
      self.marca = marca
      self.modelo = modelo
      self.ano = ano
      self.velocidade = velocidade 

   # Métodos
   # método acelerar
   def acelerar(serf, aumento)
     # serf.velocidade = self.velocidade + aumento
       serf.velocidade += aumento

       print(f"O carro acelerou para {serf.velocidade} km/h")


    # Criando um objeto da Classe Carro
    
    # carro1 é uma variável que recebe um objeto 
carro1 = Carro("Chevrolet", "S10", 2013)

# Exibir informações do carro
print(f"Marca: {carro1.marca}")
print(f"Modelo: {carro1.modelo}")
print(f"Ano: {carro1.ano}")
print(f"Ano: {carro1.velocidade}")

carro1.acelerar(50)


carro2 = Carro("FIT", "UNO", 2009)
print(f"Marca: {carro2.marca}")
print(f"Modelo: {carro2.modelo}")
print(f"Ano: {carro2.ano}")

carro3 = Carro("Ford", "F250", 2008)
print(f"Marca: {carro3.marca}")
print(f"Modelo: {carro3.modelo}")
print(f"Ano: {carro3.ano}")