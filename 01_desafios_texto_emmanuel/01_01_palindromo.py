def palindromo(tex):
  tex = str(tex)
  rev = tex[::-1]
  r = (tex==rev)
  return r

print(palindromo(1221))
print(palindromo("palindromo"))