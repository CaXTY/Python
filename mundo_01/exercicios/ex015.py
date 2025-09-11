# Escreva um programa em python que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.

dias = int(input("Quantos dias de aluguel? "))
km = float(input("Quantos Km rodados? "))

custo_dias = dias * 60
custo_km = km * 0.15
total = custo_dias + custo_km

print("="*40)
print(f"\nCusto por {dias} dias: R$ {custo_dias:.2f}.")
print(f"Custo por {km} km: R$ {custo_km:.2f}.")
print(f"Total a pagar: {total:.2f}.")
print("="*40)

