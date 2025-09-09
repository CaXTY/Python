#DESAFIO_04 > Um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ela.
print ('===Desafio 03===')
#Lê algo do teclado
valor = input('Digite algo: ')

#Exibe o tipo primitivo
print(f'\n 🔍 Analisando o valor: {valor}')
print(f'Tipo primitivo: {type(valor)}')

#Informações Adicionais
print(f'É numérico? {valor.isnumeric()}')
print(f'É alfabetico? {valor.isalpha()}')
print(f'É alfanumerico? {valor.isalnum()}')
print(f'Está em maiuscula? {valor.isupper()}')
print(f'Está em minuscula? {valor.islower()}')
print(f'Está capitalizada? {valor.isupper()}')
print(f'Só tem espaços? {valor.isspace()}')

#Tentiva de conversão automática
try:
    inteiro = int(valor)
    print(f"Pode ser convertido para inteiro: {inteiro}")
except:
    print("Não pode ser convertido para inteiro.")

try:
    decimal = float(valor)
    print(f"Pode ser convertido para float: {decimal}")
except:
    print("Não pode ser convertido para float.")

if valor.lower() in ['true', 'false']:
    print(f"Pode ser interpretado como booleano: {bool(valor.lower() == 'true')}")

#Contagem de Caracteres
print(f"Número de caracteres: {len(valor)}")



