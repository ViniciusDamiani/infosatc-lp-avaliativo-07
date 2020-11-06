#Função normal
def quadrado (x):
    return x **2

print(quadrado(6))

#Função Lambda
(lambda x: x**2) (6)

#Atribuindo a uma variavel
funcLambda = (lambda x: x**2)
print(funcLambda(4))

#Erro pois nome é String e chamei um número (Inteiro)
#nome='Vinicius'
#nome(5)

#COMO USAR A FUNÇÃO LAMBDA
#Função lambda dentro da variavel
f=lambda a, b: a+b
print(f(2,8))

#Função lambda fora da variavel
(lambda a,b: a+b)(2,8)

#
f=lambda a,b=8: a+b
print(f(2))

(lambda: 'Ola')()

#Exemplo01
alunos=["Aluno_20","Aluno_100","Aluno_201","Aluno_10","Aluno_30","Aluno_01"]#Ordenar pelo número do aluno
x=sorted(alunos)
print(x)
y=sorted(alunos, key=lambda x: int(x[6:]))
print(y)
print('Aluno_100'[6:])

#Exemplo02
funcoes=[lambda x: x**2, lambda x: x**3, lambda x: x**4,]
for f in funcoes:
    print(f(5))

#exemplo de cima sem função lambda
def f1(x):
    return x**2

def f2(x):
    return x**3

def f3(x):
    return x**4

funcoes=[f1, f2, f3]
for f in funcoes:
    print(f(5))

#Exemplo03
nomesA= filter(lambda x: 'a' in x, ['Vinicius', 'Pedra'])
z=list(nomesA)
print(z)

#exemplo acima sem lambda
def temA(x):
    return 'a' in x
nomesA = filter(temA, ['Vinicius', 'Pedra'])
t=list(nomesA)
print(t)





 
