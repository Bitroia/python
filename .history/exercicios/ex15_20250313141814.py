salarioinicial = float (input("Digite o salário do funcionário: "))
aumento = salarioinicial * 0.15
salariofinal = aumento + salarioinicial
print ("O seu novo salário teve um aumento e agora é: R${:.2}".format(salariofinal))