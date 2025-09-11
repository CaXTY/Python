#Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = (celsius * 9 / 5) + 32

print(f"{celsius}°C equivalem a {fahrenheit:.1f}°F")

#Funcionamento
# foi usado Float() para garantir que números decimais sejam aceitos
#O .1f formata o resultado com 1 casa decimal