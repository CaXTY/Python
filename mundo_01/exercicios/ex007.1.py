# Programa com validação básica das notas
try:
    nota1 = float(input("Digite a primeira nota (0-10): "))
    nota2 = float(input("Digite a segunda nota (0-10): "))

    # Verificando se as notas estão no intervalo válido
    if 0 <= nota1 <= 10 and 0 <= nota2 <= 10:
        media = (nota1 + nota2) / 2
        print(f"\nMédia: {media:.1f}")

        # Verificando se o aluno foi aprovado (considerando média 7)
        if media >= 7:
            print("Situação: Aprovado! ✅")
        else:
            print("Situação: Reprovado ❌")
    else:
        print("Erro: As notas devem estar entre 0 e 10!")

except ValueError:
    print("Erro: Digite apenas números!")