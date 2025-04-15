from operator import index


def exercicio1():
    nome=input("Digite seu nome completo:\n")
    pnome=""
    for letra in nome:
        if letra == " ":
            break
        else:
            pnome+=letra
    print(f"Bem-vindo(a) ao Python,{pnome}")
def exercicio2():
    nota1=int(input("Digite a nota do primeiro bimestre da disciplina:\n"))
    nota2=int(input("Digite a nota do segundo bimestre da disciplina:\n"))
    print(f"Média parcial = {(nota1*2+nota2*3)//5}")
def exercicio3():
    import math
    print("Digite a base e a altura do retângulo:")
    base=int(input())
    altura=int(input())
    print(f"Área = {base*altura} - Perímetro = {(base*2)+(altura*2)} - Diagonal = {math.sqrt(base**2+altura**2)}")
def exercercio4():
    frase=input("Digite uma frase:\n")
    index=0
    palavra=""
# exercicio1()
#exercicio2()