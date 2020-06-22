#MÉTODO E CLASSE
#No Pytho o método é def!
def soma(a,b):
    return a + b

print (soma(1,2))
print (soma(3,4))

def subtracao(a,b):
    return a - b
print(subtracao(10,2))
print(subtracao(5,2))

def multiplicacao(a,b):
    return a * b
print(subtracao(10,2))

def divisao(a,b):
    return a / b
print(divisao(10,2))



#CLASSE
class Calculadora:

    def soma(self, valor_a, valor_b):
          return valor_a + valor_b


    def subtracao(self, valor_a,valor_b):
        return valor_a - valor_b

    def multiplicacao(self, valor_a, valor_b):
            return valor_a * valor_b

    def divisao(self, valor_a,valor_b):
            return valor_a / valor_b

calculadora = Calculadora()
print(calculadora.soma(10,2))
print(calculadora.subtracao(5,3))
print(calculadora.divisao(100,2))
print(calculadora.multiplicacao(50,10))

