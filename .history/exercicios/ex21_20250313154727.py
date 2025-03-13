import math

#maneira numero 1

##a = int (input('Qual o comprimento do cateto adjascente?: '))
hi = (co ** 2 + ca **2) ** (1/2)
print("A hipitenusa vai medir {:.2f}".format(hi))

# maneira numero 2
co = int (input('Qual o comprimento do cateto oposto?: '))
ca = int (input('Qual o comprimento do cateto adjascente?: '))
hi = math.hypot(co,ca)
print("A hipotenusa vai medir {:.2f}".format(hi))
