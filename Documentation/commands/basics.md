# Funciones basicas

## rem

Se indica su funcionamiento en /Documentation/syntax.md

## pass

pass es la funcion mas simple de RLL, no recibe ningun argumento y no hace nada, es muy util cuand por ejemplo un if tiene un comportamiento para el bloque si pero no para el bloque else:

```rll
(set "pass" (input "Contraseña: ") )
(if (!= password "1234") (raise "Contraseña incorrecta") (pass) )
```

## exit

exit es para terminar el programa, tiene un solo argumento numero que es opcional de poner que representa el codigo de salida, por ejemplo si quieres salir y no ocurrio nada:

```rll
(exit)
```

o si ocurrio un error y quieres terminar el programa con un codigo de salida:

```rll
(exit 1)
```

## set

set es probablemente la funcion mas importante de RLL, sirve para declarar variables, recibe dos argumentos:
El primero esta en texto y sirve para el nombre de la variable, puede contener espacios pero las reglas sintaxicas van a hacer que una variable con espacios sea imposible de obtener y se tendra que usar `rename`
El segundo es simplemente el valor que se le dara a la variable.

## del

del sirve para borrar variables, despues de borrarla su valor y entrada se perdera, recibe un solo argumento de texto que es el nombre de la variable.
por ejemplo:

```rll
(set "temp" (num (input "Numero:" ) ) )
(del "temp")
```

## delf

delf funciona exactamente igual pero borra funciones, puedes borrar todas las funciones internas o tuyas que quieras pero borrar funciones buitlint podria romper modulos o codigo

```rll
(delf "print")
(print "Hola")
```

va a dar un error porque print habra dejado de existir.

## func

Su funcionamiento se describe en /Documentation/syntax.md

## join

join recibe un argumento obligatorio seguido de una cantidad infinita de argumentos opcionales, lo que hace es juntar todos los argumentos el primer argumento de separacion retornando siempre un string.
Por ejemplo

```rll
(print (join ", " 1 2 3 ) )
```

salida:

```text
1, 2, 3
```

## joinl

joinl recibe un argumento obligatorio seguido de un argumento que, lo que hace es juntar todos los elementos del segundo el primer argumento de separacion retornando siempre un string.
Por ejemplo

```rll
(print (joinl ", " (list 1 2 3) ) )
```

salida:

```text
1, 2, 3
```

## exec

`exec` recibe un unico argumento de texto y lo que hace es prosesarlo para poder ejecutarlo. Por ejemplo

```rll
(set "x" "Hola mundo!")
(exec "(print x)" )
```

salida:

```rll
Hola mundo!
```
