import math

angulo = float (input('Digite o ângulo que você deseja: '))

seno = math.sin(math.radians(angulo))
coss = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print ("O ângulo de {} tem o SENO de {:.2f}, o COSSENO de {:.2f} e a TANGENTE de {:.2f}".format(angulo,seno,coss,tan))