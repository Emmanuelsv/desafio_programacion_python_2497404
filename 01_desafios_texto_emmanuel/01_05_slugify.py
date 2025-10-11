#import string 

def slugify(texto):

  Alfabeto = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n",
              "ñ","o","p","q","r","s","t","u","v","w","x","y","z"]
  
  Alfabeto_mayusculas = [j.upper() for j in Alfabeto] 

  Numeros = ["0","1","2","3","4","5","6","7","8","9"]

  Alfanumericos = Alfabeto + Alfabeto_mayusculas + Numeros + [" "] 

  texto_alfanum = ""


  for i in texto:

    if i in Alfanumericos:

      texto_alfanum = texto_alfanum + i

  slug = texto_alfanum.replace(" ", "-")

  return slug

print(slugify("texto& con caracteres$# especia-les"))

print(slugify("Este es un ejemplo!!!"))

  

