#Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

#Lendo o número do usuário
numero = float(input('Digite um número: '))

#Calculando o dobro, triplo e raiz quadrada
dobro = numero * 2
triplo = numero * 3
raiz = numero ** (1/2) # ou :2f - formata a raiz quadrada para mostrar 2 casas decimais

#Mostrando os resultados
print(f'O seu numero digitado foi: {numero}')
print(f'Seu dobro é: {dobro}')
print(f'Seu triplo é: {triplo}')
print(f'Sua raiz quadrada é: {raiz}')

#Funcionamento do programa
#Float(input()) - lê o numero como ponto flutuante (aceita números inteiros e decimais)
#numero * 2 - calcula o dobro
#numero * 3 calcula o triplo
#numero ** (1/2) - calcula a raiz quadrada (elevando a 0.5)
