"""
1 - Faça um Programa que verifique se uma letra digitada é uma vogal ou consoante.

O programa deverá seguir as seguintes regras:

- Solicitar ao usuário que insira uma letra.
- Verificar se o caractere inserido é uma letra do alfabeto.
- Caso o usuário tenha inserido um caractere válido (ou seja, uma letra do alfabeto), o programa deverá identificar e informar se essa letra é uma vogal ou uma consoante.
- Caso o usuário insira um valor inválido (como números, símbolos ou mais de um caractere), o programa deverá exibir uma mensagem de erro, informando que a entrada é inválida e pedindo para que ele insira apenas uma letra.
"""
vogais = ("a", "e", "i", "o", "u")

def ler_caracter():
    #Função onde o programa irá capturar o caracter do usuário
    print()
    caracter = input("Insira uma letra para verificar se é consoante ou vogal: ")
    return caracter

def verificar_letra(caracter):
    #Função que checará se o caracter inserido pelo usuário é uma letra
    if(caracter.isalpha() and len(caracter) == 1):
        return 1
    else:
        return 0

def exibir_erro(teste, caracter):
    #Função que irá exibir o erro caso o caracter inserido não seja uma letra
    if(teste == 0):
        print()
        print(f"O caracter '{caracter}' não é uma letra! Insira uma letra!")
    else:
        print()
        print(f"O caracter '{caracter}' é uma letra!")
        
def tipo_letra(caracter):
    letra = caracter.lower()
    if letra in vogais:
        print()
        print(f"'{caracter}' é uma vogal")
    else:
        print()
        print(f"'{caracter}' é uma consoante")
    

def main():
    #Função que integragrá todas as funções anexas
    teste = 0
    while (teste == 0):
        caracter = ler_caracter()
        teste = verificar_letra(caracter)
        exibir_erro(teste, caracter)
    tipo_letra(caracter)


main()