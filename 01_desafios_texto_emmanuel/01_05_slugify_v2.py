
import re

def slugify_v2(texto):
  p = re.compile(r'[^\w\s]')

  p2 = re.compile(r'\s') 
  
  slug = p.sub('', texto)

  slug = p2.sub('-',slug)

  return slug

print(slugify_v2("texto& con caracteres$# especia-les"))
print(slugify_v2("Este es un ejemplo!!!"))

