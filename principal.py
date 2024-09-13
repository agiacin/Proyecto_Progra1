import funciones as funcion
# Programa principal

while True:
    try:
        
        opcion = input('Ingrese una opcion \n 1-Para registrar libro \n 2 - Para mostrar los libros \n 0-Para Salir: \n')
    
        
        if opcion == "0":
           # Salir 
            break
        
        elif opcion == "1":
            
            titulo = input("Ingrese titulo del libro: ").strip()
            while True:
                if len(titulo)==0:
                    titulo = input("Ingrese titulo del libro valido: ").strip()
                    continue
                break
            
            autor = input("Ingrese autor del libro: ").strip()
            while True:
                if len(autor)==0:
                    autor = input("Ingrese autor del libro: ").strip()
                    continue
                break
            
            while True:
                try:
                    anio=int(input("Ingrese el año del libro: "))
                    break
                
                except ValueError: 
                    print('Ingrese un año valido')
                
            funcion.registrarLibro(titulo, autor, anio) 
            print('*** Se registro el libro correctamente *** \n')
            
        elif opcion == "2":
            funcion.mostrarLibros('libros.txt')
            
        else:
            print('Ingrese una opcion valida:')
    
    except Exception as e:
        print("\nHa ocurrido un error inesperado: ", e)



