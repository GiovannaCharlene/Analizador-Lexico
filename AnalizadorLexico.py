#Analizador Lexico del AFD que acepta la cadena vacía o un numero par de x's y/o un numero par de y's

# Tabla de transiciones
# Estado    x     y     FDC
# S0       S2    S1     Aceptar
# S1       S3    S0     Rechazar
# S2       S0    S3     Rechazar
# S3       S1    S2     Rechazar

#0 para rechazar y 1 para aceptar
Tabla=[[2, 1, 1], [3, 0, 0], [0, 3, 0], [1, 2, 0]]

Estado=0
Aceptado=0
indice=0


def Analizador(simbolo, EstadoAc,Tabla):
   #Se envia al estado siguiente
    EstadoF=Tabla[EstadoAc][simbolo]
    #Se acepta o se rechaza
    FC=Tabla[EstadoF][2]
    if FC==1:
        FCD='Acepta'
    else:
        FCD='Rechaza'
    return EstadoF,FCD

cadena = input("Ingrese cadena de entrada para el alfabeto x,y: ")
tamCad= len(cadena)

if tamCad != 0:
    while indice<=tamCad-1:
        if cadena[indice]=='x' or cadena[indice]=='X':
            [Estado, FCD]=Analizador(0, Estado, Tabla)
        elif cadena[indice]=='y' or cadena[indice]=='Y':
            [Estado, FCD]=Analizador(1, Estado, Tabla)
        else:
            print('Formato de cadena erroneo')
            break
        indice += 1
else:
    FCD='Acepta'

if len(FCD) != 0:
    print(FCD)


