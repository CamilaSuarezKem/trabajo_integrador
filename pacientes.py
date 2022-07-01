from ast import Num
import json
from datetime import datetime
import yaml
from dateutil.relativedelta import relativedelta

nombre_archivo = 'datos_pacientes.json'

def leer_paciente():
    obj_archivo = open(nombre_archivo, 'rt', encoding='utf-8')
    str_contenido = obj_archivo.read()
    res = json.loads(str_contenido)
    obj_archivo.close()
    return res

def agregar_paciente(pacientes=[]):
    # esta fx agrega pacientes pidiendo que el usuario ingrese DNI, Nombre, Apellido, Nacimiento, Nacionalidad, enfermeddad, médico y una observación
    if len(pacientes) == 0:
        Numero_Paciente = 1
    else: Numero_Paciente = 1 + pacientes[len(pacientes)-1]["Numero_Paciente"]
    DNI = int(input("Ingrese DNI del paciente: "))
    Nombre = input("Ingrese nombre del paciente: ")
    Apellido = input("Ingrese apellido del paciente: ")
    Nacimiento = input("Ingrese la fecha de nacimiento en formato DD/MM/AA: ")
    Nacionalidad = input("Ingrese nacionalidad del paciente: ")
    print("A continuación ingrese los datos de su historia clínica: ")
    Fecha = datetime.today().strftime('%d/%m/%Y')
    Enfermedad = input("Ingrese la enfermedad/afección que padece: ")
    Medico = input("Ingrese el médico que lo atenderá: ")
    Observacion = input("Ingrese alguna observación: ")

    pacientes.append(
        {
            "Numero_Paciente" : Numero_Paciente,
            "DNI": DNI,
            "Nombre": Nombre,
            "Apellido": Apellido,
            "Nacimiento": Nacimiento,
            "Nacionalidad": Nacionalidad,
            "historia_clinica": [
                {
                    "Fecha": Fecha,
                    "Enfermedad": Enfermedad,
                    "Medico": Medico,
                    "Observacion": Observacion
                }
            ]
        }
    )
    print("")
    print("Se ha registrado el siguiente paciente:")
    print("")
    print(Nombre, Apellido, "✅") 
    print("DNI:", DNI)
    print("Fecha de nacimiento:",Nacimiento)
    print("Nacionalidad:",Nacionalidad)
    fechaa = datetime.strptime(Nacimiento, "%d/%m/%Y")
    edad = relativedelta(datetime.now(), fechaa)
    print("Edad:", f"{edad.years} años")
    print("")
    with open('datos_pacientes.json', 'w') as file:
        json.dump(pacientes, file)

def agregar_historia_clinica(lista, paciente):
    print("")
    print("Ingrese una nueva historia clínica para el paciente:")
    Fecha = datetime.today().strftime('%d/%m/%Y')
    Enfermedad = input("Ingrese la enfermedad/afección que padece: ")
    Medico = input("Ingrese el médico que lo atenderá: ")
    Observacion = input("Ingrese alguna observación: ")
    historia = { "Fecha" : Fecha, "Enfermedad" : Enfermedad, "Medico" : Medico, "observacion" : Observacion}
    paciente["historia_clinica"].append(historia)
    print("")
    print("La nueva historia clínica de",paciente["Nombre"],paciente["Apellido"],"se ha guardado exitosamente ✅")
    print("")
    guardar_listaPacientes(lista)
    return

def buscar_paciente(lista):
    # esta funcion busca un paciente a partir de distinas opciones. Es recursiva si la busqueda es nula. ver de meter la seleccion de pacientes dentro de un bucle while para que no tengamos errores cuando el input es > len pacientes.
    # Input: lista de pacientes
    # output: 1 paciente | None
    print("Desea buscar un paciente mediante: ")
    print("")
    print(" 1️⃣   Su nombre/apellido.")
    print(" 2️⃣   La fecha en la que fue atendido.")
    print(" 3️⃣   Su enfermedad/afección.")
    print(" 4️⃣   El médico que lo atendió.")
    print(" 5️⃣   Su nacionalidad.")
    print(" 0️⃣   Volver para atrás.")
    print("")
    res = input("Ingrese una opción: ")
    if not res.isnumeric():
        print("Debe ingresar un NÚMERO, no una letra 😕, por favor ingrese una opción correcta.")
        print("")
        input("Presione ENTER para continuar... ")
        print("")
        return buscar_paciente(lista)
    res = int(res)
    if res == 1:
        pacientes = filtrar_nombre(lista)
    elif res == 2:
        pacientes = filtrar_por_fecha(lista)
    elif res == 3:
        pacientes = filtrar_enfermedad(lista)
    elif res == 4:
        pacientes = filtrar_medico(lista)
    elif res == 5:
        pacientes = filtrar_nacionalidad(lista)
    elif res == 0:# salida del menu
        print("")
        return 
    else:
        print("La opción ingresada no es correcta 😕, por favor, intente nuevamente.")

    if len(pacientes) > 1:
        print(yaml.dump(pacientes, sort_keys=False, default_flow_style=False))
        print("")
        n = int(input("Elija el número de paciente que necesita buscar: "))
        paciente = lista[(n-1)]
        print("")
        print("¿Quiere editar al paciente ",paciente["Nombre"],  paciente["Apellido"],"?")
        print("Ingrese 1 si su respuesta es SI o ingrese 2 si su respuesta es NO y quiere editar a otro paciente: ")
        res = input("Respuesta: ")
        if int(res) == 1:    
            print("")
        elif int(res) == 2:
            buscar_paciente(lista)
    elif len(pacientes) == 1:
        paciente = pacientes[0]
        print("")
        print('Se ha seleccionado a ', paciente['Nombre'])
        edad_paciente(paciente)
    else:
        print("")
        print('No hemos encontrado ningún a paciente con el dato ingresado 😕. Por favor intente nuevamente.')
        print("")
        input("Presione ENTER para continuar...")
        print("")
        paciente = buscar_paciente(lista)
    return paciente

def editar_paciente(lista, paciente):
    # Input lista de pacientes, paciente (1)
    print("")
    print("¿Qué datos quieres editar?")
    print("1️⃣  DNI")
    print("2️⃣  Apellido")
    print("3️⃣  Nombre")
    print("4️⃣  Fecha de Nacimiento")
    print("5️⃣  Nacionalidad")
    print("")
    op = int(input("Elija una opción: "))
    if op == 1:
        DNI = int(input("Ingrese el DNI correspondiente: "))
        paciente["DNI"] = DNI
    elif op == 2:
        Apellido = input("Ingrese el apellido: ")
        paciente["Apellido"] = Apellido
    elif op == 3:
        Nombre = input("Ingrese el nombre: ")
        paciente["Nombre"] = Nombre
    elif op == 4:
        # certifico que sea una Fecha
        while True:
            try:
                Fecha = input("Ingresa una fecha en el formato DD/MM/AAA: ")
                datetime.strptime(Fecha, '%d/%m/%Y')
                paciente["Nacimiento"] = Fecha
                return
            except ValueError:
                print("La Fecha ingresada es inválida 😕. Por favor ingrese la Fecha correspondiente")
                print("")
                input("Presione ENTER para volver a intentarlo...")
                print("")
    elif op == 5:
        Nacionalidad = input("Ingrese la nacionalidad del paciente: ")
        paciente["Nacionalidad"] = Nacionalidad
    else: print("El valor ingresado no está en nuestras opciones 😕, por favor ingrese un número válido.")
    print("")
    print("✅ Se editó correctamente a: ")
    print("")
    print(paciente["Nombre"], paciente["Apellido"])
    print("DNI: ",paciente["DNI"])
    print("Nacimiento: ",paciente["Nacimiento"])
    print("Nacionalidad: ",paciente["DNI"])
    print("Enfermedad/afección: ", paciente["historia_clinica"][0]["Enfermedad"])
    print("Médico que lo/a atendió: ",paciente["historia_clinica"][0]["Medico"])
    print("Observación: ",paciente["historia_clinica"][0]["Observacion"])
    print("Fecha: ",paciente["historia_clinica"][0]["Fecha"])
    print("")
    guardar_listaPacientes(lista)
    return

def eliminar_paciente(lista, paciente):
    print("")
    res = myFilter(lista, "DNI", paciente["DNI"])
    if res != None:
        lista.pop(res[1])
        print("")
        print("El/la paciente", res[0]["Nombre"], res[0]
              ["Apellido"], "se ha eliminado correctamente ✅")
    else: print("Debe ingresar un valor válido.")
    print("")
    guardar_listaPacientes(lista)

def filtrar_nombre(lista):
    res = []
    print(" ")
    Nombre = input("Ingrese nombre o apellido que quiere buscar: ")
    for elem in lista:
        if elem["Nombre"].lower() == Nombre.lower() or elem["Apellido"].lower() == Nombre.lower(): 
            res.append(elem)
    return res

def filtrar_nacionalidad(lista):
    res = []
    print("")
    Nacionalidad = input("Ingrese la nacionalidad del paciente: ")
    for elem in lista:
        if elem["Nacionalidad"].lower() == Nacionalidad.lower():
            res.append(elem)
    return res

def filtrar_dni(lista):
    print(" ")
    DNI = int(input("Ingrese DNI que quiere buscar: "))
    res = myFilter(lista, "DNI", DNI)
    print(res)
    if res != None:
        print(res[0], "en posición", res[1])
    return res

def myFilter(lista, parametro: str, valor):
    for x in range(len(lista)):
        if lista[x][parametro] == valor:
            return (lista[x], x)

def filtrar_por_fecha(lista):
    # input la lista de pacientes
    # ouput la lista filtrada de los pacientes en cierta Fecha
    Fecha = input("Ingrese la fecha que quiere buscar: ")
    return _filtrar_HistoriasClinicas(lista, "Fecha", Fecha)

def filtrar_enfermedad(lista):
    #esta funion filtra por enfermedades de las historias clínicas de los pcientes
    # input : lista de pacientes
    # output: pacientes ta que poseen dicha enfermedad
    Enfermedad = input("Ingrese la enfermedad/afección que quiere buscar: ")
    return _filtrar_HistoriasClinicas(lista,'Enfermedad',Enfermedad)
    
def filtrar_medico(lista):
    # igual que la de arriba pero con médicos
    Medico = input("Ingrese el nombre/apellido del médico que lo atendió: ")
    return _filtrar_HistoriasClinicas(lista,'Medico',Medico)
    
def _filtrar_HistoriasClinicas(lista,key,value):
    # input una lista, una clave y un valor
    # ouput una lista filtrada de pacientes que poseen esa clave-valor
    pacientes = []
    for paciente in lista:
            historias = paciente["historia_clinica"]
            for h in historias:
                if h[key].lower() == value.lower():
                    pacientes.append(paciente)
            # if paciente == []:
            #      print("No se ha encontrado", value, "en ninguna historia clínica.")
            #      print("")
    return pacientes

def guardar_listaPacientes(lista):
    # guarda la lista de pacientes
    obj_archivo = open(nombre_archivo, 'wt', encoding='utf-8')
    str_contenido_a_guardar = json.dumps(lista, indent=4, ensure_ascii=False)
    obj_archivo.write(str_contenido_a_guardar)
    obj_archivo.close()

def edad_paciente(paciente):
    # calcula la edad de un paciente
    # input un paciente
    # devuelve la edad de un paciente
    Nacimiento = datetime.strptime(paciente["Nacimiento"], "%d/%m/%Y")
    edad = relativedelta(datetime.now(), Nacimiento)
    return print(f"{edad.years} años")