import random

def generarDatos ():
    datos = []
    for _ in range(5000):
        dato={}
        id = random.randint(1,10000) 
        referencia = random.choice(["ACH01","ACH22","ACH43"])
        marca = random.choice(["Sony","Kalley","LG"])
        capacidad = random.randint(100,2000)
        ciudad = random.choice(["Medellin","Bogota","Manizales","Cali","Bucaramanga"])
        responsable = random.choice(["Juan Ernesto Gonzalez Montoya","Maria Garcia Restrepo","Ana Rogriguez Lopez","Carlos Martinez Hernandez","Lorena Gomez Perez"])

        dato=[id,referencia, marca,capacidad,ciudad,responsable]
        datos.append(dato)
    
    return datos

print(generarDatos())