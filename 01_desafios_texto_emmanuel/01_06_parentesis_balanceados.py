
def es_balanceado(string):
  c = 0
  
  if string[0] == ")":
    return False

  for i in string:

    if i == "(":
      c += 1

    if i == ")":
      c -= 1

  if c == 0:
    return True
  else:
    return False
  
print(es_balanceado("((()))()"))
print(es_balanceado(")(()"))
print(es_balanceado("(()"))