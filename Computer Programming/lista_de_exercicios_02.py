#########################################################################################################

# 1. Elabore um programa que solicite ao usuário um número real e ao final imprima na tela se onúmero informado é maior que 10 (dez)
n = float(input("Digite um número real: "))
if n > 10:
    print("O número informado é maior que 10")
else:
    print("O número informado é menor ou igual a 10")
#########################################################################################################

# 2. Escreva um programa que solicite ao usuário um número real e ao final imprima na tela se o número informado é maior ou igual a dez ou menor que 10 (dez)
n = float(input("Digite um número real: "))
if n >= 10:
    print("O número informado é maior ou igual a 10")
else:
    print("O número informado é menor que 10")
#########################################################################################################

# 3. Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela se o número informado é maior que dez, se é menor que dez, ou se é igual a dez
n = float(input("Digite um número real: "))
if n > 10:
    print("O número informado é maior que 10")
elif n < 10:
    print("O número informado é menor que 10")
else:
    print("O número informado é igual a 10")
#########################################################################################################

# 4. Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela se o número informado é positivo, negativo ou nulo (zero)
n = float(input("Digite um número real: "))
if n > 0:
    print("O número informado é positivo")
elif n < 0:
    print("O número informado é negativo")
else:
    print("O número informado é nulo (zero)")
#########################################################################################################

# 5. Elabore um algoritmo que leia um número inteiro e imprima uma das mensagens: é múltiplo de 3, ou, não é múltiplo de 3
n = int(input("Digite um número inteiro: "))
if n % 3 == 0:
    print("O número informado é múltiplo de 3")
else:
    print("O número informado não é múltiplo de 3")
#########################################################################################################

# 6. Refazer o exercício anterior, solicitando antes o múltiplo a ser testado
m = int(input("Digite o múltiplo a ser testado: "))
n = int(input("Digite um número inteiro: "))
if n % m == 0:
    print("O número informado é múltiplo de {}.".format(m))
else:
    print("O número informado não é múltiplo de {}.".format(m))
#########################################################################################################

# 7. Desenvolva um algoritmo que classifique um número inteiro fornecido pelo usuário como par ou ímpar
n = int(input("Digite um número inteiro: "))
if n % 2 == 0:
    print("O número informado é par.")
else:
    print("O número informado é ímpar.")
#########################################################################################################

# 8. Elabore um algoritmo que leia um número, e se ele for maior do que 20, imprimir a metade desse número, caso contrário, imprimir o dobro do número
n = int(input("Digite um número: "))
if n > 20:
    print("A metade do número informado é: {}".format(n / 2))
else:
    print("O dobro do número informado é: {}".format(n * 2))
#########################################################################################################

# 9. Elabore um algoritmo que leia dois números inteiros e realize a adição; caso o resultado seja maior que 10, imprima o quadrado do resultado, caso contrário, imprima a metade dele
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))
soma = n1 + n2
if soma > 10:
    print("O quadrado do resultado é: {}".format(soma ** 2))
else:
    print("A metade do resultado é: {}".format(soma / 2))
#########################################################################################################

# 10. O sistema de avaliação de determinada disciplina é composto por três provas. A primeira prova tem peso 2, a segunda tem peso 3 e a terceira tem peso 5. Considerando que a média para aprovação é 6.0, faça um algoritmo para calcular a média final de um aluno desta disciplina e dizer se o aluno foi aprovado ou não
# Entrada das notas das provas
nota1 = float(input("Digite a nota da primeira prova: "))
nota2 = float(input("Digite a nota da segunda prova: "))
nota3 = float(input("Digite a nota da terceira prova: "))

# Cálculo da média final
media = (nota1 * 2 + nota2 * 3 + nota3 * 5) / 10

# Verificação da aprovação
if media >= 6.0:
    print("Aprovado!")
else:
    print("Reprovado!")
#########################################################################################################

# 11. Elabore um algoritmo que leia o nome e o peso de duas pessoas e imprima o nome da pessoa mais pesada
# Entrada dos dados
nome1 = input("Digite o nome da primeira pessoa: ")
peso1 = float(input("Digite o peso da primeira pessoa (em kg): "))
nome2 = input("Digite o nome da segunda pessoa: ")
peso2 = float(input("Digite o peso da segunda pessoa (em kg): "))

# Verificação da pessoa mais pesada
if peso1 > peso2:
    pessoa_mais_pesada = nome1
else:
    pessoa_mais_pesada = nome2

# Saída do resultado
print("A pessoa mais pesada é {}.".format(pessoa_mais_pesada))
#########################################################################################################

# 12. Elabore um algoritmo que indique se um número digitado está compreendido entre 20 e 90, ou não
# Entrada do número
numero = int(input("Digite um número: "))

# Verificação do intervalo
if numero >= 20 and numero <= 90:
    print("O número {} está compreendido entre 20 e 90.".format(numero))
else:
    print("O número {} não está compreendido entre 20 e 90.".format(numero))
#########################################################################################################

# 13. Elabore um algoritmo que leia dois números e imprima qual é maior, qual é menor, ou se são iguais
# Entrada dos números
numero1 = int(input("Digite o primeiro número: "))
numero2 = int(input("Digite o segundo número: "))

# Verificação do maior número
if numero1 > numero2:
    maior = numero1
    menor = numero2
else:
    maior = numero2
    menor = numero1

# Saída do resultado
print("O maior número é {} e o menor número é {}.".format(maior, menor))
#########################################################################################################

# 14. Escreva um programa em linguagem C que solicite ao usuário a média para aprovação em um curso e em seguida solicite ao usuário o nome, sexo e as 03 notas do aluno e ao final imprima a frase: "O aluno XXXXX foi aprovado com media YY" considerando o gênero do(a) aluno(a) e se foi aprovado(a) ou reprovado(a)
#include <stdio.h>
#include <stdlib.h>

int (main) {
    // Declaração das variáveis
    float media_aprovacao;
    char nome[50];
    char sexo;
    float nota1, nota2, nota3;

    // Entrada dos dados
    printf("Digite a média para aprovação: ");
    scanf(" %f ", &media_aprovacao);
    printf("Digite o nome do aluno: ");
    scanf(" %s ", nome);
    printf("Digite o sexo do aluno (M/F): ");
    scanf(" %c ", &sexo);
    printf("Digite a primeira nota: ");
    scanf(" %f ", &nota1);
    printf("Digite a segunda nota: ");
    scanf(" %f ", &nota2);
    printf("Digite a terceira nota: ");
    scanf(" %f ", &nota3);

    // Cálculo da média final
    float media_final = (nota1 + nota2 + nota3) / 3;

    // Verificação da aprovação
    if (media_final >= media_aprovacao) {
        printf("O aluno %s foi aprovado com média %.2f", nome, media_final);
    } else {
        printf("O aluno %s foi reprovado com média %.2f", nome, media_final);
    }

    return 0;
}