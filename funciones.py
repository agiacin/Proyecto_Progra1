def registrarLibro(titulo,autor,fecha):
    print('*** RegistrandoLibro ***')
    try:
        contenido=open('libros.txt','a')
        registro= titulo + ';' + autor + ';' + str(fecha)
       # print(registro,file=contenido)
        contenido.write(registro + '\n')
        contenido.close()
        
    except Exception as e:
#         FileNotFoundError
        print('Ha ocurrido la excepcion:',type(e),'\n',e)


def mostrarLibros(ruta):
    try:
        contenido=open(ruta,'r')
        
        registro = contenido.read()
        #obtenemos una lista con los renglones
        libros = registro.split("\n")
        
        diccResultado={}
        #Recorremos y mostramos cada línea
        for libro in libros:
            if (libro != ''): #por el ultimo renglon que es una linea vacia por el salto de linea
                titulo, autor ,fecha = libro.split(";")
               
                diccResultado[titulo] = {'Autor': autor,
                                           'Fecha':int(fecha)}
                
        print('El listtado de libros es: \n',diccResultado)       
        contenido.close()
        
    except Exception as e:
        print('Ha ocurrido la excepcion:',type(e),'\n',e)
        
  
