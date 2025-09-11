#Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo.
#Calcule e mostre o comprimento da hipotenusa.

#VERSÃO USANDO MATEMÁTICA
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))

hipotenusa = (co ** 2 + ca ** 2) ** (1/2)

print(f"A hipotenusa vai medir {hipotenusa:.2f}")

#-------------------#
'''#VERSÃO USANDO A BIBLIOTECA MATH
from math import hypot
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = hypot(co, ca)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")'''

#hypot(*coordinates) - Norma euclidiana de um iterável de coordenadas

#=================#
'''import math
co = float(input("Digite o valor do cateto oposto: "))
ca = float(input("Digite o valor do cateto adjacente: "))
hipotenusa = math.sqrt(co **2 + ca ** 2)
print(f"A hipotenusa vai medir {hipotenusa:.2f}")'''

#sqrt(x) - Raiz quadrada

#obs: para testar as versões bastar tirar os (''')