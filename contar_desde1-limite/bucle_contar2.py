# coding: utf-8
salir = "false"
contar = 1
limite = input("Introduce el límite :")
while (salir == "false"):
	print contar, 
	if contar == limite:
		salir = "true"
	contar = contar + 1
