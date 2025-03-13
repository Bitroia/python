preco = float (input('Qual o preço do produto?:R$ '))
desconto = preco * 0.05
precofinal = preco - desconto 
print("O produto está com desconto, e o seu novo preço é: {:.2f}".format(precofinal))