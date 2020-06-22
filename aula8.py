#MÓDULOS
# Importação de outros módulos
from aula7 import Calculadora
calculdora = Calculadora(5,10)
print(calculdora.soma())


#CRIANDO ARQUIVO
def escrever_arquivo(texto) :
    arquivo =  open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()
    
    
#ATUALIZANDO ARQUIVO
def atualizar_arquivo(texto) :
    arquivo = open('texto.txt', 'a')
    arquivo.write(texto)
    arquivo.close()



#LER O ARQUIVO
def ler_arquivo(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        texto = arquivo.read()
        print(texto)


if __name__ == '__main__':
    escrever_arquivo('Primeira linha.\n')
    atualizar_arquivo('Terceira linha.\n')
    ler_arquivo('teste.txt')







def escrever_arquivo(texto) :
    arquivo =  open('teste.txt', 'w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto) :
    arquivo = open(nome_arquivo, 'a')
    arquivo.write(texto)
    arquivo.close()


def ler_arquivo(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        texto = arquivo.read()
        print(texto)

#MANIPULAR ARQUIVOS
def media_nota(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    aluno_nota = arquivo.read()
    print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    print(aluno_nota)
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas]) /4
        print(media(lista_notas))

#COPIAR E MOVER ARQUIVO
def copia_arquivo(nome_arquivo):
    import shutil
    shutil.copy(nome_arquivo, 'C:/Users/Fatima/PycharmProjects/notas_alunos.txt')

def move_arquivo(nome_arquivo):
    import shutil
    shutil.move(nome_arquivo, 'C:/Users/Fatima/PycharmProjects/notas_alunos')

if __name__ == '__main__':
    move_arquivo('notas.txt')
    copia_arquivo('notas.txt')
    media_nota('nota.txt')
    escrever_arquivo('Primeira linha.\n')
    aluno =  '\nCarlos,8,9,6,7'
    atualizar_arquivo('nota.txt', aluno)
    ler_arquivo('teste.txt')
