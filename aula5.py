#Aprendendo sobre Listas e Tuplas
lista = [1,3,5,7]
lista_animal = ['cachorro', 'gato', 'elefante']
print (lista_animal[1])
nova_lista = lista_animal * 3
print(nova_lista)



print(sum(lista)) #somando os numeros da lista
print(max(lista)) #o maior valor da lista
print(min(lista)) #o menor valor da lista




lista = [1,3,5,7]
lista_animal = ['cachorro', 'gato', 'elefante']
if 'lobo' in lista_animal:
    print('Existe um gato na lista')
else:
    print('Não existe um lobo na lista.Será incluido.')
    lista_animal.append('lobo')  #adciona um novo elemto na lista
    print(lista_animal)
lista_animal.pop()  #retira o ultima elemento da lista
print(lista_animal)



lista = [10,3,7,5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']
lista.sort()  #ordena os elementos dentro da lista
lista_animal.sort()
print(lista)
print(lista_animal)
lista_animal.reverse()  #ordena de forma reversa os elemetos da lista
print(lista_animal)
lista_animal[0] = 'macaco'  #altero o elemento
print(lista_animal)




#Tuplas
lista = [10,3,7,5]
lista_animal = ['cachorro', 'gato', 'elefante', 'lobo', 'arara']

tupla = (1, 10, 12, 14)
print (len(tupla))

tupla_animal = tuple(lista_animal)  #convertendo lista em tupla
print(tupla_animal)
