# Tratar arquivos externos

def escrever_arquivo(texto):
    arquivo = open('teste.txt','w')
    arquivo.write(texto)
    arquivo.close()

def atualizar_arquivo(nome_arquivo, texto):
    arquivo = open(nome_arquivo,'a')
    arquivo.write(texto)
    arquivo.close()
def ler_arquivo(nome_arquivo):
    arquivo = open(nome_arquivo, 'r')
    texto = arquivo.read()
    print(texto)

if __name__ == '__main__':
#    copia_arquivos('notas.txt')
    #aluno = 'Fernanda,6,8,9,9 \n'
    #atualizar_arquivo('notas.txt', aluno)
    #atualizar_arquivo('Terceira Linha. \n')
    #ler_arquivo('notas.txt')