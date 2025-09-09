#FAÇA UM PROGRAMA QUE LEIA UM NÚMERO INTEIRO E MOSTRE NA TELA O SEU SUCESSOR E SEU ANTECESSOR.

# Lendo o número inteiro do usuário
numero = int(input('Digite um número inteiro: '))

#Calculando o sucessor e antecessor
sucessor = numero + 1
antecessor = numero - 1

#Mostrando os resultados
print(f'O número digitado foi: {numero}')
print(f'Seu sucessor é: {sucessor}')
print(f'Seu antecessor é: {antecessor}')

#Funcionamento do programa
#input() - lê a entrada do usuário como string
#int() - converte a string para número inteiro
#numero + 1 - calcula o sucessor (próximo número)
#numero - 1 - calcula o antecessor (número anterior)
#print - exibe os resultados na tela