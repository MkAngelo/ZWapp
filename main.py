import random

DB = [
    {
        "Principiantes" : {    # Popotes
            "Calentamiento":[
                "Changuitos",
                "Ballenitas"
            ],
            "Ejercicios":[
                "2 vueltas Superman",
                "2 vueltas aviones",
                "2 vueltas wakanda for ever",
                "2 vueltas patada perrito cara afuera",
                "2 vueltas patada perrito cara adentro",
                "2 vueltas tortugas (tablas)",
                "2 vueltas patada crol",
                "2 vueltas de brazada de perrito",
                "2 vueltas de crolsito",
                "2 vueltas de dorsito",
                "Sumercion con aros chiquitos",
            ],
            "Material": [
                "Tablas",
                "Pelotas normales",
                "Pelotas chiquitas",
                "Pull boys",
                "Popotes",
                "Popotitos",
                "Juguetes",
                "Tablitas",
            ]
        }
    },
    {    #Intermedios
        "Intermedios" : {
            "Calentamiento":[
                "Perrito cara afuera",
                "Perrito cara adentro",
                "Ballenitas",
                "Ballenita loca",
                "vueltas de Crol"
            ],
            "Ejercicios":[
                "Patada de Crol normal",
                "Patada de Dorso normal",
                "Patada lateral (ida y regreso diferente)",
                "Brazada de Crol",
                "Brazada de Dorso",
                "Brazada de Crol con un solo brazo (ida y regreso diferente)",
                "Crol correctivo, tocando hombros",
                "Crol correctivo, tocando gluteo",
                "Crol correctivo, dedos no salen del agua",
                "Crol correctivo, cutch up",
                "Dorso correctivo, cutch up",
                "Dorso correctivo, pelota chica en el aire",
                "Dorso correctivo, pulgar, meñique",
                "Dorso con pelota en el abdomen",
                "Dorso con tabla en el aire",
                "Patada de crol con resistencia",
                "Patada de crol y con pelota movimiento de basketball",
                "Patada de crol con pelota sumergida",
                "Patada de crol con tabla sumergida",
                "Flecha con patada de crol",
                "Flecha con patada de dorso",
                "Flecha con delfineo",
                "Flecha con abnea hasta las banderas",
                "Sumercion con aro",
                "Crol con popotito, cambio en la posicion de la muñeca",
                "Trabajo de viraje con popote",
                "Practica de viraje Crol",
            ],
            "Material": [
                "Tablas",
                "Pelotas normales",
                "Pelotas chiquitas",
                "Pull boys",
                "Popotes",
                "Popotitos",
                "Tablitas",
            ]
        }
    },
    {    #Avanzados
        "Avanzados" : {
            "Calentamiento":[
                "300m de Crol",
                "300m libres (Cualquier estilo)"
            ],
            "Ejercicios":[
                "200m Patada de Crol normal",
                "200m Patada de Dorso normal",
                "200m Patada lateral (ida y regreso diferente)",
                "200m Brazada de Crol con pull",
                "200m Brazada de Crol con tabla",
                "200m Brazada de Crol con pies cruzados",
                "200m Brazada de Dorso con pull",
                "200m Brazada de Dorso con tabla",
                "200m Brazada de Dorso con pies cruzados",
                "100m Brazada de Crol con un solo brazo (ida y regreso diferente)",
                "100m Crol correctivo, tocando hombros",
                "100m Crol correctivo, tocando gluteo",
                "100m Crol correctivo, dedos no salen del agua",
                "100m Crol correctivo, cutch up",
                "100m Dorso correctivo, cutch up",
                "100m Dorso correctivo, pelota chica en el aire",
                "100m Dorso correctivo, pulgar, meñique",
                "150m Dorso con pelota en el abdomen",
                "150m Dorso con tabla en el aire",
                "200m patada de crol con resistencia",
                "150m Patada de crol y con pelota movimiento de basketball",
                "100m Patada de crol con pelota sumergida",
                "100m Patada de crol con tabla sumergida",
                "200m Flecha con patada de crol",
                "200m Flecha con patada de dorso",
                "200m Flecha con delfineo",
                "Crol con popotito, cambio en la posicion de la muñeca",
                "Trabajo de viraje con popote",
                "Practica de viraje Crol",
                "Escalera combinado ascendente: 25-c, 50-d, 75-p, 100-m",
                "Escalera combinado desendente: 100-m, 75-p, 50-d, 25-c",
                "Escalera crol ascendente: 25, 50, 75, 100",
                "Escalera crol desendente: 100, 75, 50, 25",
                "Escalera dorso ascendente: 25, 50, 75, 100",
                "Escalera dorso desendente: 100, 75, 50, 25",
                "Escalera pecho ascendente: 25, 50, 75, 100",
                "Escalera pecho desendente: 100, 75, 50, 25",
                "Escalera mariposa ascendente: 25, 50, 75, 100",
                "Escalera mariposa desendente: 100, 75, 50, 25",
                "Patada de delfin boca abajo",
                "Patada de delfin boca arriba",
                "Patada de pecho",
                "Brazada de pecho",
                "Mariposa correctivo, cutch up",
                "Brazada de pecho y patada de crol",
                "Brazada de crol y patada de pecho",
                "Brazada de mariposa y patada de crol",
                "Brazada de crol y delfineo",
                "Pecho correctivo, cutch up",
                "Flecha 10 m y el resto a velocidad",
                "8 x 25m (aumentando, rapido-lento, sin respirar, maxima)",
                "4 x 50m (paletas y pull, paletas, pull, sin equipo)",
                "4 x 75m combinado, retrocediendo el ultimo 25 de estilo",
                "Salidas con flecha larga y crol",
                "4 x 25m, crol a maxima hasta la mitad despues suave",
                "4 x 50m, ida: agarrando un pie y patada de delfin boca abajo, regreso a maxima de crol",
                "4 x 50m, ida: agarrando un pie y patada de delfin boca arriba, regreso a maxima de dorso",
                "4 x 50m, alguien agarra los pies mientras el otro brasea, pasan 10 segundos lo sueltan hace viraje y sale de crol, continua el siguiente",
                "8 x 25m de gigantes, uno bracea y otro patea",
                "4 x 25m patada de crol con popote entre 2",
                "4 x 25m a maxima velocidad de crol"
            ],
            "Material": [
                "Tablas",
                "Tablitas",
                "Pelotas normales",
                "Pelotas chiquitas",
                "Pull boys",
                "Popotes",
                "Popotitos",
                "Paletas"
            ]
        }   
    },
]


def seleccionador(opciones, n):
    temp = []
    i = 0
    while i < n:
        ejercicio = random.choice(opciones)
        if ejercicio not in temp:
            temp.append(ejercicio)
            i += 1
    return temp

def mostrar(rutina):
    for i in range(3):
        if i == 0:
            print("CALENTAMIENTO:")
        elif i == 1:
            print("EJERCICIOS:")
        else:
            print("MATERIAL OPCIONAL:")
        for elem in rutina[i]:
            print(f"\t+ {elem}")
    


if __name__ == "__main__":
    print("B.A.B.A.S.\t\t\t\tv0.1")
    print("RUTINAS DISPONIBLES")
    print("  1.Principiantes\n  2.Intermedios\n  3.Avanzados\nSelecciona la rutina que quires generar: ", end="")
    op = int(input())
    print("-"*40)
    if op in [1,2,3]:
        rutina = []

        if op == 1:
            banco_ejercicios = DB[0].get("Principiantes")
            # Calentamiento
            rutina.append(seleccionador(list(banco_ejercicios.values())[0], 1))
            # Ejercicios
            rutina.append(seleccionador(list(banco_ejercicios.values())[1], 4))
            # Material
            rutina.append(seleccionador(list(banco_ejercicios.values())[2], 1))
        elif op == 2:
            banco_ejercicios = DB[1].get("Intermedios")
            # Calentamiento
            rutina.append(seleccionador(list(banco_ejercicios.values())[0], 2))
            # Ejercicios
            rutina.append(seleccionador(list(banco_ejercicios.values())[1], 6))
            # Material
            rutina.append(seleccionador(list(banco_ejercicios.values())[2], 1))
        elif op == 3:
            banco_ejercicios = DB[2].get("Avanzados")
            # Calentamiento
            rutina.append(seleccionador(list(banco_ejercicios.values())[0], 2))
            # Ejercicios
            rutina.append(seleccionador(list(banco_ejercicios.values())[1], 8))
            # Material
            rutina.append(seleccionador(list(banco_ejercicios.values())[2], 1))
        mostrar(rutina)
        print("-"*40)
    else:
        print("Ocurrio un error, intenta despues :)")

