#La compañía estaadounidense American MegaDesign está realizando un nuevo modelo de muebles basados en los planos del famoso Diseñador Industrial italiano Martin Vaccoto pero muchas piezas no han encajado correctamente debido a que los planos están en cms y las maquinarias americanas en pulgadas.
#----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- 
#Algoritmo:
#1-Definir el valor de 1 centímetro en pulgadas.
#2-Solicitar la medida en centímetros del plano.
#3-Realizar la conversión de centímetros a pulgadas.
#4-Mostrar el resultado en pulgadas.
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

cm_a_pulgadas = 2.54 #Valor de 1 centímetros = 1 pulgada 

plano_x = float(input("Ingrese la medida en centímetros del plano: \n-"))

conversion = plano_x / 2.54

print(f"El plano tiene una medida de {conversion} pulgadas.")