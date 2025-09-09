#SOMANDO DOIS NÚMEROS
print ('===Desafio 02===')
#Solicita dos números ao usuário
num1 = int(input('Digite um valor: '))
num2 = int(input('Digite outro valor: '))

#Tenta converter e somar
try:
    soma = float(num1) + float(num2)
    print(f'A soma entre {num1} + {num2} é {soma}')
except ValueError:
    print("⚠️ Ops! Certifique-se de digitar apenas números.")