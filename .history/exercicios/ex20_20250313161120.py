import random

aluno1 = str (input('Nome do aluno 1: '))
aluno2 = str (input('Nome do aluno 2: '))
aluno3 = str (input('Nome do aluno 3: '))
aluno4 = str (input('Nome do aluno 4: '))

alunos = [aluno1,aluno2, aluno3, aluno4]

escolhido = random.choice(alunos)

print("O aluno escolhido foi: {}".format(escolhido))
