#faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

#Lê o preço do produto
preco_original = float(input('Digite o valor do produto: R$'))

#Calcula o desconto de 5%
desconto = preco_original * 0.05
preco_com_desconto = preco_original - desconto

#Exibe os resultados
print(f"\nPreço original: {preco_original:.2f}")
print(f"Desconto (5%): {desconto:.2f}")
print(f"Preço com desconto: {preco_com_desconto:.2f}")


