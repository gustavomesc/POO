def qst1():
    import math

    A, B, C = input().split()

    A = float(A)
    B = float(B)
    C = float(C)

    delta = B**2 - 4 * A * C

    if A == 0 or delta < 0:
        print("Impossivel calcular")
    else:
        raiz1 = (-B + math.sqrt(delta)) / (2 * A)
        raiz2 = (-B - math.sqrt(delta)) / (2 * A)
        print(f"R1 = {raiz1:.5f}")
        print(f"R2 = {raiz2:.5f}")
def qst2():
    A, B = input().split()

    A = int(A)
    B = int(B)

    if A % B == 0 or B % A == 0:
        print("Sao Multiplos")
    else:
        print("Nao sao Multiplos")
def qst3():
    palavra1 = input()
    palavra2 = input()
    palavra3 = input()

    if palavra1 == "vertebrado":
        if palavra2 == "mamifero":
            if palavra3 == "onivoro":
                print("homem")
            elif palavra3 == "herbivoro":
                print("vaca")
        elif palavra2 == "ave":
            if palavra3 == "carnivoro":
                print("aguia")
            elif palavra3 == "onivoro":
                print("pomba")
    elif palavra1 == "invertebrado":
        if palavra2 == "inseto":
            if palavra3 == "hematofago":
                print("pulga")
            elif palavra3 == "herbivoro":
                print("lagarta")
        elif palavra2 == "anelideo":
            if palavra3 == "hematofago":
                print("sanguessuga")
            elif palavra3 == "onivoro":
                print("minhoca")
def qst4():
    DDD = int(input())

    if DDD == 11:
        print("Sao Paulo")
    elif DDD == 19:
        print("Campinas")
    elif DDD == 21:
        print("Rio de Janeiro")
    elif DDD == 27:
        print("Vitoria")
    elif DDD == 31:
        print("Belo Horizonte")
    elif DDD == 61:
        print("Brasilia")
    elif DDD == 71:
        print("Salvador")
    elif DDD == 32:
        print("Juiz de Fora")
    else:
        print("DDD nao cadastrado")
def qst5():
    X, Y = input().split()

    X = int(X)
    Y = int(Y)

    if 0 <= X <= 432 and 0 <= Y <= 468:
        print("dentro")
    else:
        print("fora")
def qst6():
    A1 = int(input())
    A2 = int(input())
    A3 = int(input())

    tempo_1 = A2 * 2 + A3 * 4
    tempo_2 = A1 * 2 + A3 * 2
    tempo_3 = A1 * 4 + A2 * 2

    melhor_tempo = min(tempo_1, tempo_2, tempo_3)

    print(melhor_tempo)
def qst7():
    for i in range(2, 101, 2):
        print(i)
def qst8():
    maior = -1
    posicao = -1

    for i in range(100):
        numero = int(input())
        if numero > maior:
            maior = numero
            posicao = i + 1

    print(maior)
    print(posicao)
def qst9():
    N = int(input())  # Número de casos de teste

    total_cobaias = 0
    total_coelhos = 0
    total_ratos = 0
    total_sapos = 0

    for _ in range(N):
        quantidade, tipo = input().split()
        quantidade = int(quantidade)
        
        total_cobaias += quantidade
        
        if tipo == 'C':
            total_coelhos += quantidade
        elif tipo == 'R':
            total_ratos += quantidade
        elif tipo == 'S':
            total_sapos += quantidade

    print(f"Total: {total_cobaias} cobaias")
    print(f"Total de coelhos: {total_coelhos}")
    print(f"Total de ratos: {total_ratos}")
    print(f"Total de sapos: {total_sapos}")

    print(f"Percentual de coelhos: {100 * total_coelhos / total_cobaias:.2f} %")
    print(f"Percentual de ratos: {100 * total_ratos / total_cobaias:.2f} %")
    print(f"Percentual de sapos: {100 * total_sapos / total_cobaias:.2f} %")
def qst10():
    while True:
    senha = int(input())
    if senha == 2002:
        print("Acesso Permitido")
        break
    else:
        print("Senha Invalida")
def qst11():
    N = int(input())  # Número de casos de teste

    for _ in range(N):
        x, y = input().split()  # Leitura dos dois números como strings
        x = int(x)  # Convertendo o primeiro número para inteiro
        y = int(y)  # Convertendo o segundo número para inteiro
        
        if y == 0:
            print("divisao impossivel")
        else:
            resultado = x / y  # Realiza a divisão
            print(f"{resultado:.1f}")  # Imprime o resultado com um dígito após o ponto decimal
def qst12():
    N = int(input())
    fib = [0, 1]
    for i in range(2, N):
        fib.append(fib[i-1] + fib[i-2])
    print(*fib[:N])







