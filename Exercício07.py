#Faça um programa que leia duas notas de um aluno numa turma de 10 alunos. Para cada aluno,
#calcular a média ponderadas das notas, sabendo que a nota1 tem peso = 4 e a nota2 tem peso = 6 .
#Imprimir a média do aluno e o conceito final, conforme tabela abaixo:
#Intervalo Conceito
#0,0 a 4,9 D
#5,0 a 6,9 C
#7,0 a 8,9 B
#9,0 a 10,0 A
#Fazer 2 funções:
#Função lambda para calcular a média ponderada das notas. Argumentos de entrada duas notas, Saída a
#média.
#Função local que irá receber como argumento de entrada a média das notas e retornar o conceito
#conforme a tabela acima.
RED   = "\033[1;31m"  
RESET = "\033[0;0m"
def linhas():
    print("-"*35)

#Professora, posso estar errado, mas somente com duas notas se encontrarmos a média sua nota não passará de 5. Implementei mais duas
nota1=float(input("Insira a nota com peso 4 do aluno: "))
while nota1>4:
    nota1=float(input(RED+"NOTA INVALIDA! "+RESET+"Insira a nota com peso 4 do aluno novamente: "))
nota2=float(input("Insira a nota com peso 6 do aluno: "))
while nota2>6:
    nota2=float(input(RED+"NOTA INVALIDA! "+RESET+"Insira a nota com peso 6 do aluno novamente: "))
nota3=float(input("Insira a nota do trabalho complementar com peso 5 do aluno: "))
while nota3>5:
    nota3=float(input(RED+"NOTA INVALIDA! "+RESET+"Insira a nota com peso 5 do aluno novamente: "))
nota4=float(input("Insira a nota do simulado com peso 5 do aluno: "))
while nota4>5:
    nota4=float(input(RED+"NOTA INVALIDA! "+RESET+"Insira a nota com peso 5 do aluno novamente: "))

verificaMedia=(lambda w,x,y,z: (w+x+y+z)/2)
media=verificaMedia(nota1,nota2,nota3,nota4)

def verificaConceito(nota):
    if (nota<4.9):
        return "D"
    elif (nota>5 and nota<6.9):
        return "C"
    elif (nota>7 and nota<8.9):
         return "B"
    else: (nota>9 and nota<10)
    return "A"

conceito=verificaConceito(media)
linhas()
print("Suas notas nesse bimestre foram essas abaixo:\nNota com peso 4: ",nota1,"\nNota com peso 6: ",nota2,"\nNota com peso 5: ",nota3,"\nNota com peso 5: ",nota4)
linhas()
print("A média do aluno é "+str(media)+" e seu conceito é ",conceito,"!")