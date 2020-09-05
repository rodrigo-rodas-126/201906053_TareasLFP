import re

def automata(cadena):
    estado = 0
    contador = -1
    contador1 = -1
    con = 0
    rango = cadena.__len__() 
    #print(rango)
    
    for i in range(rango):
        #print(estado)

        if cadena[i]=='_':
            con += 1
            if con>1:
                estado = 1
            elif con == 1:
                estado = 3
            else:
                estado = 0

        elif re.match('[a-z]', cadena[i]):
            contador1 += 1
            if contador1 == 0:
                if estado==1:
                    estado = 2

                elif estado==2:
                    estado=0

            elif estado==3 or estado==4:
                estado = 4

            else:
                estado = 0

        elif re.match('[0-9]', cadena[i]):
            contador += 1
            if contador == 0:
                if estado == 4 or estado == 2:
                    estado = 5
            else:
                estado = 0
             
    #print(estado)
    if estado==5:
        print('Cadena valida')
    else:
        print('Cadena invalida')
        
        

entrada="__servidor1"
entrada1="3servidor"
entrada2="_servidoresdeminecraft1"

automata(entrada)
automata(entrada1)
#automata(entrada2)


    
