# Tratar arquivos externos

def escrever_arquivo(texto):
    arquivo = open('teste.txt','w')
    arquivo.write(texto)
    arquivo.close()
import shutil

def copia_arquivos(nome_arquivo):
    shutil.copy(nome_arquivo, 'D:/Ari_ESTUDOS/PHYTON/notas-alunos.txt')



def atualizar_arquivo(texto):
    arquivo = open('teste.txt','a')
    arquivo.write(texto)
    arquivo.close()
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
    copia_arquivos('notas.txt')
    #escrever_arquivo('Primeira Linha. \n')
    #atualizar_arquivo('Segunda Linha. \n')
    #atualizar_arquivo('Terceira Linha. \n')
    ler_arquivo('teste.txt')