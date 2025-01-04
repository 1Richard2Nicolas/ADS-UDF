#Exercício 1: Apresente em tela (output) toda a base de dados. Pontuação: 0,5 pontos
#Espera-se que você exiba todo o conteúdo da base de dados na saída.

import pandas as pd

Cidade = ["Brasília", "Nova Iorque", "São Paulo", "São Luiz", "São Francisco", "Chicago", "Zurich", "Barcelona", "Roma"]
País = ["Brasil", "Estados Unidos", "Brasil", "Brasil", "Estados Unidos", "Estados Unidos", "Suíça", "Espanha", "Itália"]
Região = ["Distrito Federal", "Nova Iorque", "São Paulo", "Maranhão", "Califórnia", "Illinois", "Zurich", "Catalunha", "Latium"]
População = ["2.817.381", "18.123.398", "11.451.995", "1.458.836", "808.437", "2.665.000", "402.762", "1.620.000", "2.873.000"]
Clima = ["Tropical", "Temperado", "Temperado Úmido", "Tropical Úmido", "Temperado Mediterrânico", "Continental Úmido", "Temperado", "Mediterrânico", "Mediterrânico"]
Fundação = ["1960", "1624", "1574", "1612", "1776", "1733", "15 a.C.", "15 a.C.", "750 a.C."]

estatísticas = {
    "Cidade": Cidade,
    "País": País,
    "Região": Região,
    "População": População,
    "Clima": Clima,
    "Fundação": Fundação
}

board = pd.DataFrame(estatísticas)

print(board)
print()
display(board)

##########################################################################################################

#Exercício 2: Apresente o tamanho do seu dataframe (quantas colunas x linhas). Pontuação: 0,5 pontos
#Você deve retornar o número de colunas e o número de linhas do dataframe.

import pandas as pd

Cidade = ["Brasília", "Nova Iorque", "São Paulo", "São Luiz", "São Francisco", "Chicago", "Zurich", "Barcelona", "Roma"]
País = ["Brasil", "Estados Unidos", "Brasil", "Brasil", "Estados Unidos", "Estados Unidos", "Suíça", "Espanha", "Itália"]
Região = ["Distrito Federal", "Nova Iorque", "São Paulo", "Maranhão", "Califórnia", "Illinois", "Zurich", "Catalunha", "Latium"]
População = ["2.817.381", "18.123.398", "11.451.995", "1.458.836", "808.437", "2.665.000", "402.762", "1.620.000", "2.873.000"]
Clima = ["Tropical", "Temperado", "Temperado Úmido", "Tropical Úmido", "Temperado Mediterrânico", "Continental Úmido", "Temperado", "Mediterrânico", "Mediterrânico"]
Fundação = ["1960", "1624", "1574", "1612", "1776", "1733", "15 a.C.", "15 a.C.", "750 a.C."]

estatísticas = {
    "Cidade": Cidade,
    "País": País,
    "Região": Região,
    "População": População,
    "Clima": Clima,
    "Fundação": Fundação
}

board = pd.DataFrame(estatísticas)

print(board.shape)
print()
