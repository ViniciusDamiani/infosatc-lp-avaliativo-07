#Faça um programa utilizando expressões lambda para gerar o quadrado, o triplo de um número.

digito=int(input("Informe um número: "))
armazenaValor=[lambda x: digito**2, lambda x: digito**3]
for f in armazenaValor:
    print(f(5))