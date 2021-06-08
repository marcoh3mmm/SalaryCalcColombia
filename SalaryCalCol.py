# Enter data and storage them into a list
dato = input()
dato = dato.split()

#Get the values for each variable, according to the entered list
salario_base = int(dato[0])
cant_horas_extra = int(dato[1])
bonificacion = int(dato[2])

#Calculate the values for each item
vlr_hora_trab_norm= salario_base / 180
vlr_hora_extra= cant_horas_extra * vlr_hora_trab_norm * 1.45
vlr_bonificacion = salario_base * 0.015

# Condition about bonification
if bonificacion == 1:
    salario_total =salario_base + vlr_hora_extra + vlr_bonificacion
else:
    salario_total =salario_base + vlr_hora_extra

# After obtain total Salary procceed with legal discounts
plan_obl_salud = salario_total * 0.055
pension= salario_total * 0.05
caja_compensacion = salario_total * 0.05
salario_pagar = salario_total - plan_obl_salud - pension - caja_compensacion

#print the outcomes
print(round(salario_pagar,1), round(salario_total,1))
print(f"{salario_pagar:.2f} {salario_total:.2f}")

        