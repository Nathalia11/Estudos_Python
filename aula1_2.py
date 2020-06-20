print ('meu primeiro programa em Python')
a = 2
b = 3
soma = a + b
print(soma)


#Interagir com usuario
a = int(input('Entre com o primeiro valor:'))
b = int(input('Entre com o segundo valor:'))
print(type(a))

soma = a + b
subtracao = a - b
multiplicacao = a * b
divisao = a / b
resto = a % b

print ('soma: {}'.format(soma))
print('soma: ' + str(soma)) # = print(soma) mas com texto
print(subtracao)
print(multiplicacao)
print(int(divisao))  #o int tira a casa dos decimais/aredonda o numero
print(resto)
