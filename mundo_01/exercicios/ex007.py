#Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

#Lendo as duas notas do aluno
nota1 = float(input('Digite sua primeira nota: '))
nota2 = float(input('Digite sua segunda nota: '))

#Calculando a média
media = (nota1 + nota2)/2

#Mostrando o resultado
print(f'\nNotas do aluno:')
print(f'Nota 1: {nota1}')
print(f'Nota 2: {nota2}')
print(f'Media: {media:.1f}')

#Funcionamento do programa
#Float(input() - converte a entrada para número decimal
#(nota1 + nota2) / 2 - fórmula da média aritmética simples
#:.1f - formata o resultado para mostrar 1 casa decimal
