def quick_sort(lista, inicio=0, fim=None):
  if fim is None:
    fim = len(lista) - 1
  if inicio < fim:
    p = partition(lista, inicio, fim)
    quick_sort(lista, inicio, p - 1)
    quick_sort(lista, p + 1, fim)


def partition(lista, inicio, fim):
  pivo = lista[fim]
  i = inicio - 1
  for j in range(inicio, fim):
    if lista[j] > pivo:  # > para ordenar em ordem decrescente
      i += 1
      lista[j], lista[i] = lista[i], lista[j]
  indice_pivo = i + 1
  lista[indice_pivo], lista[fim] = lista[fim], lista[indice_pivo]
  return indice_pivo
