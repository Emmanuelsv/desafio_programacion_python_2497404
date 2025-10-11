
def es_anagrama(palabra_1,palabra_2):

  palabra_1_min = palabra_1.lower()

  palabra_2_min = palabra_2.lower()

  letras1 = [i for i in palabra_1_min]
  letras2 = [j for j in palabra_2_min]

  #r = []

  #for l in letras1:

   # if l in letras2:
    #  r.append(l)

  #if len(r) == len(palabra1):
  #  return True
      
  #else:
  #  return False

  respuesta = [l for l in letras1 if l in letras2]

  if respuesta == letras1:
    return True
  
  else:
    return False






       

  

print(es_anagrama("mora","ramo"))
print(es_anagrama("lama","Mala"))
print(es_anagrama("calor","coral"))
print(es_anagrama("cama","casa"))