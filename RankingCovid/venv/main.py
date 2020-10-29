from processar_planilha import processar
from quick_sort import quick_sort
from plotar_grafico import plotar_grafico


matriz_dados = processar('dados_relevantes.xlsx')
quantidade_estados = len(matriz_dados)
casos = []
casos_novos = []
obitos = []
# [0 - 26] = linhas , [0 - 3] = colunas
# 0 = UF, 1 = Casos, 2 = novosCasos, 3 = Obitos
# Cada linha representa os dados de um estado, cada coluna representa uma categoria de dados

for i in range(quantidade_estados):
  casos.append([matriz_dados[i][1], matriz_dados[i][0]])
  casos_novos.append([matriz_dados[i][2], matriz_dados[i][0]])
  obitos.append([matriz_dados[i][3], matriz_dados[i][0]])

quick_sort(casos)
quick_sort(casos_novos)
quick_sort(obitos)


casos_estados = [casos[i][1] for i in range(quantidade_estados)]
casos_num = [casos[i][0] for i in range(quantidade_estados)]

casosN_estados = [casos_novos[i][1] for i in range(quantidade_estados)]
casosN_num = [casos_novos[i][0] for i in range(quantidade_estados)]

obitos_estados = [obitos[i][1] for i in range(quantidade_estados)]
obitos_num = [obitos[i][0] for i in range(quantidade_estados)]

plotar_grafico('Casos', casos_estados, casos_num)
plotar_grafico('Novos Casos', casosN_estados, casosN_num)
plotar_grafico('Obitos', obitos_estados, obitos_num)
