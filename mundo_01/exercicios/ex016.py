#Crie um programa que leia um número Real qualquer pelo teclado e mostre na tela a sua porção Inteira.

'''#VERSÃO SIMPLES
numero = float(input("Digite um número real: "))
parte_inteira = int(numero)

print(f"A parte inteira de {numero} é {parte_inteira}")'''

#-------------------#

#USANDO A BIBLIOTECA MATH
import math
numero = float(input("Digite um número real: "))
parte_inteira = math.trunc(numero)

print(f"A parte inteira de {numero} é {parte_inteira}")

#int(nuemro) - Converte para inteiro, removendo a parte decimal
#math.trunc(numero) - Remove a parte decimal (igual ao int())

#obs: para testar as versões bastar tirar os (''')