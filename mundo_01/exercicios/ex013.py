#faça um algoritmo que leia o salário e mostre seu novo salário, com 15% de aumento.

#Entrada do salário atual
salario_atual = float(input("Digite o salário atual: R$ "))

#Cálculo do aumento (15%)
aumento = salario_atual * 0.15

#Calculo do novo salário
novo_salario = salario_atual + aumento

#Exibição dos resultados
print("\n" + "="*40)
print(f"Salário atual: R$ {salario_atual:.2f}")
print(f"Aumento: R$ {aumento:.2f}")
print(f"Novo salário: R$ {novo_salario:.2f}")
print("="*40)


#Como funciona:

#O programa solicita o salário atual
#Calcula o valor do aumento (15% do salário atual)
#Soma o aumento ao salário original
#Exibe os resultados formatados com 2 casas decimais