#faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta área de 2m2

print("CALCULADORA DE TINTA PARA PAREDES")

#Lê as dimensões de parede
largura = float(input('\nDigite a largura da parede (metros): '))
altura = float(input('Digite a altura da parede (metros): '))

#Calcula a area
area = largura * altura

#Calcula a quantidade de tinta (cada litro pinta 2m²)
quantidade_tinta = area / 2

#Mostra os resultados
print(f'\n→ Área a ser pintada: {area:.2f} m²')
print(f'→ Tinta necessária: {quantidade_tinta:.2f} litros')

#Recomendações práticas
print("\n💡 RECOMENDAÇÕES: ")
print(f"Área total: {area:.2f} m² ")
print(f" - Compre {quantidade_tinta:.1f} litros de tinta")

