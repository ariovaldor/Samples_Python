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
def media_notas(nome_arquivo):
        arquivo = open(nome_arquivo, 'r')
        aluno_nota = arquivo.read()
        print(aluno_nota)
        aluno_nota = aluno_nota.split('\n')
        for x in aluno_nota:
            print(x)


if __name__ == '__main__':
    media_notas('notas.txt')
    aluno = 'Felipe,7,8,5,6 \n'
   atualizar_arquivo('notas.txt', aluno)
   #atualizar_arquivo('Terceira Linha. \n')
    ler_arquivo('notas.txt')