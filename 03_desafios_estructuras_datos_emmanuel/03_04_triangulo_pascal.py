
def triangulo_pascal(fila):
  t_0 = 0
  t_1 = 1
  triangulo = []
  rows = []
  n = fila
   
  for i in range(n):
    for j in range(i+1):
      k =list(range(i+1))


      if j ==min(k) or j == max(k):
        rows.append(t_1)

      if j !=min(k) and j !=max(k):
        t = 0
        t = triangulo[i-1][j-1] + triangulo[i-1][j]
        rows.append(t)

    triangulo.append(rows)
    rows = []
  return triangulo

print(triangulo_pascal(2))


print(triangulo_pascal(3))

print(triangulo_pascal(4))

print(triangulo_pascal(8))

    
    


    

       
      
       
    


