# 1. Escreva um programa que apresente na tela a frase: "Meu primeiro programa!!!" .

print("Meu primeiro programa!!! Olá mundo!!!")
##########################################################################################################

# 2. Escreva um programa que solicite ao usuário um número inteiro e ao final apresente na tela o número informado pelo usuário do programa.

n = int(input("Digite um número inteiro: "))
print("O número que você digitou foi:", n)
##########################################################################################################

# 3. Escreva um programa que solicite ao usuário um número inteiro e ao final apresente na tela o número informado da seguinte forma: "Foi informado o valor: X".

# Apresente na tela dos dois números informados da seguinte forma:
# "VocÊ informou o "

n = int(input("Digite um número inteiro: "))


print("Foi informado o valor:",n)
print(f'foi informado o valor: {n}')
##########################################################################################################

# 4. Escreva um programa que solicite ao usuário dois números inteiros e ao final apresente na tela os dois números informados da seguinte forma: "Você informou os números X e Y".

x = int(input("Digite o primeiro número inteiro: "))
y = int(input("Digite o segundo número inteiro: "))

print("Você informou os números", x, "e", y)
##########################################################################################################

# 5. Escreva um programa que solicite ao usuário um número real e ao final apresente na tela o número informado formatado com duas casas decimais da seguinte forma: "Você informou o número X.YY".



numeroReal = float(input("Digite um número real: "))
print("Você informou o número", numeroReal, "formatado com duas casas decimais:", format(numeroReal, ".2f"))
##########################################################################################################

# 6. Escreva um programa que solicite ao usuário a temperatura em graus Celsius e ao final apresente a temperatura correspondente em graus Farenheit. F = Celsius * 1.8 + 32

celsius = float(input("Digite a temperatura em graus Celsius: "))
fahrenheit = celsius * 1.8 + 32

print("A temperatura em graus Farenheit é", fahrenheit)
##########################################################################################################

# 7. Escreva um programa que solicite ao usuário um número inteiro e um número real e ao final apresente na tela os dois números informados formatando com duas casas decimais somente o número real da seguinte forma: "Você informou os números N e X.YY".

numero_inteiro = int(input("Digite um número inteiro: "))
numero_real = float(input("Digite um número real: "))

print("Você informou os números", numero_inteiro, "e", numero_real)
##########################################################################################################

# 8. Escreva um programa que solicite ao usuário a primeira letra de seu nome e ao final apresente na tela a letra informada pelo usuário da seguinte forma: "Você digitou w".

nome = input("Digite a primeira letra do seu nome: ")
if len(nome) > 1:
  print("Você digitou mais que uma letera")
else:
  print("Você digitou", nome)
##########################################################################################################

# 9. Escreva um programa que solicite ao usuário o nome de sua cor preferida e ao final apresente na tela a cor informada pelo usuário da seguinte forma: "Voce gosta da cor AAA".

cor = input("Qual é a sua cor preferida? ")

print("Você gosta da cor", cor)
##########################################################################################################

# 10. Escreva um programa que solicite ao usuário o nome de uma verdura e uma fruta de sua preferência e ao final apresente na tela as informações digitadas pelo usuário da seguinte forma: "Você gosta de AAAAAAA e BBBBBBB".

verdura = input("Qual é a sua verdura preferida? ")
fruta = input("Qual é a sua fruta preferida? ")

print("Você gosta de", verdura, "e", fruta)
##########################################################################################################

# 11. Elabore um algoritmo que solicite ao usuário um número real e ao final imprima na tela o numero informado e na linha de baixo o dobro deste número da seguinte forma: Numero -> X Dobro deste numero -> Y.

numero = float(input("Digite um número real: "))
dobro = numero * 2

print("Numero ->", numero)
print("Dobro deste numero ->", dobro)
##########################################################################################################

# 12. Reescrever o programa anterior apresentando o quadrado e o cubo do número informado.

numero = float(input("Digite um número real: "))
dobro = numero * 2
quadrado = numero ** 2
cubo = numero ** 3

print("Numero ->", numero)
print("Dobro deste numero ->", dobro)
print("Quadrado deste numero ->", quadrado)
print("Cubo deste numero ->", cubo)
##########################################################################################################

# 13. Escreva um programa que solicite ao usuário dois números inteiros e ao final apresente na tela a soma dos dois números informados da seguinte forma: "Os números N e X somados correspondem a Y".

n = int(input("Digite o primeiro número: "))
x = int(input("Digite o segundo número: "))

soma = n + x

print("Os números {} e {} somados correspondem a {}".format(n, x, soma))
##########################################################################################################

# 14. Escreva um programa que solicite ao usuário dois números reais e ao final apresente na tela o produto dos dois números informados da seguinte forma: "O produto dos números N e X corresponde a Y".

n = float(input("Digite o primeiro número: "))
x = float(input("Digite o segundo número: "))

produto = n * x

print("O produto dos números {} e {} corresponde a {}".format(n, x, produto))
##########################################################################################################

# 15. Refazer o programa 14 realizando as quatro operações aritméticas básicas.

n = float(input("Digite o primeiro número: "))
x = float(input("Digite o segundo número: "))

soma = n + x
subtracao = n - x
multiplicacao = n * x
divisao = n / x

print("A soma dos números {} e {} corresponde a {}".format(n, x, soma))
print("A subtração dos números {} e {} corresponde a {}".format(n, x, subtracao))
print("A multiplicação dos números {} e {} corresponde a {}".format(n, x, multiplicacao))
print("A divisão dos números {} e {} corresponde a {}".format(n, x, divisao))
##########################################################################################################

# 16. Escreva um programa que solicite o valor fixo do salário de um vendedor, o total vendidono mês e o percentual de comissão do vendedor. Ao final apresentar o salário bruto.

salario_fixo = float(input("Digite o valor do salário fixo do vendedor: "))
total_vendido = float(input("Digite o total vendido pelo vendedor: "))
percentual_comissao = float(input("Digite o percentual de comissão do vendedor: "))

comissao = total_vendido * percentual_comissao

salario_bruto = salario_fixo + comissao

print("O salário bruto do vendedor é de R$ {}".format(salario_bruto))


# "Não existe amor em SP"
# "True" significa verdadeiro em inglês
# Trata-se de um verdadeiro ou falso
# Variável boleana é a forma de identificar de algo é verdadeiro ou falso (radialmente)
print("amor" in "Não existe amor em SP")
print(type("amor" in "Não existe amor em SP"))

##########################################################################################################

# Igual: ==
# Diferente: !
# Menor: <
# Maior: >
# Menor ou Igual: <=
# Maior ou Iguaç: >=

# IF [condição]:
#    [instruções]
##########################################################################
# ELIF [condição:]
#      [instruções]
##########################################################################
# ELSE:
#    [instruções]
# (identação é o espaço epós o IF e ELSE)
##########################################################################