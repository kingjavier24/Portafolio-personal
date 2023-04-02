n1 = input("Ingrese un numero")
n2 = input("Ingrese un numero")

n1 = int(n1)
n2 = int(n2)

suma = n1 + n2
resta = n1-n2
multiplicacion = n1*n2
division = n1/n2

mensaje = f"""
para los numero {n1} y {n2}
el resultado de la suma {suma}
el resultado de la resta {resta}
el resultado de la multiplicacion {multiplicacion}
el resultado de la division {division}"""

print(mensaje)
