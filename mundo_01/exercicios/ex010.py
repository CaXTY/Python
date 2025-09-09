#crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.
#considere US$1.00 = R$5.41

print("=" * 50)
print("CONVERSOR DE MOEDA - REAL PARA DÓLAR")
print("=" * 50)

#Cotação fixa do dólar
cotacao_dolar = 5.41

#Lê o valor em reias
reais = float(input('\nDigite o valor da sua carteira em reais R$: '))

#Calcula a conversão
dolares = reais / cotacao_dolar

#Mostrando os resultados
print("\n" + "=" * 50)
print(f"Valor em Reais: R$ {reais:.2f}")
print(f"Cotação do Dólar: US$1.00 = R$ {cotacao_dolar:.2f}")
print(f"Valor em Dólares: R$ {dolares:.2f}")
print("=" * 50)