# Copiar arquivo para outro diretório

import shutil

def copia_arquivos(nome_arquivo):
    shutil.copy(nome_arquivo, 'D:/Ari_ESTUDOS/PHYTON/notas-alunos.txt')


if __name__ == '__main__':
    copia_arquivos('notas.txt')


