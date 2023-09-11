from os import strerror

with open("nuevotexto.txt","w") as my_file:
    my_file.write("Mi nombre es:Jessica Triviño \n")
    my_file.write("Mi edad es:18 años \n")
    my_file.write("Mi fecha de nacimiento es: 02-06-2005 \n")
    my_file.write("Mi correo es:Jpaolatv02@gmail.com \n")

with open('nuevotexto.txt', 'rt') as my_file:
    nuevotexto=my_file.read()
    print(nuevotexto)
    
def Caracteres_lineas():
    character_counter=line_counter=0
    stream=open('nuevotexto.txt','rt')
    lines=stream.readlines()
    while len(lines) !=0:
        for line in lines:
            line_counter +=1
            for char in line:
                print(char, end='')
                character_counter +=1
        line =stream.readlines()
    stream.close()
    print(f'\n\Hay {line_counter} lineas en el archivo.')
    print(f'\n\Hay {character_counter} caracteres en el archivo.')
    
    
Caracteres_lineas()