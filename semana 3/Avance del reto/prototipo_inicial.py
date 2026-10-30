# SISTEMA DE REGISTRO DE PACIENTES CANINOS EN PETCO
import pdb

opcion = ""
contador = 0

while opcion != "2":

    print("\n========== PETCO ==========")
    print("1. Registrar paciente")
    print("2. Salir")

    opcion = input("Selecciona una opcion: ")

    if opcion == "1":

        # Capturar datos del paciente
        print("\n--- DATOS DEL PACIENTE ---")
        nombre_perro = input("Nombre del perro: ")
        nombre_dueno = input("Nombre del dueño: ")
        edad = int(input("Edad del perro: "))
        motivo = input("Motivo de la consulta: ")

        print("\n--- SERVICIOS DISPONIBLES ---")
        print("1. Baño - $180")
        print("2. Corte de uñas - $80")
        print("3. Limpieza de oidos - $100")
        print("4. Consulta veterinaria - $250")
        print("5. Vacunacion - $300")
        print("6. Revision de piel - $200")

        opcion_servicio = input("Selecciona el servicio: ")

        if opcion_servicio == "1":
            servicio = "Baño"
            precio = 180

        elif opcion_servicio == "2":
            servicio = "Corte de uñas"
            precio = 80

        elif opcion_servicio == "3":
            servicio = "Limpieza de oidos"
            precio = 100

        elif opcion_servicio == "4":
            servicio = "Consulta veterinaria"
            precio = 250

        elif opcion_servicio == "5":
            servicio = "Vacunacion"
            precio = 300

        elif opcion_servicio == "6":
            servicio = "Revision de piel"
            precio = 200

        else:
            servicio = ""
            precio = 0

        if nombre_perro != "" and nombre_dueno != "" and edad > 0 and servicio != "":

            contador = contador + 1

            # Imprimir comprobante completo
            print("\n==========================================")
            print("          COMPROBANTE DE PETCO")
            print("==========================================")

            print("Nombre del perro:", nombre_perro)
            print("Nombre del dueño:", nombre_dueno)
            print("Edad del perro:", edad, "años")
            print("Motivo de consulta:", motivo)
            print("Servicio seleccionado:", servicio)
            print("Total a pagar: $", format(precio, ".2f"))

            print("==========================================")
            print("       REGISTRO REALIZADO CORRECTAMENTE")
            print("==========================================")

            # Depuracion
            pdb.set_trace()

        else:
            print("Datos incorrectos. Intenta nuevamente.")

    elif opcion == "2":
        print("Gracias por utilizar el sistema de Petco, a seguir moviendo la colita")
        print("Total de pacientes registrados:", contador)

    else:
        print("Opcion incorrecta.")