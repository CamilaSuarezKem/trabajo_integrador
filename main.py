from pacientes import*
from profesionales import*

def main():
    # aca inicia el programa
    print("")
    print("             🧬 Instituto Médico las Luciérnagas 🧬              ")
    op = mostrar_menu_opciones() 
    if op.isnumeric():
        if int(op) == 1 or int(op)==2:
            lista = leer_paciente()
            if int(op) == 1:
                agregar_paciente(lista)
            elif int(op) == 2:
                paciente = buscar_paciente(lista)
                if paciente != None:
                    menu_paciente(paciente,lista)
        elif int(op) == 3 or int(op) == 4:
            profesionales = leer_prof()
            if int(op) == 3:
                agregar_profesional(profesionales)
            elif int(op) == 4:
                listar_prof(profesionales)
        else: 
            print("El valor ingresado no está entre las opciones 😕. Por favor, ingrese un número válido.")
            print("")

    else: 
        print("El valor ingresado NO es un número 😕, por favor ingrese una de las opciones.")
        print("")
    
def mostrar_menu_opciones():
    print(" ")
    print("SECCIÓN PACIENTES:")
    print(" 1️⃣  - Si desea registrar un nuevo paciente.")
    print(" 2️⃣  - Si desea buscar un paciente.")
    print(" ")
    print("SECCIÓN MEDICOS:")
    print(" 3️⃣  - Si desea registrar un nuevo médico.")
    print(" 4️⃣  - Si desea listar todos los médicos.")
    print("")
    opcion = input("Ingrese una opción: ")    
    print("")
    print("------------------------------------------------------------------------------------------------------")
    print("")
    return opcion

def menu_paciente(paciente, lista):
    # muestra el menu y luego edita, agrega una historia clínica o elimina  un paciente
    print("")
    print(" 1️⃣  - Si desea editar al paciente.")
    print(" 2️⃣  - Si desea agregar otra historia clínica al paciente.")
    print(" 3️⃣  - Si desea eliminar el paciente.")
    print("")
    op = int(input("Ingrese una opción: "))
    if op == 1:
        editar_paciente(lista, paciente)
    elif op == 2:
        agregar_historia_clinica(lista, paciente)
    elif op == 3:
        eliminar_paciente(lista, paciente)
    else:
        print("El valor ingresado es inválido😕, por favor ingrese una de las opciones.")
        print("")
        input("Presione ENTER para continuar...")
        print("")
        menu_paciente(paciente)

def menu():
    print("🧬 Si desea VOLVER al menú principal, ingrese V. Si quiere FINALIZAR, ingrese cualquier otra letra.")
    a = (input("🙏 Ingrese una opción: "))
    while a.upper() == "V":
        main()
        print("🧬 Si desea VOLVER al menú principal, ingrese V. Si quiere FINALIZAR, ingrese cualquier otra letra.")
        a = (input("🙏 Ingrese una opción: "))

main()
menu()   