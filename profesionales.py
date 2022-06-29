from datetime import datetime
import json
import yaml
from dateutil.relativedelta import relativedelta

nombre_archivo = 'profesionales.json'

def leer_prof():
    objeto_archivo = open(nombre_archivo, 'rt', encoding='utf-8')
    contenido = objeto_archivo.read()
    res = json.loads(contenido)
    objeto_archivo.close()
    return res

def agregar_profesional(profesionales=[]):
    
    dni = int(input("Ingrese DNI del médico: "))
    nombre = input("Ingrese nombre del médico: ")
    apellido = input("Ingrese apellido del médico: ")
    nacimiento = input("Ingrese fecha de nacimiento del médico en formato DD/MM/AAA: ")
    nacionalidad = input("Ingrese nacionalidad del médico: ")
    profesionales.append(
        {
            "dni" : dni,
            "nombre" : nombre,
            "apellido" : apellido,
            "fecha_nacimiento" : nacimiento,
            "nacionalidad" : nacionalidad,
        }
    )
    print("")
    print("✅🩺 Se ha registrado el siguiente médico:")
    print("")
    print(nombre, apellido)
    print("DNI:", dni)
    print("Fecha de nacimiento en formato DD/MM/AAA:",nacimiento)
    print("Nacionalidad:",nacionalidad)
    fechaa = datetime.strptime(nacimiento, "%d/%m/%Y")
    edad = relativedelta(datetime.now(), fechaa)
    print(f"Edad: {edad.years} años")
    with open('profesionales.json', 'w') as f:
        json.dump(profesionales, f, indent=4)

def listar_prof(profesionales):
    print("👩👨🩺 La lista de médicos es la siguiente:")
    print("")
    print(yaml.dump(profesionales, sort_keys=False, default_flow_style=False))    