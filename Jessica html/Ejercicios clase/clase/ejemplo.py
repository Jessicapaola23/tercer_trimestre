from os import strerror

try:
    character_counter = line_counter = 0     #esta linea de codigo guarda y cuenta el numero de los caracteres y el numero de lineas del archivo 
    stream = open('text.txt', 'rt')          #esta linea direcciona al archivo que deseamos   
    lines = stream.readlines(20)             #
    while len(lines) != 0:                   #esta linea esta leyendo las lineas en el archivo
        for line in lines:                   #esta contando cuantas lineas tiene el archivo
            line_counter += 1                #guarda el numero de lineas contado anteriormente
            for char in line:                #cuenta el numero de caracteres en cada linea
                print(char, end='')          #imprime el numero de caracteres y con end salta a la siguiente linea 
                character_counter += 1       #
        lines = stream.readlines(10)         #no va a contar mas de 10 lineas
    stream.close()                           #termina el stream
    print("\nCaracteres en el archivo:", character_counter)   #imprime los caracteres contados
    print("Líneas en el archivo:", line_counter)              #imprime las lineas contadas
except IOError as e:                                          #si no se da ningun ciclo for o while da como salida un error
    print("Se produjo un error de E/S:", strerror(e.errno))   #

stream = open("text.txt")        #abre el archivo 
print(stream.readlines(20))      #
print(stream.readlines(20))      #
print(stream.readlines(20))      #
print(stream.readlines(20))      #
stream.close()    




#from os import strerror

#try:
#	file = open('newtext.txt', 'wt') # Un nuevo archivo (newtext.txt) es creado.
#	for i in range(10):
#		s = "línea #" + str(i+1) + "\n"
#		for char in s:
#			file.write(char)
#	file.close()
#xcept IOError as e:
#	print("Se produjo un error de E/S:", strerror(e.errno))#