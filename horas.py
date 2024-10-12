horas_extras=[] # lista vacia

for dia in range(1,31):  #un mes de 30 dias

	while True:			#introduccion datos, añadir a lista

		horas=float(input(f"Introduce las horas extras del dia {dia}:"))

		horas_extras.append(horas)

		break



total_horas_extras=sum(horas_extras)   #calculo total horas

print("El total de horas extras es:" , total_horas_extras)  #imprime horas totales
print (horas_extras)  #Imprime lista

