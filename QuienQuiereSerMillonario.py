#Examen Sofía Rubie García 

# Diccionario de Usuarios-Clave
usersGame = {  
    'Sofia': 'srg123',
    'Pedro': '123',
    'Juan': '456',
    'Matias': '789',
}


#Lista de diccionarios con las pregunas,opciones y respuesta correcta...
preguntas = [
    {
        "pregunta": "¿Cuál es el río más largo del mundo?",
        "opciones": ["Amazonas", "Nilo", "Yangtsé"],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Quién interpretó a James Bond en la película 'Skyfall'?",
        "opciones": ["Pierce Brosnan", "Daniel Craig", "Sean Connery"],
        "respuesta_correcta": 2
    },
    {
        "pregunta": "¿Cuál es el elemento químico con el número atómico 79?",
        "opciones": ["Oro", "Plata", "Platino"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿En qué deporte se utiliza una puntuación perfecta de 10?",
        "opciones": ["Gimnasia artística", "Patinaje artístico", "Natación sincronizada"],
        "respuesta_correcta": 1
    },
    {
        "pregunta": "¿Quién escribió la famosa novela 'Cien años de soledad'?",
        "opciones": ["Gabriel García Márquez", "Isabel Allende", "Julio Cortázar"],
        "respuesta_correcta": 1
    }
]

def crearNuevoUsuario(users, passwd):  # Registro
    usersGame[users] = passwd
    mensaje = "Usuario creado correctamente"
    return mensaje

def validacionUsuario(users, passwd):  # Iniciar sesión
    bandera = False
    if users in usersGame:
        passwordOriginal = usersGame[users]
        if passwordOriginal == passwd:
            bandera = True
    return bandera

def jugar(): #Juego
    cont=0
    for i, pregunta in enumerate(preguntas):
        print("Pregunta", i + 1 ,":", pregunta['pregunta'])
        for j, opcion in enumerate(pregunta['opciones']):
            print(j + 1 , opcion)
    
        try:
            respuesta = int(input("Ingrese el número de su respuesta: "))
            if respuesta == pregunta['respuesta_correcta']:
                print("¡Correcto!")
                cont=cont+100
                print("Puntuación:", cont, "puntos\n")
            else:
                print("Respuesta incorrecta. Juego terminado.\n")
                return
        except ValueError:
            print("Entrada no válida. Por favor ingrese un número.")
            return
    
    print("¡Felicidades, has respondido todas las preguntas correctamente!")


#### MAIN ####
continuar = "SI"
while continuar != "NO":
    print("****Juego Quien Quiere Ser Millonario***")
    print("1. Registrarme")
    print("2. Iniciar sesión")
    print("3. Salir")
    
    op = input("Seleccione una opción: ")

    if op == "1" or op == "2":
        users = input("Digite su nombre de usuario: ")
        passwd = input("Digite la contraseña: ")

    if op == "1":  # Registro
        created = crearNuevoUsuario(users, passwd)
        print(created)
    elif op == "2":  # Inicio de sesión
        login = validacionUsuario(users, passwd)
        if login:
            print("Bienvenido")
            print("Cada pregunta respondida correctamente equivale a 100 puntos")
            while True:  
                jugar() 
                continuar = input("¿Desea empezar de nuevo (Si/No)? ").upper()
                if continuar == "NO":
                    print("Gracias por jugar...")
                    break  
        else:
            print("Usuario/Contraseña incorrectos")
    elif op == "3":  # Salir
        print("Gracias por usar nuestro juego...")
        break
    else:
        print("Opción inválida")

