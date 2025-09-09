#Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

#Lendo o valor em metros
metros = float(input('Digite um valor em metros: '))

#Convertendo para centímetros e milímetros
centimetros = metros * 100
milimetros = metros * 1000

#Mostrando os resultados
print(f'\nCoversões: ')
print(f'{metros:.2f} metros equivalem a: ')
print(f'{centimetros} centímetros')
print(f'{milimetros} milimetros')

#Relações de conversão:

#1 metro = 100 centímetros
#1 metro = 1000 milímetros
