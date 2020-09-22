def buscar_en_lista(numeros,numero_a_encontrar,lim_inf,lim_sup):
    
    medio = ((lim_sup+lim_inf)//2)
    if lim_sup < lim_inf:
        return False

    if  numero_a_encontrar == numeros[medio]:
        return True
    elif numero_a_encontrar > numeros[medio]:
       return buscar_en_lista(numeros,numero_a_encontrar,medio+1,lim_sup)
    else:
       return buscar_en_lista(numeros,numero_a_encontrar,lim_inf,medio-1)
        
    
if __name__=='__main__':
     numeros = [1, 3, 4, 5, 6, 9, 10, 11, 25, 27, 28, 34, 36, 49, 51]
     numero_a_encontrar=int(input('Ingresa un numero: '))
     numero=buscar_en_lista(numeros,numero_a_encontrar,0,len(numeros)-1)
     if numero == False:
        print('El número {} no está en la lista'.format(numero_a_encontrar))
     else:
        print('El número {} si está en la lista'.format(numero_a_encontrar))