import random

aluno1 = str (input('Nome do aluno 1: '))
aluno2 = input('Nome do aluno 2: ')
aluno3 = input('Nome do aluno 3: ')
aluno4 = input('Nome do aluno 4: ')

alunos = [aluno1,aluno2, aluno3, aluno4]

random.shuffle(alunos)

print("Ordem de apresentação: {}".format(alunos))
