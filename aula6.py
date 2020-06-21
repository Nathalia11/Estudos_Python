#Conjuntos aritimeticos
conjunto = {1,2,3,4,4,2}
conjunto.add(5)
conjunto.discard(4)
print(conjunto)




conjunto = {1,2,3,4,5}
conjunto2 = {5,6,7,8}
#UNIÃO
conjunto_uniao = conjunto.union(conjunto2)
print(conjunto_uniao)
#INTERSECÇÃO
conjunto_interseccao = conjunto.intersection(conjunto2)
print(conjunto_interseccao)
#DIFERENÇA
conjunto_diferenca1 = conjunto.difference(conjunto2)
conjunto_diferenca2 = conjunto.difference(conjunto)
print(conjunto_diferenca1)
print(conjunto_diferenca2)
#DIFERENÇA SIMÉTRICA
conjunto_diff_simetrica = conjunto.symmetric_difference(conjunto2)
print(conjunto_diff_simetrica)






#PERTINENCIA
conjunto_a = {1,2,3}
conjunto_b = {1,2,3,4,5}
#SUBCONJUNTO
conjunto_subset = conjunto_a.issubset(conjunto_b)
print(conjunto_subset)
#SUPERCONJUNTO
conjunto_superset = conjunto_b.issuperset(conjunto_a)
print(conjunto_superset)





#CONVERÇÃO DE LISTA PARA CONJUNTO
lista = ['cachorro', 'cachorro', 'gato', 'gato', 'elefante']
print(lista)
conjunto_animais = set(lista)
print(conjunto_animais)
lista_animais = list(conjunto_animais)
print(lista_animais)


