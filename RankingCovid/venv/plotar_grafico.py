import matplotlib as mpl
import matplotlib.pyplot as plt

def plotar_grafico(nome, estados, quantidade):
  mpl.use('Agg')
  fig = plt.figure(figsize=(11,8))

  plt.bar(estados,quantidade, color="blue")
  
  plt.ticklabel_format(style='plain', axis='y')

  plt.xlabel('Estados')
  plt.ylabel(nome)


  fig.savefig(nome)
