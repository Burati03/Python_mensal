def verificar_par_impar():
    valor = input("Digite um número: ")

    # Verifica se o valor é um número inteiro
    try:
        numero = int(valor)

        # Verifica se o número é par ou ímpar
        if numero % 2 == 0:
            return True  # Número par
        else:
            return False  # Número ímpar
    except ValueError:
        return "Valor inválido. Por favor, insira um número inteiro."

# Chama a função
resultado = verificar_par_impar()
print(resultado)
