# #Comando FOR
for x in range(1, 100):
    print(x)



a = int(input('Entre com o número: '))
div = 0
for x in range (1, a+1) :
    resto = a % x
    print (x, resto)
    if resto == 0 :
        div = div + 1

if div == 2:
    print('Número {} é primo'. format(a))
else:
    print ('Número {} naõ é primo'. format(a))



#Citando números primos
a = int(input('Entre com o valor: '))
for num in range(a + 1):
    div = 0
    for x in range (1, num + 1) :
        resto = num % x
        if resto == 0 :
            div = div + 1
    if div == 2:
                print(num)
                
                

a = 0
while a < 10:
    print(a)
    a = a + 1


nota = int (input('Entre com a nota: ')) #while força voce a digitar corretamente
while nota > 10:
    nota = int(input('Nota invalida. Entre com a nota correta: '))
    print(nota)
