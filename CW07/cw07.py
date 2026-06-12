#INPUT
rol = input("Ingrese el rol sin guión ni dígito verificador (ej. 201012341): ")

#PROCESS
rol_invertido = ""
for i in range(len(rol) - 1, -1, -1):
    rol_invertido = rol_invertido + rol[i]


multiplicadores = [2, 3, 4, 5, 6, 7]
suma_total = 0
indice = 0

for digito_str in rol_invertido:
    digito_num = int(digito_str)
    multiplicador_actual = multiplicadores[indice]
    
    suma_total = suma_total + (digito_num * multiplicador_actual)
    
    
    indice = indice + 1
    if indice == len(multiplicadores):
        indice = 0

modulo = suma_total % 11

resultado_resta = 11 - modulo

if resultado_resta == 11:
    digito_verificador = "0"
elif resultado_resta == 10:
    digito_verificador = "K"
else:
    digito_verificador = str(resultado_resta)

#OUTPUT
print("El dígito verificador calculado es:", digito_verificador)
print("Rol completo:", rol + "-" + digito_verificador)
