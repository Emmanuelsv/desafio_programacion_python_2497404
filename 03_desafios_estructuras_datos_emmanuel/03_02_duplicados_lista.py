

def duplicados_lista(lista):
 
  n = len(lista)
  duplicados = []

  for i in range(n):
    for j in range(n-i-1):
      if lista[i] == lista[j+i+1] and lista[i] not in duplicados:
        duplicados.append(lista[i])

  return duplicados

print(duplicados_lista(["ana","paco","paco","emilio","javier","ana"]))
print(duplicados_lista([1,2,2,3,4,1,1]))