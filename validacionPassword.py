import time
#Validación de contraseña

print('- Hola!, tu PASSWORD que usas en el mundo digital es seguro...?')
time.sleep(2)
print('- Vamos a probarlo!!!')
 

while True:
    password=input('\nIngrese una contraseña: ')

    contador_minuscula=0
    contador_mayuscula=0
    contador_carac_especiales=0
    contador_digitos=0
    hay_espacio=False     

    if len(password)<8:
        print(chr(27)+"[0;31m",'\nPeligro! ',chr(27)+"[0m")        
        print(chr(27)+"[5;31m",' ->',chr(27)+"[0m",'Recuerda usar las reglas para crear una contraseña... [a-z][A-Z][0-9][#$%&/_!?]')
        print(chr(27)+"[5;31m",' ->',chr(27)+"[0m",'El password debe ser de 8 caracteres minimo') 

    else:        
        for i in password:
            if i.isspace():
                hay_espacio=True
                break
            elif i.islower():
                contador_minuscula+=1
            elif i.isupper():
                contador_mayuscula+=1
            elif i.isalnum()==False:
                contador_carac_especiales+=1 
            else:
                contador_digitos+=1

        if hay_espacio:
            print(chr(27)+"[5;36m",'\n  ->',chr(27)+"[0m",'No se aceptan espacios en blanco')
        
        elif contador_minuscula >= len(password) or contador_mayuscula >= len(password) or contador_digitos >= len(password) or contador_carac_especiales >= len(password):
            print(chr(27)+"[1;33m",'\nCuidado! ',chr(27)+"[0m")        
            print(chr(27)+"[5;33m",' ->',chr(27)+"[0m",'Malas prácticas de creación de PASSWORD')
            print(chr(27)+"[5;33m",' ->',chr(27)+"[0m",'Recuerda usar las reglas para crear una contraseña... [a-z][A-Z][0-9][#$%&/_!?]')
        
        else:
            if contador_minuscula>=1 and contador_mayuscula>=1 and contador_digitos>=1 and contador_carac_especiales>=1:

                if len(password)==8:
                    print(chr(27)+"[1;32m",'\n  -> Password válido',chr(27)+"[0m")
                    print('  -> Cumple con las reglas para crear un Password')
                    print('  -> De preferencia que sean más de',chr(27)+"[1;32m",'8',chr(27)+"[0m",'caracteres\n')
                else:
                    print(chr(27)+"[5;32m",'\n -> Excelente!',chr(27)+"[0m")
                    print(chr(27)+"[1;32m",'-> Password valido',chr(27)+"[0m")

                break
            else:
                print(chr(27)+"[1;36m"+'\nRecuerda:',chr(27)+"[1;33m")         
                print('\ta) 8 caracteres como mínimo')
                print('\tb) Letras minúsculas')
                print('\tc) Letras mayúsculas')
                print('\td) Números [0-9]')
                print('\te) Caracteres especiales')
                print(chr(27)+"[0m") # Regresar al color de texto por defecto
        
                
        
