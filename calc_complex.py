# calculadora de números complexos criada na aula 5
from aula4.complexos import *

print("***** CALCULADORA DE NÚMEROS COMPLEXOS *****")

opcao = int(input("Escolha uma opção:\n" +
                  "\t1-informações\n" +
                  "\t2-cálculos\n" +
                  "Sua escolha: "))

if opcao == 1:
    print("Seja z = a + bi. Digite o valor de a e de b.")
    a = float(input("a = "))
    b = float(input("b = "))

    z = z(a, b)

    if b >= 0:
        sinal = "+"
    else:
        sinal = ""

    print("====== Informações ======")
    print(f"z = {z}\t({a}{sinal}{b}i)\n")
    print(f"Re(z) = {re(z)}\n")
    print(f"Im(z) = {im(z)}\n")
    print(f"-z = {oposto(z)}\n")
    print(f"conjugado = {conjugado(z)}\n")
    print(f"módulo = {modulo(z)}\n")
    print(f"argumento(radianos) = {rad(z)}\n")
    print(f"argumento(graus) = {grau(z)}\n")
    print(f"polar(raio, radianos) = {polar(z)}\n")
    print(f"polar(raio, graus) = {polar(z, True)}\n")
    input("Pressione ENTER para sair.")

elif opcao == 2:
    opcao = int(input("Escolha uma opção:\n" +
                      "\t1-soma\n" +
                      "\t2-subtração\n" +
                      "\t3-multiplicação\n" +
                      "\t4-divisão\n" +
                      "\t5-potência\n" +
                      "\t6-radiciação\n" +
                      "Sua escolha: "
                      ))
    
    if opcao < 5:
        print("Seja z1 = a + bi. Digite o valor de a e de b.")
        a = float(input("a = "))
        b = float(input("b = "))
        z1 = z(a, b)

        print("Seja z2 = c + di. Digite o valor de c e de d.")
        c = float(input("c = "))
        d = float(input("d = "))
        z2 = z(c, d)

        if opcao == 1:
            print(f"{z1} + {z2} = {somar(z1, z2)}")
        elif opcao == 2:
            print(f"{z1} - {z2} = {subtrair(z1, z2)}")
        elif opcao == 3:
            print(f"{z1} * {z2} = {multiplicar(z1, z2)}")
        elif opcao == 4:
            print(f"{z1} / {z2} = {dividir(z1, z2)}")

        input("Pressione ENTER para sair.")
    elif opcao == 5 or opcao == 6:
        print("Seja z = a + bi. Digite o valor de a e de b.")
        a = float(input("a = "))
        b = float(input("b = "))
        z = z(a, b)

        if opcao == 5:
            n = int(input("Digite o valor do expoente n: "))
            print(f"{z}^{n} = {potencia(z, n)}")
        elif opcao == 6:
            n = int(input("Digite o valor do índice n: "))
            print(f"{z}^1/{n} = {raiz(z, n)}")

        input("Pressione ENTER para sair.")
    else:
        print("Opção inválida")
        input("Pressione ENTER para sair.")
else:
    print("Opção inválida")
    input("Pressione ENTER para sair.")