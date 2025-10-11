
def conversion_fomato_horario(hora_12):

  if hora_12[-2:].lower() == "am":
    hora_24 = hora_12[:-3]
    if hora_12[:2] == "12":
      hora_24 = "00" + hora_12[2:-2]

    
    return hora_24

  if hora_12[-2:].lower() == "pm":
    hora_24 = hora_12[:-3]
    if hora_12[:2] != "12":
      hora_int = int(hora_12[:2])
      hora_int = hora_int + 12
      hora_str = str(hora_int)
      hora_24 = hora_str + hora_12[2:-2]
    return hora_24
  
  else:
    return "Formato incorrecto"
  

print(conversion_fomato_horario("10:34 pm"))
print(conversion_fomato_horario("03:55 am"))
print(conversion_fomato_horario("11:00 pm"))
print(conversion_fomato_horario("12:40 am"))
print(conversion_fomato_horario("12:15 pm"))