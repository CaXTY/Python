#faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

numero = int(input("Digite um número inteiro para ver a sua tabuada: "))

print(f"\nTabuada do {numero}:")
print("=" * 15)

for i in range(0, 11):
    resultado = numero * i
    print(f"{numero} x {i:2} = {resultado:3}")

print("=" * 15)

#usa um loop FOR para calcular a tabuada de 1 a 10