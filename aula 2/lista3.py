def qst1():
    valor1 = int(input())
    valor2 = int(input())
    PROD = valor1 * valor2
    print(f"PROD = {PROD}")
def qst2():
    n1 = float(input())
    n1 = float(input())
    media = (n1 * 3.5 + n2 * 7.5) / 11
    print(f"MEDIA = {media:.5f}")
def qst3():
    R = float(input())
    pi = 3.14159
    volume = (4.0 / 3) * pi * R**3
    print(f"VOLUME = {volume:.3f}")
def sqt4():
    import math

    x1, y1 = input().split()
    x2, y2 = input().split()

    x1 = float(x1)
    y1 = float(y1)
    x2 = float(x2)
    y2 = float(y2)

    distancia = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

    print(f"{distancia:.4f}")
def qst5():
    T1, T2, T3, T4 = input().split()

    T1 = int(T1)
    T2 = int(T2)
    T3 = int(T3)
    T4 = int(T4)

    max_aparelhos = (T1 - 1) + (T2 - 1) + (T3 - 1) + T4

    print(max_aparelhos)
def qst6():
    C, N = input().split()

    C = int(C)
    N = int(N)

    ponto_termino = C % N

    print(ponto_termino)


    