
def ordenamiento_burbuja(lista):
  n = len(lista)
  s=0
  i=0
  while s < n-1:

    if lista[i] > lista[i+1]:
    
      lista[i], lista[i+1] = lista[i+1], lista[i]

    i += 1

    if i == n-1:
      s += 1
      i = 0

  return lista

print(ordenamiento_burbuja([3,8,4,1,2]))
print(ordenamiento_burbuja([1,5,3,0,2,8]))

