# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.

soma = 0
contador = 0
while True:
    numero = float(input("Digite seus numeros(digite -1 para sair): "))
    if numero == -1:
        break

    soma += numero
    contador += 1
    media = soma / contador
print("sua media é: ", media)