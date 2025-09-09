#script que leia o dia, o mês e o ano de nascimento e mostre uma mensagem com a data formatada.
print ('===Desafio 02b===')

#Entra do usuário
nome = input('Digite seu nome: ')
dia = input("Digite o dia do seu nascimento: ")
mes = input("Digite o mês do seu nascimento: ")
ano = input("Digite o ano do seu nascimento: ")

#Exibe a data formatada
print(f"Olá, {nome}! Você nasceu no dia {dia} do mês de {mes} no ano {ano}. Correto?")
