# 1 - Elabore um algoritmo que imprima na tela lado a lado o texto "Hello World!" 10 vezes.
# Imprime "Hello World!" 10 vezes lado a lado
for i in range(10):
    print("Hello World!", end=" ")
#################################################################################################################

# 2 - Elabore um algoritmo que imprima na tela o texto "Hello World!" 10 vezes, um por linha.
# Imprime "Hello World!" 10 vezes, um por linha
for i in range(10):
    print("Hello World!")
#################################################################################################################

# 3 - Elabore um algoritmo que imprima todos os números inteiros de 1 até 100 inclusive.
# Imprime todos os números inteiros de 1 até 100 inclusive
for i in range(1, 101):
    print(i)
#################################################################################################################

# 4 - Elabore um algoritmo que imprima 100 vezes o texto "1- Hello World!" com o número.
# Imprime 100 vezes o texto "i- Hello World!" com o número
for i in range(1, 101):
    print(f"{i}- Hello World!")  
#################################################################################################################

# 5 - Elabore um algoritmo que imprima todos os números decrescentes de 100 até 0 inclusive.
# Imprime todos os números decrescentes de 100 até 0 inclusive
for i in range(100, -1, -1):
    print(i)
#################################################################################################################

# 6 - Elabore um algoritmo que imprima todos os números pares inteiros de 1 até 1000.
# Imprime todos os números pares inteiros de 1 até 1000
for i in range(2, 1001, 2):
    print(i)
#################################################################################################################

# 7 - Elabore um algoritmo que imprima todos os números ímpares de 1000 até 0.
# Imprime todos os números ímpares de 1000 até 0
for i in range(1000, -1, -2):
    print(i)
#################################################################################################################

# 8 - Elabore um algoritmo que imprima a soma dos 100 primeiros números inteiros positivos.
# Imprime a soma dos 100 primeiros números inteiros positivos
soma = 0
for i in range(1, 101):
    soma += i
print(soma)
#################################################################################################################

# 9 - Elabore um algoritmo que solicite ao usuário um número inteiro que indicará a quantidade de vezes que o texto "Hello World!" será impresso na tela, um em cada linha.
# Solicita ao usuário um número inteiro que indicará a quantidade de vezes que o texto "Hello World!" será impresso na tela, um em cada linha
numero = int(input("Digite um número inteiro: "))

# Imprime o texto "Hello World!" o número de vezes especificado pelo usuário
for i in range(numero):
    print("Hello World!")
#################################################################################################################

# 10 - Elabore um algoritmo que solicite ao usuário uma palavra e um número inteiro que indicará a quantidade de vezes que a palavra digitada será impressa na tela, um em cada linha.
# Solicita ao usuário uma palavra e um número inteiro que indicará a quantidade de vezes que a palavra digitada será impressa na tela, um em cada linha
palavra = input("Digite uma palavra: ")
numero = int(input("Digite um número inteiro: "))

# Imprime a palavra o número de vezes especificado pelo usuário
for i in range(numero):
    print(palavra)
#################################################################################################################

# 11 - Elabore um algoritmo que leia um número de entrada que indicará a quantidade de números a serem lidos. Em seguida, leia n números (conforme o valor informado anteriormente) e imprima a soma e a média aritmética dos números informados.
# Lê um número de entrada que indicará a quantidade de números a serem lidos
n = int(input("Digite a quantidade de números a serem lidos: "))

# Inicializa as variáveis soma e média
soma = 0
media = 0

# Lê os números informados
for i in range(n):
    numero = int(input("Digite um número: "))
    soma += numero

# Calcula a média aritmética
media = soma / n

# Imprime a soma e a média aritmética
print("Soma:", soma)
print("Média aritmética:", media)
#################################################################################################################

# 12 - Elabore um algoritmo que leia um número de entrada que indicará a quantidade de registros a serem lidos (N). Em seguida algoritmo deve solicitar o nome e idade de N pessoas e ao final apresentar o nome da pessoa mais velha.
# Lê um número de entrada que indicará a quantidade de registros a serem lidos
n = int(input("Digite a quantidade de registros a serem lidos: "))

# Inicializa as variáveis nome_mais_velho e idade_mais_velho
nome_mais_velho = ""
idade_mais_velho = 0

# Lê os nomes e idades das pessoas
for i in range(n):
    nome = input("Digite o nome da pessoa: ")
    idade = int(input("Digite a idade da pessoa: "))

    # Verifica se a pessoa atual é mais velha que a pessoa mais velha até o momento
    if idade > idade_mais_velho:
        nome_mais_velho = nome
        idade_mais_velho = idade

# Imprime o nome da pessoa mais velha
print("Nome da pessoa mais velha:", nome_mais_velho)
#################################################################################################################

# 13 - Elabore um algoritmo que leia um número de entrada que indicará a quantidade de registros a serem lidos (N). Em seguida algoritmo deve solicitar o sexo (M/F) e idade de N pessoas e ao final apresentar a média de idade de ambos os gêneros catalogados.
# Lê um número de entrada que indicará a quantidade de registros a serem lidos
n = int(input("Digite a quantidade de registros a serem lidos: "))

# Inicializa as variáveis soma_idades_masculinas, soma_idades_femininas, quantidade_masculinos e quantidade_femininas
soma_idades_masculinas = 0
soma_idades_femininas = 0
quantidade_masculinos = 0
quantidade_femininas = 0

# Lê os sexos e idades das pessoas
for i in range(n):
    sexo = input("Digite o sexo (M/F): ")
    idade = int(input("Digite a idade: "))

    if sexo == "M":
        soma_idades_masculinas += idade
        quantidade_masculinos += 1
    elif sexo == "F":
        soma_idades_femininas += idade
        quantidade_femininas += 1

# Calcula a média de idade de cada gênero
media_idade_masculina = soma_idades_masculinas / quantidade_masculinos
media_idade_feminina = soma_idades_femininas / quantidade_femininas

# Imprime as médias de idade
print("Média de idade masculina:", media_idade_masculina)
print("Média de idade feminina:", media_idade_feminina)
#################################################################################################################

# 14 - Elabore um algoritmo que solicite ao usuário 10 números reais e ao final apresente o maior e o menor deles.
# Inicializa as variáveis maior e menor com o primeiro número digitado
maior = float(input("Digite o primeiro número: "))
menor = maior

# Lê os outros 9 números
for i in range(1, 10):
    numero = float(input("Digite o próximo número: "))

    # Atualiza as variáveis maior e menor se necessário
    if numero > maior:
        maior = numero
    elif numero < menor:
        menor = numero

# Imprime o maior e o menor número
print("Maior número:", maior)
print("Menor número:", menor)
#################################################################################################################

# 15 - Elabore um algoritmo que solicite N números reais e quando o usuário informar o valor nulo 0 (zero) o programa ordene e mostre todos os números informados de forma crescente.
# Cria uma lista vazia para armazenar os números
numeros = []

# Lê os números até que o usuário digite 0
while True:
    numero = float(input("Digite um número (ou 0 para encerrar): "))
    if numero == 0:
        break
    numeros.append(numero)

# Ordena a lista de números em ordem crescente
numeros.sort()

# Imprime os números ordenados
print("Números ordenados:", numeros)
#################################################################################################################

# 16 - Escreva um programa que vá solicitando as idades dos alunos da sala até que todos sejam informados (perguntar ao usuário se deseja informar a idade do próximo aluno). Ao final apresentar a idade do mais novo, a idade do mais velho, Quantos alunos têm mais de 18 anos, quantos alunos têm até 18 anos, a média aritmética e a mediana.
# Cria uma lista vazia para armazenar as idades
idades = []

# Loop para solicitar as idades dos alunos
while True:
    resposta = input("Deseja informar a idade do próximo aluno? (S/N): ")
    if resposta.upper() == "N":
        break
    idade = int(input("Informe a idade do aluno: "))
    idades.append(idade)

# Calcula a idade do mais novo e do mais velho
idade_minima = min(idades)
idade_maxima = max(idades)

# Conta quantos alunos têm mais de 18 anos e quantos têm até 18 anos
alunos_maiores_de_18 = 0
alunos_ate_18 = 0
for idade in idades:
    if idade > 18:
        alunos_maiores_de_18 += 1
    else:
        alunos_ate_18 += 1

# Calcula a média aritmética
media_aritmetica = sum(idades) / len(idades)

# Calcula a mediana
idades.sort()
if len(idades) % 2 == 0:
    mediana = (idades[len(idades) // 2] + idades[len(idades) // 2 - 1]) / 2
else:
    mediana = idades[len(idades) // 2]

# Imprime os resultados
print("Idade do mais novo:", idade_minima)
print("Idade do mais velho:", idade_maxima)
print("Número de alunos com mais de 18 anos:", alunos_maiores_de_18)
print("Número de alunos com até 18 anos:", alunos_ate_18)
print("Média aritmética das idades:", media_aritmetica)
print("Mediana das idades:", mediana)