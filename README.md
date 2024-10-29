#  SWIMMING APP

[!TIP]

Esta aplicación es desarrollada para poder generar rutinas de entrenamiento para deportistas o entrenadores de natación, con el fin de mejorar las habilidades fisicas que cada uno puede desarrollar.

### FUNCIONAMIENTO (0.1v):
El funcionamiento actual de la aplicación es basada en una terminal, puedes ocupar alguna basada en bash, zsh, cmd o powershell. Siempre y cuando cuentes con el lenguaje de programación Python 3.11.X

Una vez que tienes Python y ya descargaste el codigo fuente del programa, es necerario que ejecutes el siguiente comando en tu terminal o cmd (dependiendo el sistema operativo).

Linux & MacOS:
```sh
python3 main.py
```

Windows:
```sh
py main.py
```

Una vez que se ejecute esa linea de codigo, se nos mostrara el menu princilpal donde necesitaremos seleccionar una opción de acuerdo a la rutina que queremos genear.


```
B.A.B.A.S.				v0.1
RUTINAS DISPONIBLES
  1.Principiantes
  2.Intermedios
  3.Avanzados
Selecciona la rutina que quires generar: 
```

Aquí seleccionamos una de las opciones disponibles el el menú, haciendo uso de la numeración.
```
B.A.B.A.S.				v0.1
RUTINAS DISPONIBLES
  1.Principiantes
  2.Intermedios
  3.Avanzados
Selecciona la rutina que quires generar: 1
```
En el ejemplo de arriba nosotros hemos solicitado la generación de una rutina para principiantes, lo que nos arrojara la siguiente salida.
```
----------------------------------------
CALENTAMIENTO:
	+ Changuitos
EJERCICIOS:
	+ 2 vueltas tortugas (tablas)
	+ 2 vueltas patada perrito cara adentro
	+ 2 vueltas aviones
	+ 2 vueltas Superman
MATERIAL OPCIONAL:
	+ Popotes
----------------------------------------
```
Una vez generada la rutina el programa se cierra en automatico. Si se desea generar otra rutina se tendrian que repetir los pasos.

### LIMITACIONES (0.1v)
- Solo se puede generar una rutina por cada llamada a la aplicación.
- Los ejercicios incorporados aún necesitas una revisión para catalogarlos mejor.
- No existe un orden al momento de generar los ejercicios

### LICENCIA
- MIT