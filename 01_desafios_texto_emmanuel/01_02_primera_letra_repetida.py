
def buscar_primera_repetida(t):
  r = []
  t = t.lower()
  texto = t.replace(" ","")

  n = len(texto)
  for i in range(n-1):
    for j in range(n-i-1):
      if texto[i]==texto[j+i+1]:
        r.append(texto[i])
        break
  if len(r) == 1:
   return r
  else:
    return r.append(None)
 
  
  
    
print(buscar_primera_repetida("hola"))
print(buscar_primera_repetida("hola mundo"))
print(buscar_primera_repetida("palindromo"))

