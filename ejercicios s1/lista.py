operadores = [
    {"nombre": "Jose", "sueldo_por_hora": 15, "horas_trabajadas": 8},
    {"nombre": "Ivan", "sueldo_por_hora": 20, "horas_trabajadas": 7},
    {"nombre": "Antonio", "sueldo_por_hora": 18, "horas_trabajadas": 9},
    {"nombre": "Ricardo", "sueldo_por_hora": 22, "horas_trabajadas": 6},
    {"nombre": "Daniel", "sueldo_por_hora": 17, "horas_trabajadas": 8},
    {"nombre": "Miguel", "sueldo_por_hora": 19, "horas_trabajadas": 7}
]

# Imprimir el nombre y el sueldo a pagar de cada operador
for operador in operadores:
    sueldo_a_pagar = operador["sueldo_por_hora"] * operador["horas_trabajadas"]
    print(f"El sueldo a pagar para {operador['nombre']} es de ${sueldo_a_pagar}")
