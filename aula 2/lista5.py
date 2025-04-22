def qst1():
    def maior(x, y):
        return x if x > y else y

    
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    print("O maior número é:", maior(a, b))
def qst2():
    def maior(x, y, z):
        return max(x, y, z)


    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    c = float(input("Digite o terceiro número: "))
    print("O maior número é:", maior(a, b, c))
def qst3():
    def iniciais(nome):
    partes = nome.strip().split()
        return ''.join([p[0].upper() for p in partes])


    nome_completo = input("Digite seu nome completo: ")
    print("Iniciais:", iniciais(nome_completo))
def qst4():
    def aprovado(nota1, nota2):
        media = (nota1 + nota2) / 2
        return media >= 60


    nota1 = float(input("Digite a nota do primeiro bimestre: "))
    nota2 = float(input("Digite a nota do segundo bimestre: "))
    if aprovado(nota1, nota2):
        print("Aluno aprovado!")
    else:
        print("Aluno em prova final.")
def qst5():
    def formatar_nome(nome):
        return nome.title()

    nome = input("Digite seu nome: ")
    print("Nome formatado:", formatar_nome(nome))



