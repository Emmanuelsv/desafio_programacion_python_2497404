
def aplanar_lista(lista):
  n = len(lista)

  for i in lista:
    if type(i) is list:
      temporal = i
      lista.remove(i)
      for j in temporal:
        lista.append(j)
  return lista

print(aplanar_lista([1,2,[1,2,3]]))
print(aplanar_lista([2,3,4,[3,2]]))
print(aplanar_lista([2,3,4,[[2]]]))



