def media_notas(nome_arquivo):
    arquivo = open(nome_arquivo,'r')
    aluno_nota = arquivo.read()
    #print(aluno_nota)
    aluno_nota = aluno_nota.split('\n')
    for x in aluno_nota:
        lista_notas = x.split(',')
        aluno = lista_notas[0]
        lista_notas.pop(0)
        print(aluno)
        print(lista_notas)
        media = lambda notas: sum([int(i) for i in notas])/ 4
        print(media(lista_notas))


if __name__ == '__main__':
    media_notas('notas.txt')
   # atualizar_arquivo('media_notas, aluno)
    #atualizar_arquivo('Terceira Linha. \n')
    #ler_arquivo('notas.txt')