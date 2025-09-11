#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.

import math

#Le o angulo em graus
angulo = float(input("Digite o ângulo em graus: "))

#Converte para radianos
radianos = math.radians(angulo)

#Calcula as funções trigonométricas
seno = math.sin(radianos)
cosseno = math.cos(radianos)
tangente = math.tan(radianos)

print(f"\nÂngulo: {angulo}°")
print(f"Seno: {seno:.3f}")
print(f"Cosseno: {cosseno:.3f}")
print(f"Tangente: {tangente:.3f}")


#Pontos importantes
#1 - Conversão necessária - A biblioteca MATH trabalha com radianos, então precisamos converter graus para radianos usando math.radians()
#2 - Funções utilizadas:
#math.sin() - Calcula o seno
#math.cos() - Calcula o cosseno
#math.tan() - Calcula a tangente
#O programa calcula corretamente todas as funções trigonométricas básicas para qualquer ângulo!