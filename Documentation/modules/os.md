# OS module Documentation

El modulo OS es como os de python, permite hacer unas cuantas cosas con el sistema operativo, tiene 7 funciones:

* system
* errexit
* mkdir
* remove
* get_cwd
* sep
* chdir

## system

Permite ejecutar comandos de shell desde el programa, por ejemplo

```rll
(import "os")
(system "echo Hola mundo!")
```

recibe un unico argumento.

## errexit

No acepta arguementos y termina el programa con el codigo de salida 1

## mkdir

Recibe un unico argumento que es el nombre de la carpeta que se quiere crea

```rll
(import "os")
(mkdir "Documentos")
```

## remove

Recibe un unico argumento que es el nombre del archivo a remover,

```rll
(import "os")
(remove "temporal.txt")
```

## get_cwd

No recibe argumentos, retorna la carpeta de trabajo actual del sistema

```rll
(import "os")
(print (gwt_cwd) )
```

⚠️ get_cwd crea un archivo temporal.

## sep

retorna el reparador de carpetas del sistema,

"\" para Windows
"/" para sistemas tipo POSIX

```rll
(import "os")
(print (sep) )
```

## chdir

Cambia la carpeta de trabajo actual

```rll
(import "os")
(chdir "Downloads")
(remove "temporal.txt")
```
